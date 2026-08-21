# ZeroGPT Report: humanizer test fixture

- Date scored: 2026-01-01
- File scored: tests/fixture_draft.md
- Word count: 160
- ZeroGPT result: 97% AI / 3% human
- Detector version or URL: fixture, not a real run
- Pre-flight run before scoring: `python3 scripts/zerogpt_preflight.py tests/fixture_draft.md --verbose`
- Gates failing at time of scoring: 6

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| 1 | In today's digital age, remote work stands as a testament to the transformative power of technology. | copula avoidance, significance inflation | yes |
| 2 | This comprehensive guide will delve into the intricacies of distributed teams, highlighting the pivotal role that asynchronous communication plays in modern organisations. | AI vocabulary, participial tail | yes |
| 3 | Companies that leverage robust collaboration tools are seeing improved outcomes, fostering a culture of trust and enhancing employee satisfaction across the board. | AI vocabulary, participial tail | yes |
| 4 | Despite these challenges, the future looks bright. | challenges trope, generic closer | NEW |

## Findings

Used by `tests/run_tests.sh` to prove the template report format parses.

## Actions taken

- [x] Nothing. This is a fixture, never ingested into real memory.
