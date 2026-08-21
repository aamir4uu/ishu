"""Shared detector library for the evolving humanizer skill.

Every detector returns a list of Hit objects. Hits carry the signal name, the
span of text that triggered them, and a raw magnitude. scan.py turns hits into
a weighted risk score; learn.py uses the same detectors to work out which
signals actually correlate with what ZeroGPT flags.

Keeping the detectors in one module means the scanner and the learner can never
drift apart.
"""

import collections
import json
import os
import re
import statistics
from dataclasses import dataclass, asdict

HERE = os.path.dirname(os.path.abspath(__file__))
MEMORY = os.path.normpath(os.path.join(HERE, "..", "memory"))


@dataclass
class Hit:
    signal: str
    span: str
    magnitude: float
    note: str = ""
    members: tuple = ()

    def to_dict(self):
        return asdict(self)


# ---------------------------------------------------------------- text utils

SENT_SPLIT = re.compile(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z0-9\"'(\[])")
MD_NOISE = re.compile(
    r"^(\s*[-*+]\s+|\s*\d+[.)]\s+|\s*>\s?|#{1,6}\s+|\s*\|.*\|\s*$)", re.M
)


def strip_markdown(text):
    """Remove markdown scaffolding but keep the prose, so detectors see what a
    reader (and a detector like ZeroGPT) sees."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return text


def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def body_paragraphs(text):
    """Prose paragraphs only: no headings, no list blocks, no tables."""
    out = []
    for p in paragraphs(text):
        first = p.lstrip().splitlines()[0] if p.strip() else ""
        if first.startswith("#") or first.startswith("|"):
            continue
        if re.match(r"^\s*([-*+]|\d+[.)])\s+", first):
            continue
        out.append(p)
    return out


def sentences(text):
    """Split markdown into prose sentences.

    Two things make this harder than a regex on periods:

    * Markdown is often hard-wrapped, so a single sentence spans several lines.
      Treating every newline as a boundary chops sentences mid-clause and
      wrecks the sentence-length statistics.
    * Markdown also uses newlines as genuine boundaries, for list items and for
      the bolded question line of an FAQ. Joining those loses real breaks.

    So we rebuild blocks first: consecutive lines join into one block unless the
    next line starts a new structural element. Then we split each block.

    Headings and table rows are dropped entirely. They are structure, not
    prose, and counting a three-word H2 as a sentence fakes burstiness the
    reader never experiences.
    """
    text = strip_markdown(text)

    NEW_BLOCK = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|>\s?|\*\*)")
    # An italicised bare link on its own line is an image credit line, not
    # prose. This matches the standing finding in references/learning-log.md:
    # credit lines are not sentences a detector weighs, and counting them
    # produced a phantom repeated-opener hit on "Image source".
    # strip_markdown() has already turned "[Image source](url)" into
    # "Image source", so match the italic wrapper that survives rather than the
    # link syntax that does not. A whole line in single italics is a caption.
    # "**...**" does not match, so FAQ question lines are kept.
    CREDIT = re.compile(r"^\s*\*[^*]+\*\s*$")
    blocks, current = [], []
    for line in text.splitlines():
        st = line.strip()
        if not st:
            if current:
                blocks.append(" ".join(current))
                current = []
            continue
        if (st.startswith("#") or (st.startswith("|") and st.endswith("|"))
                or CREDIT.match(st)):
            if current:
                blocks.append(" ".join(current))
                current = []
            continue
        if NEW_BLOCK.match(line) and current:
            blocks.append(" ".join(current))
            current = []
        current.append(MD_NOISE.sub("", line).strip())
    if current:
        blocks.append(" ".join(current))

    out = []
    for block in blocks:
        block = re.sub(r"\s+", " ", block).strip()
        if len(block) < 2:
            continue
        out.extend(x.strip() for x in SENT_SPLIT.split(block))
    return [x for x in out if len(x) > 1]


def words(s):
    return re.findall(r"[A-Za-z']+", s)


def norm(s):
    """Normalised form used to match a ZeroGPT-reported span back to the draft."""
    return re.sub(r"[^a-z0-9 ]", " ", strip_markdown(s).lower())


def squash(s):
    return re.sub(r"\s+", " ", norm(s)).strip()


# ------------------------------------------------------------------ lexicons

BASE_WORDS = [
    "delve", "tapestry", "vibrant", "landscape", "realm", "embark", "excels",
    "comprehensive", "intricate", "intricacies", "pivotal", "moreover",
    "arguably", "notably", "robust", "myriad", "utilize", "utilise", "leverage",
    "elevate", "captivate", "resonate", "resonates", "foster", "fostering",
    "endeavor", "endeavour", "unleash", "offerings", "adhere", "multifaceted",
    "testament", "underscore", "underscores", "showcase", "showcases",
    "seamless", "seamlessly", "crucial", "vital", "paramount", "harness",
    "transformative", "groundbreaking", "boasts", "nestled", "renowned",
    "meticulous", "meticulously", "bolster", "encompass", "encompasses",
    "garner", "interplay", "cornerstone", "holistic", "invaluable",
    "unparalleled", "profound", "curated", "empower", "empowers", "navigate",
    "navigating", "streamline", "streamlining", "ever-evolving", "seamless",
]

BASE_PHRASES = [
    "streamline your workflow", "dive into", "it's important to note",
    "it is important to note", "it's important to remember",
    "navigating the complexities", "delving into the intricacies",
    "a testament to", "a treasure trove", "in today's digital age",
    "in today's fast-paced", "harness the power", "key to unlocking",
    "play a crucial role", "plays a crucial role", "in the realm of",
    "at the forefront", "more crucial than ever", "more important than ever",
    "unlock the full potential", "embrace the journey", "ever-changing",
    "profound impact", "has revolutionized", "has revolutionised",
    "evokes a sense of", "foundational elements", "in an era where",
    "a cornerstone of", "digital-first world", "when it comes to",
    "in conclusion", "let's dive in", "let's explore", "let's break",
    "here's what you need to know", "without further ado", "at its core",
    "the real question is", "what really matters", "the heart of the matter",
    "game-changer", "game changer", "best of both worlds", "the bottom line is",
    "whether you're a", "look no further", "in this article, we'll",
    "by the end of this", "buckle up", "the good news is",
    "that being said", "with that said", "needless to say",
    "in the ever-evolving", "rapidly evolving", "stay ahead of the curve",
    "take your", "to the next level", "make no mistake",
    "in order to", "align with", "best practices", "across the board",
    "meaningful outcomes", "drive meaningful", "at scale", "moving forward",
    "due to the fact that", "at this point in time", "in the event that",
    "has the ability to", "a wide range of", "a variety of",
]

HEDGES = [
    "arguably", "potentially", "possibly", "generally speaking", "it could be",
    "somewhat", "relatively", "fairly", "quite possibly", "may or may not",
    "tends to", "often times", "in many cases", "for the most part",
]

TRANSITIONS = [
    "however", "additionally", "moreover", "furthermore", "in addition",
    "consequently", "therefore", "thus", "nevertheless", "nonetheless",
    "ultimately", "overall", "in essence", "that said", "on the other hand",
    "as a result", "in summary", "to summarize", "to summarise", "notably",
    "importantly", "significantly", "essentially", "fundamentally",
]

COPULA_DODGE = re.compile(
    r"\b(serves? as|stands? as|acts? as|functions? as|represents? a|marks? a|"
    r"boasts?|features? a|offers? a|remains? a)\b", re.I
)

PARTICIPIAL_TAIL = re.compile(
    r",\s+(?:thereby\s+|thus\s+)?(highlight|underscor|emphasis|ensur|reflect|"
    r"symboliz|symbolis|contribut|cultivat|foster|encompass|showcas|allow|"
    r"help|creat|mak|driv|deliver|enabl|provid|offer|position|solidif|"
    r"demonstrat|signal|prov)\w*ing\b", re.I
)

NEG_PARALLEL = re.compile(
    r"\b(not (just|only|merely|simply)\b[^.?!]{0,90}?\b(but|it'?s|they'?re))|"
    r"\b(isn'?t|aren'?t|wasn'?t)\s+(just|only|merely|about)\b", re.I
)

RULE_OF_THREE = re.compile(
    r"\b([A-Za-z][\w'-]*(?:\s+[\w'-]+){0,3}),\s+([A-Za-z][\w'-]*(?:\s+[\w'-]+){0,3}),"
    r"\s+and\s+([A-Za-z][\w'-]*(?:\s+[\w'-]+){0,3})\b"
)

FALSE_RANGE = re.compile(r"\bfrom\s+[^.,;]{3,40}\s+to\s+[^.,;]{3,40}\b", re.I)

BOLD_HEADER_ITEM = re.compile(r"^\s*[-*+]\s+\*\*[^*]{2,60}\*\*\s*:", re.M)

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF⭐✅❌]"
)

CURLY = re.compile("[‘’“”]")
EMDASH = re.compile("[—–]")

CONTRACTION = re.compile(
    r"\b\w+(?:'|’)(?:s|t|re|ve|ll|d|m)\b", re.I
)

CHALLENGES_TROPE = re.compile(
    r"\b(despite (its|these|the|such)[^.?!]{0,40}challenges?|"
    r"faces? (several|a number of|various) challenges|"
    r"challenges and (legacy|future|opportunities)|future outlook)\b", re.I
)

GENERIC_CLOSER = re.compile(
    r"\b(the future looks bright|exciting times (lie ahead|await)|"
    r"a step in the right direction|only time will tell|"
    r"the possibilities are endless|continues to (thrive|evolve)|"
    r"one thing is (for )?certain|the journey (has just begun|continues)|"
    r"here'?s to)\b", re.I
)

CHATBOT = re.compile(
    r"\b(i hope this helps|of course!|certainly!|you'?re absolutely right|"
    r"would you like|let me know if|here is a|as an ai|as of my last)\b", re.I
)


# --------------------------------------------------------- parallel structure

FUNCTION_WORDS = set("""a an the and or but if of to in on for with at by from as is are was
were be been being it its this that these those you your we our they their he she her them us
not no so than then there here what which who how when where why can could should would will
may might must do does did have has had i me my more most much many very just also into over
under about across per each other some any it's you're don't isn't aren't won't can't""".split())

