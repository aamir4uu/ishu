#!/usr/bin/env bash
# Smoke test for the humanizer-evolve pipeline.
#
# Runs against a synthetic fixture in an isolated copy of memory/, so the real
# calibration is never touched. Exercises: scanning, span matching, weight
# recalibration, rule mining, and the state/log writes.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL="$(dirname "$HERE")"
SANDBOX="$(mktemp -d)"
trap 'rm -rf "$SANDBOX"' EXIT

cp -r "$SKILL/scripts" "$SANDBOX/scripts"
cp -r "$SKILL/references" "$SANDBOX/references" 2>/dev/null || true
cp -r "$SKILL/tests" "$SANDBOX/tests"
mkdir -p "$SANDBOX/memory"
echo '{"phrases": {}, "words": {}, "structures": {}}' > "$SANDBOX/memory/learned_rules.json"
# Copy the real topic-term guard so the test exercises it.
cp "$SKILL/memory/never_promote.txt" "$SANDBOX/memory/never_promote.txt"

cd "$SANDBOX"

echo "== 1. scan a deliberately AI-sounding fixture =="
python3 scripts/scan.py tests/fixture_draft.md --top 5
SCORE=$(python3 scripts/scan.py tests/fixture_draft.md --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["score"])')
echo "$SCORE" > /tmp/hz_score_before
python3 - "$SCORE" <<'PY'
import sys
score = float(sys.argv[1])
# The fixture is deliberate slop. It must land in "at risk" or worse (>=35),
# never in either "clean" band, or the scanner is not doing its job.
assert score >= 35, f"slop fixture should score >=35, got {score}"
print(f"   ok: fixture scores {score}/100 (at risk or worse)")
PY

echo
echo "== 2. ingest the fixture report and evolve =="
# --min-corpus 4 so the tiny fixture reaches the mining path. Real runs use the
# default of 8, which holds promotion back until there is enough evidence.
python3 scripts/learn.py tests/fixture_report.md --min-corpus 4

echo
echo "== 3. assert the model actually changed =="
python3 - <<'PY'
import json, os
rules = json.load(open("memory/learned_rules.json"))
state = json.load(open("memory/state.json"))
n = len(rules["phrases"]) + len(rules["words"])
assert n > 0, "expected at least one rule mined from the flagged corpus"
mined = set(rules["phrases"]) | set(rules["words"])
assert "remote work" not in mined, (
    "topic-term guard failed: 'remote work' is in never_promote.txt but was "
    "still promoted")
assert not any("remote" in g for g in mined), f"guard leaked: {mined}"
assert state["reports_ingested"] == 1, state["reports_ingested"]
assert state["sessions"] == 1, state["sessions"]
assert state["skill_version"] != "1.0.0", "version should have bumped"
assert state["history"], "history should record the session"
assert os.path.exists("memory/zerogpt-log.md"), "session log missing"
assert os.path.exists("memory/flagged.jsonl"), "flagged corpus missing"
print(f"   ok: {n} rules mined, topic-term guard held, "
      f"version now {state['skill_version']}")
print(f"   mined: {sorted(mined)}")
PY

echo
echo "== 4. recall must have improved, and mined rules must load =="
python3 - <<'PY'
import json, subprocess
out = subprocess.run(["python3", "scripts/scan.py", "tests/fixture_draft.md",
                      "--json"], capture_output=True, text=True, check=True)
res = json.loads(out.stdout)
learned = res["learned_rules"]["phrases"] + res["learned_rules"]["words"]
assert learned > 0, "scanner is not reading the learned rules"
state = json.load(open("memory/state.json"))
recall = state["history"][-1]["recall"]
before = float(open("/tmp/hz_score_before").read())
# The real "did it learn" assertion: after ingesting the report, the same text
# must score higher than it did before, because the weights moved and rules
# were mined from what the detector actually flagged.
assert res["score"] > before, (
    f"score did not rise after learning: {before} -> {res['score']}")
print(f"   ok: scanner loads {learned} learned rules, recall {recall}, "
      f"score {before} -> {res['score']}")
PY

echo
echo
echo "== 5. the template report format must parse too =="
python3 - <<'PY'
import sys
sys.path.insert(0, "scripts")
import learn
meta, spans = learn.parse_report("tests/fixture_report_template.md")
assert meta.get("draft") == "tests/fixture_draft.md", meta
assert meta.get("score") == "97", meta
assert len(spans) >= 3, spans
print(f"   ok: template format parsed, score {meta['score']}, {len(spans)} spans")
PY

echo
echo "== 6. cross-sentence parallelism must still be detected =="
python3 - <<'PY'
import sys
sys.path.insert(0, "scripts")
import detectors as D

# Verbatim from the 2026-08-21 ZeroGPT report, rows 9-11: three list items on
# one template, all three highlighted while the numerals between them came back
# clean. This is the regression guard for the signal that report produced.
triad = """1. **Hooks and single tips:** 7 to 15 seconds, with no setup.
2. **Product demos and how-tos:** 30 to 60 seconds, enough for a real workflow.
3. **Explainers and interviews:** 60 to 180 seconds, worth it only when your audience already knows you.
"""
hits = [h for h in D.parallel_hits(D.sentences(triad))
        if h.signal == "parallel_structure"]
assert hits, "parallel_structure no longer fires on the flagged triad"

# Rows 12-13: two sentences three paragraphs apart sharing an opening template
# that differs only in its numbers. repeated_openers cannot see this.
pair = """A 45-second Reel stretched to 90 doesn't gain you 45 seconds of attention.

Something entirely different goes here to separate them properly.

A 25-second Reel that most viewers watch to the end sends a far stronger signal.
"""
opens = [h for h in D.parallel_hits(D.sentences(pair))
         if h.signal == "parallel_opening"]
assert opens, "parallel_opening no longer fires on the flagged pair"

# And it must not fire on two unrelated sentences that merely share a shape.
noise = """Our free social media resources include planning templates.

Whether anyone watches it is a different question.
"""
assert not D.parallel_hits(D.sentences(noise)), "parallelism over-fires on noise"
print("   ok: triad and pair both detected, noise rejected")
PY

echo
echo "ALL TESTS PASSED"
