# Recorded exceptions

Cases where a client instruction overrides the generic catalogue. The client
brief always wins; the exception is recorded here so nobody "fixes" it later
and so the scanner's output can be read correctly.

| # | Signal / rule | Client | Override | Reason |
| --- | --- | --- | --- | --- |
| 1 | Title case in headings (generic catalogue treats it as an AI tell) | SocialBee | Use APA title case for H1 and all subheadings | Explicit item in the AEO/SEO checklist: "capitalize the title and subheadings properly - APA" |
| 2 | `rule_of_three` on Key Takeaways boxes | SocialBee | Allowed | Checklist mandates a 4-5 bullet takeaways box; parallel bullets are the format, not a tell |
| 3 | `no_contractions` threshold | SocialBee | Enforce strictly | Brand voice explicitly requires contractions throughout (you're, it's, don't) |
| 4 | Expressions of importance ("is crucial", "is vital", "is essential") | SocialBee | Hard cap of two per article, prefer zero | Brand doc lists these as a Don't, stricter than the generic catalogue |

## Added after the second ZeroGPT report, 2026-08-21

| # | Signal / rule | Client | Override | Reason |
| --- | --- | --- | --- | --- |
| 5 | Learned phrase `short answer` | SocialBee | Label removed, answer kept | Both filed reports flagged the opening block including the bolded "Short answer:" label, so the learner promoted the phrase. The AEO checklist requires a 40-60 word direct answer at the top; it does not require the label. Answer stays, label goes. |
| 6 | `stat_dense` on cited statistics | SocialBee | Never resolve by cutting the fact | The checklist asks for a specific citable data point and E-E-A-T asks for sourced claims. `stat_dense` fires on exactly that. Fix the delivery, splitting the source from the figures, never the substance. |
| 7 | `table_row_markers` and flattened tables | SocialBee | Accepted residual | Detectors read table cells as prose, confirmed in both reports. Tables are inherently parallel and uniform, which is their job. Rewriting a table to look less table-like damages it for the reader. |
| 8 | `intro_position` | — | Informational, always fires | It marks the opening for extra scrutiny rather than reporting a defect. Treat a hit as "rewrite this by hand, last", not as something to eliminate. |
