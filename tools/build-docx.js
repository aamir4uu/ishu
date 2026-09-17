#!/usr/bin/env node
// Markdown -> Word (.docx) builder for content deliverables.
//
// Usage:
//   node tools/build-docx.js <source.md> <output.docx> [--creator "Team name"] [--images <dir>] [--no-notes] [--no-alt]
//
//   --no-notes  leave HTML-comment editor notes out of the Word file
//   --no-alt    do not print the alt text under each image (it stays in the image's alt attribute)
//
// Environment:
//   NODE_PATH        where the `docx` npm package lives, if not resolvable from the cwd
//   DOCX_CREATOR     default document creator (overridden by --creator)
//   PLACEHOLDER_DIR  directory holding placeholder-N.png frames for image slots that
//                    point at a remote URL (default: <source dir>/placeholders,
//                    then tools/placeholders next to this script)
//
// Markdown handled:
//   # / ## / ###          real Word Heading 1/2/3 styles
//   - item                bullet list (proper numbering config)
//   1. item               numbered list
//   | a | b |             pipe table (first row is the header)
//   ![alt](path-or-url)   image slot. A local path (relative to the source file, or
//                         --images dir) is embedded as the real picture. A remote URL
//                         gets a sized placeholder frame plus an instruction line.
//                         Either way the caption beneath is the words "Image Source",
//                         hyperlinked to the URL given on the following
//                         [Image Source](url) line (or to the image URL itself).
//   <!-- note -->         editor note: italic, coloured, not part of the page copy
//   ---                   horizontal rule
//   **bold**, [label](url) inline
'use strict';
const fs = require('fs');
const path = require('path');

function loadDocx() {
  const candidates = [
    'docx',
    path.join(process.cwd(), 'node_modules', 'docx'),
    path.join(__dirname, 'node_modules', 'docx'),
    path.join(__dirname, '..', 'node_modules', 'docx'),
  ];
  for (const c of candidates) { try { return require(c); } catch (e) { /* next */ } }
  console.error('cannot find the `docx` package. Run `npm install docx` or set NODE_PATH.');
  process.exit(1);
}
const D = loadDocx();
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, ExternalHyperlink, ImageRun,
  AlignmentType, BorderStyle, LevelFormat, convertInchesToTwip, Table, TableRow,
  TableCell, WidthType, ShadingType,
} = D;

// ---------------------------------------------------------------- args
const args = process.argv.slice(2);
const positional = [];
const opts = { creator: process.env.DOCX_CREATOR || 'SEO and Content Team', images: null, notes: true, altLine: true };
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--creator') opts.creator = args[++i];
  else if (args[i] === '--images') opts.images = args[++i];
  else if (args[i] === '--no-notes') opts.notes = false;
  else if (args[i] === '--no-alt') opts.altLine = false;
  else positional.push(args[i]);
}
const [SRC, OUT] = positional;
if (!SRC || !OUT) {
  console.error('usage: node build-docx.js <source.md> <output.docx> [--creator NAME] [--images DIR] [--no-notes] [--no-alt]');
  process.exit(1);
}
const SRC_DIR = path.dirname(path.resolve(SRC));
const PLACEHOLDER_DIRS = [
  process.env.PLACEHOLDER_DIR,
  path.join(SRC_DIR, 'placeholders'),
  path.join(__dirname, 'placeholders'),
].filter(Boolean);

const INK = '1A1A1A', HEAD = '0F2E4C', MUTED = '5A6472', LINK = '0B5FAE', NOTE = 'A33A1F', RULE = 'D2D7DE';
const FONT = 'Calibri';

// ---------------------------------------------------------------- inline parse
function inline(text, o = {}) {
  const base = { size: o.size || 22, color: o.color || INK, font: FONT };
  const out = [];
  const re = /(\*\*(.+?)\*\*)|(\[([^\]]+)\]\(([^)]+)\))/g;
  let last = 0, m;
  const push = (t, extra = {}) => { if (t) out.push(new TextRun({ ...base, ...o.run, ...extra, text: t })); };
  while ((m = re.exec(text)) !== null) {
    push(text.slice(last, m.index));
    if (m[2] !== undefined) push(m[2], { bold: true });
    else out.push(new ExternalHyperlink({
      link: m[5],
      children: [new TextRun({ ...base, ...o.run, text: m[4], color: LINK, underline: {} })],
    }));
    last = m.index + m[0].length;
  }
  push(text.slice(last));
  return out;
}

