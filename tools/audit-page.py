#!/usr/bin/env python3
"""Audit a delivered Hero FinCorp page against the project checklist and its brief.

Checks what a machine can check: heading structure and APA title case, the
banner and its hyperlinked Image Source line, length in words and characters,
the sixteen humanizer gates, every section and FAQ the page brief mandates,
target keywords, the client CTA, internal links, and punctuation hygiene.

What it cannot check, and a person still must: whether a figure is true,
whether the prose repeats itself, and what a detector will actually score.

Usage: python3 tools/audit-page.py      (exit 1 if any check fails)
"""
import re, sys, json, subprocess
from pathlib import Path

# APA 7th: lowercase only minor words (articles, short prepositions and
# conjunctions) of THREE letters or fewer. "From", "With", "Into" are four
# letters and stay capitalised.
APA_LOWER = {"a","an","the","and","but","or","nor","for","so","yet","at","by","in","of","on","to","up","via","per","as","if","off","out","vs"}

def headings(md):
    return [(len(m.group(1)), m.group(2).strip()) for m in re.finditer(r'^(#{1,6})\s+(.*)$', md, re.M)]

def apa_ok(title):
    """APA: capitalise first, last, and all words of 4+ letters; minor words of <=3 letters lowercase."""
    # strip markdown/links/parens
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', title)
    t = re.sub(r'[*_`]', '', t)
    words = [w for w in re.split(r'[\s/]+', t) if w]
    bad = []
    for i, w in enumerate(words):
        core = re.sub(r'^[^\w]+|[^\w]+$', '', w)
        if not core or not core[0].isalpha(): continue
        if core.isupper() or len(core) <= 1: continue           # acronyms
        if re.match(r'^[a-z]-[A-Z]', core): continue            # e-KYC
        first_last = (i == 0 or i == len(words)-1)
        minor = core.lower() in APA_LOWER
        if first_last or not minor:
            if not core[0].isupper(): bad.append(core)
        else:
            if core[0].isupper() and core.lower() in APA_LOWER: bad.append(core + " (should be lowercase)")
    return bad

