---
name: jf-internet-appendix
description: Use when deciding what belongs in the Internet Appendix vs. the main text of a The Journal of Finance (JF) manuscript. Allocates content and structures the appendix per JF's actual policy; it does not generate the results.
---

# Internet Appendix (jf-internet-appendix)

## When to trigger

- The main text is bloated with proofs, secondary robustness tables, or data-construction detail
- A referee will ask for more checks but the article is near the 60-page limit
- You are unsure how JF wants the Internet Appendix submitted and hosted
- The main result is buried on page 40 behind diagnostics

## JF's actual Internet Appendix policy

The "Internet Appendix" is a **JF convention** (JF helped popularize it). JF's specifics differ from generic "online appendices":

- **At submission, the Internet Appendix is placed at the END of the same PDF as the manuscript — NOT uploaded as a separate file.** Put the title **"Internet Appendix"** at the top of its first page so it is not mistaken for a regular appendix.
- The Internet Appendix **does not count toward JF's 60-page manuscript limit** (manuscript: ≤60 pp, ≥1.5 spacing, 12-pt font).
- The **paper must be self-contained**: a reader must understand the study in full **without** consulting the Internet Appendix.
- **On acceptance**, the appendix is published as the **Internet Appendix with the online article on the publisher's (Wiley) site**.
> Source: afajof.org/submissions and the JF Submission Guidelines (Rev. March 12, 2024), accessed 2026-05-30.

## What goes where

| Content                                                        | Main text | Internet Appendix |
|----------------------------------------------------------------|:---------:|:-----------------:|
| The question, design, headline result, economic magnitude      |     X     |                   |
| The 3–6 decisive robustness checks                             |     X     |                   |
| Full proofs / derivations of propositions                      |           |         X         |
| Secondary / exhaustive robustness tables                       |           |         X         |
| Detailed variable construction, data filters, sample steps     |   brief   |     full detail   |
| Alternative measures / extra subsamples / extra factor models  |           |         X         |
| Monte Carlo / simulation evidence                              |           |         X         |
| Additional figures, summary-stat breakdowns                    |           |         X         |

## Structuring the Internet Appendix

- Mirror the main-text section order; label tables `IA.I`, `IA.II`, … and figures `IA.1`, `IA.2`, ….
- Every appendix item must be **referenced from the main text** ("see Internet Appendix Table IA.IV") — orphan tables read as padding.
- Keep each appendix table self-contained, same note conventions as the main exhibits (`jf-tables-figures`).
- Note: replication **code** is handled separately under JF's Data and Code Sharing Policy (Supplementary Information at acceptance), not via the Internet Appendix — see `jf-submission`.

## Checklist

- [ ] Internet Appendix is at the END of the same PDF, titled "Internet Appendix"
- [ ] Main text is self-contained and ≤60 pages on its own
- [ ] All proofs/derivations are in the Internet Appendix, not interleaved in the body
- [ ] Every Internet Appendix item is cited from the main text
- [ ] IA numbering and note conventions match the main exhibits
- [ ] No genuinely new headline finding appears only in the appendix

## Anti-patterns

- Uploading the Internet Appendix as a separate file (JF wants it bundled in the same PDF at submission)
- Writing a body that cannot be understood without the appendix (JF requires self-containment)
- Treating the Internet Appendix as a junk drawer of uncited tables
- Padding the body past 60 pages and pushing core results into the appendix to dodge the limit

## Output format

```
【IA bundled at end of same PDF + titled?】yes / no
【Body self-contained and ≤60 pp?】yes / no
【Proofs relocated?】yes / no
【All IA items cited from body?】yes / no
【New result hidden in appendix?】yes / no
【Next step】jf-writing-style
```