NUMERAL = re.compile(r"\b\d[\d,.:]*\b")


def shape_signature(sent):
    """A sentence's grammatical shape, with the content stripped out.

    Numbers collapse to '#' and content words to '*', so
    "A 45-second Reel stretched to 90 ..." and
    "A 25-second Reel that most viewers watch ..." come out with the same
    opening even though they share almost no vocabulary. That is the thing a
    perplexity model notices and a word-level check never will.
    """
    text = NUMERAL.sub(" # ", sent.lower())
    toks = re.findall(r"#|[a-z']+", text)
    skeleton = []
    for t in toks:
        if t == "#":
            skeleton.append("#")
        elif t in FUNCTION_WORDS:
            skeleton.append(t)
        else:
            skeleton.append("*")
    # Hyphens are word-internal ("how-tos", "45-second") and must not make two
    # otherwise identical templates look different.
    punct = "".join(c for c in sent if c in ":;,()")
    punct = re.sub(r"(.)\1+", r"\1", punct)
    return skeleton, punct, toks


def opening_key(sent, n=4):
    skeleton, _, toks = shape_signature(sent)
    if len(toks) < n:
        return None
    # Mix the skeleton with the actual first word, so "A # * *" only matches
    # another sentence that also literally starts with "a".
    return (toks[0], tuple(skeleton[:n]))