def audit(slug, brief):
    d = Path(f'blog/herofincorp/{slug}')
    md = (d / f'{slug}.md').read_text(encoding='utf-8')
    body = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    out = []
    ok = lambda c, label, detail='': out.append((c, label, detail))

    # 1. heading structure
    hs = headings(body)
    h1 = [t for lv, t in hs if lv == 1]
    ok(len(h1) == 1, "Exactly one H1", f"{len(h1)}: {h1[0] if h1 else 'none'}")
    levels = [lv for lv, _ in hs]
    ok(all(l in (1,2,3) for l in levels), "Only H1/H2/H3 used", f"levels present: {sorted(set(levels))}")
    jumps = [hs[i][1] for i in range(1, len(hs)) if hs[i][0] - hs[i-1][0] > 1]
    ok(not jumps, "No skipped heading levels", f"skips before: {jumps}")

    # 2. APA title case on every heading
    bad = {t: apa_ok(t) for lv, t in hs if apa_ok(t)}
    ok(not bad, "APA title case on all headings", json.dumps(bad)[:300] if bad else f"{len(hs)} headings checked")

    # 3. images: banner + hyperlinked Image Source under each
    imgs = re.findall(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', body, re.M)
    srcs = re.findall(r'^\[Image Source\]\(([^)]+)\)\s*$', body, re.M)
    ok(len(imgs) >= 1, "Has a banner image", f"{len(imgs)} image(s)")
    ok(len(imgs) == len(srcs), "Every image has an Image Source line", f"{len(imgs)} images / {len(srcs)} source lines")
    lines = body.split('\n')
    paired = 0
    for i, l in enumerate(lines):
        if re.match(r'^!\[', l.strip()):
            nxt = [x for x in lines[i+1:i+4] if x.strip()]
            if nxt and re.match(r'^\[Image Source\]\(https?://', nxt[0].strip()): paired += 1
    ok(paired == len(imgs), "Image Source directly below each image and hyperlinked", f"{paired}/{len(imgs)} paired")
    first_block = body.split('##')[0]
    ok(bool(re.search(r'^!\[', first_block, re.M)), "Banner sits at the top, before the first H2")

    # 4. length + characters
    o = subprocess.run(['python3','tools/count-words.py', str(d/f'{slug}.md'),'--min','0','--max','99999'], capture_output=True, text=True).stdout.split()
    w, c = int(o[0]), int(o[2])
    ok(c >= 5000, "At least 5,000 characters", f"{c:,}")
    ok(w <= 1000 + 35, "Within the 1,000-word extreme-case ceiling", f"{w:,} words")

    # 5. humanizer gates
    j = json.loads(subprocess.run(['python3','.claude/skills/humanizer/scripts/zerogpt_preflight.py', str(d/f'{slug}.md'),'--json'], capture_output=True, text=True).stdout)
    ok(not j['failed'], "All 16 humanizer gates pass", ', '.join(j['failed']) if j['failed'] else "16/16")

    # 6. brief: mandated sections
    for name, pat in brief['sections']:
        ok(bool(re.search(pat, body, re.I|re.M)), f"Brief section present: {name}")
    # 7. brief: FAQ count
    faq_h = [t for lv, t in hs if lv == 3 and t.rstrip().endswith('?')]
    ok(len(faq_h) >= brief['faq_min'], f"At least {brief['faq_min']} FAQ questions", f"{len(faq_h)} found")
    for q in brief['faqs']:
        ok(any(q.lower() in t.lower() for t in faq_h), f"Brief FAQ present: {q[:52]}")
    # 8. keywords
    low = body.lower()
    for kw in brief['keywords']:
        ok(kw.lower() in low, f"Keyword present: {kw}")
    # 9. CTA and internal links
    ok('Apply Now' in body, "Client CTA retained")
    internal = len(re.findall(r'\]\(https://(?:www\.|loans\.apps\.)?herofincorp\.com', body))
    ok(internal >= 2, "Internal herofincorp links retained", f"{internal} link(s)")
    # 10. punctuation hygiene
    ok('—' not in body, "No em dashes")
    ok(not any(ch in body for ch in '“”‘’'), "No curly quotes")
    return out, w, c

BRIEFS = {
 'what-is-ekyc': {
   'sections': [("Offline e-KYC (H3)", r'^###\s.*Offline e-KYC'), ("Video KYC (H3)", r'^###\s.*Video KYC'),
                ("e-KYC Process Explained Step by Step (H2)", r'^##\s+e-KYC Process Explained Step by Step'),
                ("How to Apply for e-KYC Online (H2)", r'^##\s+How to Apply for e-KYC Online')],
   'faq_min': 4,
   'faqs': ["Full Form of e-KYC", "Difference Between Aadhaar e-KYC and Video KYC", "Why Does e-KYC Sometimes Fail", "Mandatory for a Personal Loan"],
   'keywords': ["e-KYC full form", "ekyc process".replace('ekyc','e-KYC'), "How to apply for e-KYC online", "What Is e-KYC"]},
 'msme-loan': {
   'sections': [("How Is an MSME Loan Used? (H2)", r'^##\s+How Is an MSME Loan Used\?')],
   'faq_min': 4,
   'faqs': ["Documents Are Required for an MSME Loan", "Repayment Tenure for an MSME Loan", "Subsidies Available on MSME Loans", "Minimum Credit Score Required"],
   'keywords': ["MSME loan eligibility", "What Is an MSME Loan", "21 to 65", "Types of MSME Loans"]},
 'working-capital-loan': {
   'sections': [("Advantages of Working Capital Loans (H2)", r'^##\s+Advantages of Working Capital Loans'),
                ("Key Features of a Working Capital Loan (H2)", r'^##\s+Key Features of a Working Capital Loan')],
   'faq_min': 7,
   'faqs': ["Calculate My Business's Working Capital Requirement", "Documents Do I Need", "Interest Rate on a Working Capital Loan",
            "Secured or Unsecured", "Different From a Term Loan", "Without Collateral", "How Quickly"],
   'keywords': ["benefit of a working capital loan", "features of a working capital loan", "working capital loan", "Eligibility"]},
}
fails = 0
for slug, brief in BRIEFS.items():
    res, w, c = audit(slug, brief)
    bad = [r for r in res if not r[0]]
    fails += len(bad)
    print("="*92); print(f"{slug}   {w:,} words / {c:,} characters   {len(res)-len(bad)}/{len(res)} checks pass"); print("="*92)
    for good, label, detail in res:
        print(f"  {'PASS' if good else 'FAIL'}  {label}" + (f"  [{detail}]" if detail else ""))
print(f"\nTOTAL FAILURES: {fails}")
sys.exit(1 if fails else 0)
