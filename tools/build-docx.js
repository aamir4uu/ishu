const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

// docx is not vendored in this repo. Point DOCX_MODULES at a node_modules
// directory that has it, or install it next to this script.
function loadDocx() {
  const tries = [
    process.env.DOCX_MODULES && path.join(process.env.DOCX_MODULES, 'docx'),
    path.join(__dirname, 'node_modules', 'docx'),
    path.join(__dirname, '..', 'node_modules', 'docx'),
    'docx',
  ].filter(Boolean);
  for (const t of tries) {
    try { return require(t); } catch (e) { /* next */ }
  }
  console.error('cannot find the docx module. npm install docx somewhere and set DOCX_MODULES to that node_modules path.');
  process.exit(1);
}
const D = loadDocx();
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, ExternalHyperlink,
  ImageRun, AlignmentType, BorderStyle, LevelFormat, convertInchesToTwip,
  Table, TableRow, TableCell, WidthType, ShadingType,
} = D;

// Usage: node build-docx.js <source.md> <output.docx> [creator]
const SRC = process.argv[2];
const OUT = process.argv[3];
const CREATOR = process.argv[4] || process.env.DOCX_CREATOR || 'Content Team';
if (!SRC || !OUT) { console.error('usage: node build-docx.js <source.md> <output.docx> [creator]'); process.exit(1); }

// A Devanagari draft rendered in Calibri falls back to whatever Word picks.
// Nirmala UI ships with Windows and Office and covers both scripts, so it is
// safe to use for the whole document once any Devanagari is present.
const DEVANAGARI = /[\u0900-\u097F]/;
const SRC_TEXT = fs.readFileSync(SRC, 'utf8');
const FONT = DEVANAGARI.test(SRC_TEXT) ? 'Nirmala UI' : 'Calibri';

const INK   = '1A1A1A';
const HEAD  = '0F2E4C';
const MUTED = '5A6472';
const LINK  = '0B5FAE';
const NOTE  = 'A33A1F';

// ---------------------------------------------------------------- inline parse
// Splits a markdown line into runs, handling **bold** and [label](url).
function inline(text, opts = {}) {
  const base = { size: opts.size || 22, color: opts.color || INK, font: FONT };
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

// ---------------------------------------------------------------- placeholder
// A flat grey 16:9 frame, built here so the tool has no asset directory to
// carry around. One cached buffer, reused for every slot.
let PNG_CACHE = null;
function placeholderPng() {
  if (PNG_CACHE) return PNG_CACHE;
  const W = 640, H = 360;
  const raw = Buffer.alloc((W * 3 + 1) * H);
  let o = 0;
  for (let y = 0; y < H; y++) {
    raw[o++] = 0;                                  // filter byte: none
    for (let x = 0; x < W; x++) {
      const edge = x < 3 || y < 3 || x >= W - 3 || y >= H - 3;
      const v = edge ? 0xA8 : 0xEE;
      raw[o++] = v; raw[o++] = v; raw[o++] = v;
    }
  }
  const chunk = (type, data) => {
    const len = Buffer.alloc(4); len.writeUInt32BE(data.length, 0);
    const body = Buffer.concat([Buffer.from(type, 'ascii'), data]);
    const crc = Buffer.alloc(4); crc.writeUInt32BE(crc32(body) >>> 0, 0);
    return Buffer.concat([len, body, crc]);
  };
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(W, 0); ihdr.writeUInt32BE(H, 4);
  ihdr[8] = 8; ihdr[9] = 2; ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  PNG_CACHE = Buffer.concat([
    Buffer.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
    chunk('IHDR', ihdr),
    chunk('IDAT', zlib.deflateSync(raw)),
    chunk('IEND', Buffer.alloc(0)),
  ]);
  return PNG_CACHE;
}

let CRC_TABLE = null;
function crc32(buf) {
  if (!CRC_TABLE) {
    CRC_TABLE = new Int32Array(256);
    for (let n = 0; n < 256; n++) {
      let c = n;
      for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1;
      CRC_TABLE[n] = c;
    }
  }
  let c = -1;
  for (let i = 0; i < buf.length; i++) c = CRC_TABLE[(c ^ buf[i]) & 0xFF] ^ (c >>> 8);
  return c ^ -1;
}

// ---------------------------------------------------------------- build blocks
const md = SRC_TEXT;
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

  // --- markdown table -> a real Word table with a shaded header row
  if (line.startsWith('|') && line.endsWith('|')) {
    const block = [];
    let j = i;
    while (j < lines.length) {
      const t = lines[j].trim();
      if (!t.startsWith('|') || !t.endsWith('|')) break;
      block.push(t);
      j++;
    }
    const cells = (row) => row.slice(1, -1).split('|').map((c) => c.trim());
    const isRule = (row) => /^\|[\s:|-]+\|$/.test(row);
    const rows = block.filter((r) => !isRule(r)).map(cells);
    if (rows.length >= 2) {
      const cols = Math.max(...rows.map((r) => r.length));
      kids.push(new Table({
        width: { size: 100, type: WidthType.PERCENTAGE },
        rows: rows.map((cellsIn, rIdx) => new TableRow({
          tableHeader: rIdx === 0,
          children: Array.from({ length: cols }, (_, cIdx) => new TableCell({
            width: { size: Math.floor(100 / cols), type: WidthType.PERCENTAGE },
            shading: rIdx === 0
              ? { type: ShadingType.CLEAR, fill: 'EDF2F7', color: 'auto' }
              : undefined,
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({
              spacing: { after: 0, line: 280 },
              children: inline(cellsIn[cIdx] || '', {
                size: 21,
                run: rIdx === 0 ? { bold: true } : {},
                color: rIdx === 0 ? HEAD : INK,
              }),
            })],
          })),
        })),
      }));
      kids.push(new Paragraph({ spacing: { after: 240 }, children: [new TextRun('')] }));
      i = j - 1;
      continue;
    }
  }

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
        data: placeholderPng(imgN),
        transformation: { width: 460, height: 259 },
        altText: { title: `Image ${imgN}`, description: alt, name: `Image ${imgN}` },
      })],
    }));
    kids.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 40 },
      children: [new TextRun({
        text: `[IMAGE ${imgN} PLACEHOLDER — download from the Image Source link below, then replace this box]`,
        size: 17, italics: true, color: NOTE, font: FONT,
      })],
    }));
    kids.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 60 },
      children: [new TextRun({
        text: `Alt text: ${alt}`,
        size: 17, italics: true, color: MUTED, font: FONT,
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
          size: 18, color: LINK, underline: {}, font: FONT,
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
  creator: CREATOR,
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
      document: { run: { font: FONT, size: 22, color: INK }, paragraph: { spacing: { line: 300 } } },
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