function imageBytes(ref) {
  if (/^https?:\/\//i.test(ref)) return null;
  const tries = [path.resolve(SRC_DIR, ref), opts.images ? path.resolve(opts.images, ref) : null, path.resolve(ref)].filter(Boolean);
  for (const t of tries) if (fs.existsSync(t)) return { data: fs.readFileSync(t), type: path.extname(t).slice(1).toLowerCase() === 'jpg' ? 'jpg' : path.extname(t).slice(1).toLowerCase() };
  return null;
}
function placeholderBytes(n) {
  for (const d of PLACEHOLDER_DIRS) {
    const p = path.join(d, `placeholder-${n}.png`);
    if (fs.existsSync(p)) return fs.readFileSync(p);
    const g = path.join(d, 'placeholder.png');
    if (fs.existsSync(g)) return fs.readFileSync(g);
  }
  return null;
}
function pngSize(buf) { return { w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) }; }
function jpgSize(buf) {
  let i = 2;
  while (i < buf.length) {
    if (buf[i] !== 0xff) { i++; continue; }
    const marker = buf[i + 1];
    if (marker >= 0xc0 && marker <= 0xc3) return { h: buf.readUInt16BE(i + 5), w: buf.readUInt16BE(i + 7) };
    i += 2 + buf.readUInt16BE(i + 2);
  }
  return { w: 16, h: 9 };
}
function fitWidth(buf, type, maxW) {
  const s = type === 'png' ? pngSize(buf) : jpgSize(buf);
  const w = Math.min(maxW, s.w);
  return { width: w, height: Math.round((s.h / s.w) * w) };
}