def skeleton_similarity(a, b):
    """How much of one sentence's template survives in the other's.

    Longest common subsequence over the full skeleton, not a bag of function
    words. Order is the whole point: "<phrase>: # to # seconds, <qualifier>"
    repeated three times is a template, and a set-overlap measure cannot see
    the difference between that and two sentences that merely share the word
    "to".
    """
    if not a or not b:
        return 0.0
    la, lb = len(a), len(b)
    prev = [0] * (lb + 1)
    for i in range(1, la + 1):
        cur = [0] * (lb + 1)
        ai = a[i - 1]
        for j in range(1, lb + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = cur[j - 1] if cur[j - 1] >= prev[j] else prev[j]
        prev = cur
    return prev[lb] / max(la, lb)


def parallel_hits(sents, window=4):
    """Find sentences built to the same template as a neighbour.

    Two checks, both learned from the 2026-08-21 ZeroGPT report, where every
    highlighted passage was one half of a matched pair or triad:

    * Matching openings anywhere in the document. Catches "A 45-second Reel ..."
      against "A 25-second Reel ..." three paragraphs later.
    * Matching skeletons among near neighbours. Catches a run of list items all
      shaped "<phrase>: # to # seconds, <qualifier>".
    """
    hits = []
    if len(sents) < 3:
        return hits

    shapes = [shape_signature(s) for s in sents]

    by_open = {}
    for i, s in enumerate(sents):
        k = opening_key(s)
        if k and len([t for t in k[1] if t != "*"]) >= 1:
            by_open.setdefault(k, []).append(i)
    for k, idxs in by_open.items():
        if len(idxs) >= 2:
            hits.append(Hit(
                "parallel_opening",
                f"{k[0]} " + " ".join(k[1][1:]),
                float(len(idxs) - 1),
                f"{len(idxs)} sentences open to the same template: "
                + " / ".join(sents[i][:52] for i in idxs[:3]),
                tuple(idxs),
            ))

    seen = set()
    for i in range(len(sents)):
        for j in range(i + 1, min(i + 1 + window, len(sents))):
            if (i, j) in seen:
                continue
            sk_a, pu_a, tk_a = shapes[i]
            sk_b, pu_b, tk_b = shapes[j]
            if len(tk_a) < 6 or len(tk_b) < 6:
                continue
            if pu_a != pu_b:
                continue
            if sk_a.count("#") != sk_b.count("#"):
                continue
            longer = max(len(tk_a), len(tk_b))
            if abs(len(tk_a) - len(tk_b)) / longer > 0.45:
                continue
            # Shape alone over-fires: two unrelated sentences can share a
            # skeleton by accident. A real template repeat also shares an
            # anchor, either a number in the same slot or a content word.
            content_a = {t for t in tk_a if t not in FUNCTION_WORDS and t != "#"}
            content_b = {t for t in tk_b if t not in FUNCTION_WORDS and t != "#"}
            anchored = bool(content_a & content_b) or sk_a.count("#") > 0
            if not anchored:
                continue

            sim = skeleton_similarity(sk_a, sk_b)
            if sim >= 0.62:
                seen.add((i, j))
                hits.append(Hit(
                    "parallel_structure",
                    f"{sents[i][:46]} ... / {sents[j][:46]} ...",
                    round(sim, 2),
                    f"same punctuation, same numeral count, {sim:.0%} skeleton "
                    f"overlap",
                    (i, j),
                ))
    return hits


# ------------------------------------------------------------------ memory IO

def load_rules():
    """Learned rules promoted by learn.py from real ZeroGPT reports."""
    path = os.path.join(MEMORY, "learned_rules.json")
    if not os.path.exists(path):
        return {"phrases": {}, "words": {}, "structures": {}}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_never_promote():
    """Terms the miner must never promote, however often they co-occur with a
    flag. Topic vocabulary is the main case: an article about remote work will
    have "remote work" in most of its flagged sentences without that phrase
    being an AI tell at all."""
    path = os.path.join(MEMORY, "never_promote.txt")
    if not os.path.exists(path):
        return set()
    out = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#")[0].strip().lower()
            if line:
                out.add(line)
    return out


def load_state():
    path = os.path.join(MEMORY, "state.json")
    if not os.path.exists(path):
        return default_state()
    with open(path, encoding="utf-8") as fh:
        st = json.load(fh)
    base = default_state()
    base.update(st)
    for k, v in default_state()["weights"].items():
        base["weights"].setdefault(k, v)
    return base


def save_state(state):
    os.makedirs(MEMORY, exist_ok=True)
    with open(os.path.join(MEMORY, "state.json"), "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
        fh.write("\n")


def default_state():
    return {
        "skill_version": "1.0.0",
        "sessions": 0,
        "reports_ingested": 0,
        "history": [],
        # Starting weights are a prior, not a truth. learn.py moves them every
        # time a real ZeroGPT report comes back.
        "weights": {
            "low_burstiness": 14.0,
            "uniform_paragraphs": 6.0,
            "mid_band_clustering": 8.0,
            "repeated_openers": 7.0,
            "participial_tail": 9.0,
            "transition_density": 6.0,
            "rule_of_three": 6.0,
            "negative_parallelism": 8.0,
            "copula_dodge": 6.0,
            "ai_word": 7.0,
            "ai_phrase": 9.0,
            "learned_phrase": 12.0,
            "learned_word": 8.0,
            "hedging": 4.0,
            "em_dash": 4.0,
            "curly_quote": 2.0,
            "emoji": 3.0,
            "bold_header_item": 5.0,
            "false_range": 4.0,
            "chatbot_artifact": 10.0,
            "no_contractions": 5.0,
            "long_sentence": 3.0,
            "challenges_trope": 9.0,
            "generic_closer": 9.0,
            "parallel_opening": 13.0,
            "parallel_structure": 13.0,
        },
    }


# ---------------------------------------------------------------- detectors

def sentence_hits(sent, rules=None):
    """Signals detectable inside a single sentence."""
    rules = rules or load_rules()
    hits = []
    low = sent.lower()
    w = words(sent)

    for phrase in BASE_PHRASES:
        if phrase in low:
            hits.append(Hit("ai_phrase", phrase, 1.0))
    for term in BASE_WORDS:
        if re.search(r"\b" + re.escape(term) + r"\b", low):
            hits.append(Hit("ai_word", term, 1.0))

    for phrase, meta in rules.get("phrases", {}).items():
        if phrase in low:
            hits.append(Hit("learned_phrase", phrase, 1.0,
                            f"learned s{meta.get('first_seen_session', '?')}"
                            f" x{meta.get('hits', 1)}"))
    for term, meta in rules.get("words", {}).items():
        if re.search(r"\b" + re.escape(term) + r"\b", low):
            hits.append(Hit("learned_word", term, 1.0,
                            f"learned s{meta.get('first_seen_session', '?')}"
                            f" x{meta.get('hits', 1)}"))

    for term in HEDGES:
        if term in low:
            hits.append(Hit("hedging", term, 1.0))
    for term in TRANSITIONS:
        if re.search(r"(^|[.;,]\s*)" + re.escape(term) + r"\b", low):
            hits.append(Hit("transition_density", term, 1.0))

    m = PARTICIPIAL_TAIL.search(sent)
    if m:
        hits.append(Hit("participial_tail", m.group(0).strip(), 1.0))
    m = NEG_PARALLEL.search(sent)
    if m:
        hits.append(Hit("negative_parallelism", m.group(0).strip(), 1.0))
    m = COPULA_DODGE.search(sent)
    if m:
        hits.append(Hit("copula_dodge", m.group(0), 1.0))
    m = RULE_OF_THREE.search(sent)
    if m:
        hits.append(Hit("rule_of_three", m.group(0), 1.0))
    m = FALSE_RANGE.search(sent)
    if m:
        hits.append(Hit("false_range", m.group(0), 1.0))
    m = CHATBOT.search(sent)
    if m:
        hits.append(Hit("chatbot_artifact", m.group(0), 1.0))
    m = CHALLENGES_TROPE.search(sent)
    if m:
        hits.append(Hit("challenges_trope", m.group(0), 1.0))
    m = GENERIC_CLOSER.search(sent)
    if m:
        hits.append(Hit("generic_closer", m.group(0), 1.0))

    n = len(EMDASH.findall(sent))
    if n:
        hits.append(Hit("em_dash", "—" * n, float(n)))
    n = len(CURLY.findall(sent))
    if n:
        hits.append(Hit("curly_quote", "curly quotes", float(n)))
    n = len(EMOJI.findall(sent))
    if n:
        hits.append(Hit("emoji", "emoji", float(n)))

    if len(w) > 34:
        hits.append(Hit("long_sentence", f"{len(w)} words", 1.0))

    return hits


def document_hits(text, rules=None):
    """Signals that only exist at document level: rhythm, structure, repetition.

    These are the ones perplexity-based detectors care about most, and the ones
    a phrase blacklist can never catch.
    """
    hits = []
    sents = sentences(text)
    lengths = [len(words(s)) for s in sents if words(s)]

    if len(lengths) >= 6:
        sd = statistics.pstdev(lengths)
        mean = statistics.mean(lengths)
        if sd < 8.0:
            hits.append(Hit("low_burstiness", f"sentence-length sd={sd:.1f}",
                            max(0.0, (8.0 - sd) / 8.0),
                            f"mean={mean:.1f} words"))
        band = [n for n in lengths if 14 <= n <= 26]
        share = len(band) / len(lengths)
        if share > 0.55:
            hits.append(Hit("mid_band_clustering",
                            f"{share:.0%} of sentences are 14-26 words",
                            share - 0.55))

    paras = body_paragraphs(text)
    if len(paras) >= 5:
        per = [len(sentences(p)) for p in paras]
        if per and statistics.pstdev(per) < 0.65:
            hits.append(Hit("uniform_paragraphs",
                            f"{statistics.mean(per):.1f} sentences per paragraph, sd="
                            f"{statistics.pstdev(per):.2f}", 1.0))

    openers = {}
    for s in sents:
        w = words(s)
        if not w:
            continue
        key = " ".join(x.lower() for x in w[:2])
        openers.setdefault(key, []).append(s)
    for key, group in openers.items():
        if len(group) >= 3:
            hits.append(Hit("repeated_openers", key, float(len(group) - 2),
                            f"{len(group)} sentences open with '{key}'"))

    if len(BOLD_HEADER_ITEM.findall(text)) >= 3:
        hits.append(Hit("bold_header_item",
                        "bulleted list of **Bold header:** items",
                        float(len(BOLD_HEADER_ITEM.findall(text)) - 2)))

    hits.extend(parallel_hits(sents))

    if len(sents) >= 12:
        n_contr = len(CONTRACTION.findall(strip_markdown(text)))
        rate = n_contr / max(1, len(sents))
        if rate < 0.18:
            hits.append(Hit("no_contractions",
                            f"{n_contr} contractions across {len(sents)} sentences",
                            0.18 - rate))

    return hits
