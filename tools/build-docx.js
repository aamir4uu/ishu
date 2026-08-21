const fs = require('fs');
const path = require('path');
const SP = '/tmp/claude-0/-home-user-ishu/89903e44-ab5e-50c4-8ae0-a56dee02f12e/scratchpad';
const D = require(path.join(SP, 'node_modules', 'docx'));
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, ExternalHyperlink,
  ImageRun, AlignmentType, BorderStyle, LevelFormat, convertInchesToTwip,
} = D;

// Usage: node build-docx.js <source.md> <output.docx>
const SRC = process.argv[2];
const OUT = process.argv[3];
if (!SRC || !OUT) { console.error('usage: node build-docx.js <source.md> <output.docx>'); process.exit(1); }

const INK   = '1A1A1A';
const HEAD  = '0F2E4C';
const MUTED = '5A6472';
const LINK  = '0B5FAE';
const NOTE  = 'A33A1F';

// ---------------------------------------------------------------- inline parse
// Splits a markdown line into runs, handling **bold** and [label](url).
function inline(text, opts = {}) {
  const base = { size: opts.size || 22, color: opts.color || INK, font: 'Calibri' };
  const out = [];
  const re = /(\*\*(.+?)\*\*)|(\[([^\]]+)\]\(([^)]+)\))/g;
  let last = 0, m;
  const push = (t, extra = {}) => {
    if (t) out.push(new TextRun({ ...base, ...opts.run, ...extra, text: t }));
  };
  while ((m = re.exec(text)) !== null) {
    push(text.slice(last, m.index));
    if (m[2] !== undefined) {
      push(m[2], { bold: true });
    } else {
      out.push(new ExternalHyperlink({
        link: m[5],
        children: [new TextRun({ ...base, ...opts.run, text: m[4], color: LINK, underline: {} })],
      }));
    }
    last = m.index + m[0].length;
  }
  push(text.slice(last));
  return out;
}

// ---------------------------------------------------------------- build blocks
const md = fs.readFileSync(SRC, 'utf8');
const lines = md.split('\n');
const docTitle = (md.match(/^#\s+(.+)$/m) || [, 'Untitled'])[1];
const kids = [];
let imgN = 0;

const para = (children, extra = {}) =>
  new Paragraph({ children, spacing: { after: 160, line: 300 }, ...extra });

for (let i = 0; i < lines.length; i++) {
  const raw = lines[i];
  const line = raw.trim();
  if (!line) continue;

  // --- image: placeholder frame + instruction + hyperlinked Image Source
  const img = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
  if (img) {
    imgN += 1;
    const alt = img[1], url = img[2];
    kids.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 260, after: 60 },
      children: [new ImageRun({
        type: 'png',
        data: fs.readFileSync(path.join(SP, 'placeholders', `placeholder-${imgN}.png`)),
        transformation: { width: 460, height: 259 },
        altText: { title: `Image ${imgN}`, description: alt, name: `Image ${imgN}` },
      })],
    }));
    kids.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 40 },
      children: [new TextRun({
        text: `[IMAGE ${imgN} PLACEHOLDER — download from the Image Source link below, then replace this box]`,
        size: 17, italics: true, color: NOTE, font: 'Calibri',
      })],
    }));
    kids.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 60 },
      children: [new TextRun({
        text: `Alt text: ${alt}`,
        size: 17, italics: true, color: MUTED, font: 'Calibri',
      })],
    }));
    // The caption the brief requires: the words "Image Source", hyperlinked.
    kids.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 300 },
      children: [new ExternalHyperlink({
        link: url,
        children: [new TextRun({
          text: 'Image Source',
          size: 18, color: LINK, underline: {}, font: 'Calibri',
        })],
      })],
    }));
    // Skip the markdown "[Image Source](...)" line that follows in the source.
    let j = i + 1;
    while (j < lines.length && !lines[j].trim()) j++;
    if (j < lines.length && /^\[Image Source\]\(/.test(lines[j].trim())) i = j;
    continue;
  }

  if (line === '---') {
    kids.push(new Paragraph({
      spacing: { before: 320, after: 240 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: 'D2D7DE', space: 8 } },
      children: [new TextRun('')],
    }));
    continue;
  }

  const h = line.match(/^(#{1,3})\s+(.*)$/);
  if (h) {
    const lvl = h[1].length;
    kids.push(new Paragraph({
      heading: [HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3][lvl - 1],
      spacing: lvl === 1 ? { after: 300 } : { before: lvl === 2 ? 400 : 300, after: 160 },
      children: inline(h[2], {
        size: lvl === 1 ? 40 : lvl === 2 ? 30 : 25,
        color: HEAD,
        run: { bold: true },
      }),
    }));
    continue;
  }

  const bullet = line.match(/^-\s+(.*)$/);
  if (bullet) {
    kids.push(new Paragraph({
      numbering: { reference: 'body-bullets', level: 0 },
      spacing: { after: 120, line: 300 },
      children: inline(bullet[1]),
    }));
    continue;
  }

  kids.push(para(inline(line)));
}

// ---------------------------------------------------------------- document
const doc = new Document({
  creator: 'Sitejet SEO and Content Team',
  title: docTitle,
  description: '',
  numbering: {
    config: [{
      reference: 'body-bullets',
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: '•',
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: convertInchesToTwip(0.35), hanging: convertInchesToTwip(0.22) } } },
      }],
    }],
  },
  styles: {
    default: {
      document: { run: { font: 'Calibri', size: 22, color: INK }, paragraph: { spacing: { line: 300 } } },
    },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },           // A4 portrait, DXA
        margin: { top: 1200, right: 1200, bottom: 1200, left: 1200 },
      },
    },
    children: kids,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log('wrote:', OUT);
  console.log('blocks:', kids.length, '| images:', imgN);
});