// ---------------------------------------------------------------- build blocks
const md = fs.readFileSync(SRC, 'utf8');
const lines = md.split('\n');
const docTitle = (md.match(/^#\s+(.+)$/m) || [, 'Untitled'])[1].replace(/\*\*/g, '');
const kids = [];
let imgN = 0, embedded = 0, placeholders = 0;
let numberedInstance = 0;

const para = (children, extra = {}) => new Paragraph({ children, spacing: { after: 160, line: 300 }, ...extra });
const noteRun = (text, color = NOTE) => new TextRun({ text, size: 17, italics: true, color, font: FONT });

function pushTable(rows) {
  const cells = rows.map((r) => r.replace(/^\|/, '').replace(/\|$/, '').split('|').map((c) => c.trim()));
  const header = cells[0];
  const body = cells.slice(1).filter((r) => !r.every((c) => /^:?-{2,}:?$/.test(c)));
  const cols = header.length;
  const colW = Math.floor(9506 / cols); // A4 text width in DXA with 1200 margins
  const mk = (text, isHead) => new TableCell({
    width: { size: colW, type: WidthType.DXA },
    shading: isHead ? { type: ShadingType.CLEAR, fill: 'EEF2F6', color: 'auto' } : undefined,
    margins: { top: 80, bottom: 80, left: 110, right: 110 },
    children: [new Paragraph({ spacing: { after: 0, line: 276 }, children: inline(text, { size: 20, run: isHead ? { bold: true } : {} }) })],
  });
  kids.push(new Table({
    width: { size: 9506, type: WidthType.DXA },
    columnWidths: Array(cols).fill(colW),
    rows: [new TableRow({ tableHeader: true, children: header.map((c) => mk(c, true)) })]
      .concat(body.map((r) => new TableRow({ children: Array.from({ length: cols }, (_, i) => mk(r[i] || '', false)) }))),
  }));
  kids.push(new Paragraph({ spacing: { after: 200 }, children: [new TextRun('')] }));
}

for (let i = 0; i < lines.length; i++) {
  const line = lines[i].trim();
  if (!line) continue;

  // editor note
  const note = line.match(/^<!--\s*(.*?)\s*-->$/);
  if (note) {
    const body = note[1];
    if (!opts.notes || /^NEW SECTION END$/i.test(body)) continue;
    let label;
    if (/^NEW SECTION START:/i.test(body)) label = `[New section: ${body.replace(/^NEW SECTION START:\s*/i, '')}]`;
    else if (/^EDIT:/i.test(body)) label = `[Edit to existing copy: ${body.replace(/^EDIT:\s*/i, '')}]`;
    else label = `[Editor note: ${body}]`;
    kids.push(new Paragraph({ spacing: { before: 160, after: 100 }, children: [noteRun(label)] }));
    continue;
  }

  // image slot
  const img = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
  if (img) {
    imgN += 1;
    const alt = img[1], ref = img[2];
    // find the [Image Source](url) line that follows, if any
    let j = i + 1;
    while (j < lines.length && !lines[j].trim()) j++;
    let sourceUrl = /^https?:\/\//i.test(ref) ? ref : null;
    if (j < lines.length) {
      const src = lines[j].trim().match(/^\[Image Source\]\(([^)]+)\)$/i);
      if (src) { sourceUrl = src[1]; i = j; }
    }
    const real = imageBytes(ref);
    let buf, type, note2;
    if (real) {
      buf = real.data; type = real.type; embedded += 1;
    } else {
      buf = placeholderBytes(imgN); type = 'png'; placeholders += 1;
      note2 = '[Image placeholder]';
    }
    if (buf) {
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { before: 260, after: 60 },
        children: [new ImageRun({
          type, data: buf, transformation: fitWidth(buf, type, 460),
          altText: { title: `Image ${imgN}`, description: alt, name: `Image ${imgN}` },
        })],
      }));
    }
    if (note2) kids.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [noteRun(note2)] }));
    if (opts.altLine) kids.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [noteRun(`Alt text: ${alt}`, MUTED)] }));
    if (sourceUrl) {
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { after: 300 },
        children: [new ExternalHyperlink({ link: sourceUrl, children: [new TextRun({ text: 'Image Source', size: 18, color: LINK, underline: {}, font: FONT })] })],
      }));
    }
    continue;
  }

  if (line === '---') {
    kids.push(new Paragraph({
      spacing: { before: 320, after: 240 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 8 } },
      children: [new TextRun('')],
    }));
    continue;
  }

  // table
  if (line.startsWith('|')) {
    const rows = [line];
    while (i + 1 < lines.length && lines[i + 1].trim().startsWith('|')) rows.push(lines[++i].trim());
    pushTable(rows);
    continue;
  }

  const h = line.match(/^(#{1,4})\s+(.*)$/);
  if (h) {
    const lvl = Math.min(h[1].length, 4);
    kids.push(new Paragraph({
      heading: [HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3, HeadingLevel.HEADING_4][lvl - 1],
      spacing: lvl === 1 ? { after: 300 } : { before: lvl === 2 ? 400 : 300, after: 160 },
      children: inline(h[2], { size: [40, 30, 25, 23][lvl - 1], color: HEAD, run: { bold: true } }),
    }));
    continue;
  }

  const bullet = line.match(/^[-*]\s+(.*)$/);
  if (bullet) {
    kids.push(new Paragraph({ numbering: { reference: 'body-bullets', level: 0 }, spacing: { after: 120, line: 300 }, children: inline(bullet[1]) }));
    continue;
  }
  const num = line.match(/^\d+\.\s+(.*)$/);
  if (num) {
    // start a fresh numbered sequence whenever the previous line was not a numbered item
    const prev = (lines[i - 1] || '').trim();
    if (!/^\d+\.\s+/.test(prev)) numberedInstance += 1;
    kids.push(new Paragraph({ numbering: { reference: 'body-numbers', level: 0, instance: numberedInstance }, spacing: { after: 120, line: 300 }, children: inline(num[1]) }));
    continue;
  }

  kids.push(para(inline(line)));
}

// ---------------------------------------------------------------- document
const listStyle = { paragraph: { indent: { left: convertInchesToTwip(0.35), hanging: convertInchesToTwip(0.22) } } };
const doc = new Document({
  creator: opts.creator,
  title: docTitle,
  description: '',
  numbering: {
    config: [
      { reference: 'body-bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: listStyle }] },
      { reference: 'body-numbers', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: listStyle }] },
    ],
  },
  styles: {
    default: { document: { run: { font: FONT, size: 22, color: INK }, paragraph: { spacing: { line: 300 } } } },
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1200, right: 1200, bottom: 1200, left: 1200 } } },
    children: kids,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log('wrote:', OUT);
  console.log(`blocks: ${kids.length} | images: ${imgN} (embedded ${embedded}, placeholder ${placeholders})`);
});
