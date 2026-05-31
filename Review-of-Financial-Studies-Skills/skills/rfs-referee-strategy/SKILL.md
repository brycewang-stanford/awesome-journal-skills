---
name: rfs-referee-strategy
description: Use when choosing suggested/opposed referees or running an objection pre-mortem before submitting a The Review of Financial Studies (RFS) manuscript. Anticipates reviewer concerns; does NOT write the rebuttal (that is rfs-rebuttal).
---

# Referee Strategy & Objection Pre-Mortem (rfs-referee-strategy)

## When to trigger

- The portal asks for suggested and opposed reviewers
- You want to anticipate the objections RFS referees will raise before they do
- A coauthor asks "who will referee this and what will they hate?"
- Preparing the cover letter's referee section

## Two jobs: referee selection and objection pre-mortem

### A. Suggesting and opposing referees
- **Suggest** referees who are active in your exact sub-field, have published the closest methods, and can evaluate both the novelty and the rigor. RFS referees are usually the authors you cite most.
- Aim for a balanced slate: not only your closest collaborators' circle, and not only theorists for an empirical paper (or vice versa).
- **Oppose** referees only with a brief, professional reason (active competing project, prior dispute, direct conflict). Do not over-exclude — editors notice and discount long oppose lists.
- Never suggest coauthors, advisors/advisees, or same-institution colleagues — these are conflicts the editor will strike.
- **Do not suggest a current RFS editor as a referee.** Know who handles your area (e.g., Viral Acharya, Xavier Giroud, Andrey Malenko, Anna Pavlova, Clemens Sialm, David Sraer, Jessica Wachter, under Executive Editor Tarun Ramadorai) — your suggested referees should complement, not duplicate, the editor pool.
- The editor chooses; your list is advisory. Make it easy for them to find qualified, fair referees.

### B. Objection pre-mortem (the high-value step)
Anticipate the specific objections an RFS referee will raise and address them *before* submission. Common RFS referee challenges:

| Objection                                  | Pre-empt by                                                |
|--------------------------------------------|------------------------------------------------------------|
| "This is incremental / not novel enough"   | A crisp delta in the intro (`rfs-literature-positioning`)  |
| "Endogeneity is not resolved"              | A clean shock + diagnostics (`rfs-identification`)         |
| "Results are fragile"                       | A full robustness battery (`rfs-robustness`)               |
| "You data-mined this predictor"            | Multiple-testing adjustment + OOS test                     |
| "Standard errors are wrong"                | Clustering/adjustment matched to the data                  |
| "The mechanism is asserted, not shown"     | Direct mechanism evidence / heterogeneity                  |
| "Missing a key recent paper"               | Cite and distinguish it (the close competitor)             |
| "Theory and empirics are disconnected"     | Integrate the model's prediction with the test             |

For each likely objection: write the one-paragraph answer now, and make sure the paper (or IA) already contains the evidence that answer points to.

### Reading the desk-reject vs. send-out signal
An RFS Editor desk-screens before referees ever see the paper. Concrete triggers that draw a desk reject:
- **Perceived novelty shortfall** — the single most common RFS desk reject. A clean re-run of a known design on new data reads as a field-journal paper. Make the contribution unmissable in the abstract and first two pages.
- **A visible identification threat** the editor can see immediately. Surface your source of variation early so the editor does not assume it is absent.
- **Scope mismatch** — out of the journal's financial-economics remit, or better suited to a sibling SFS journal (Review of Asset Pricing Studies, Review of Corporate Finance Studies).
- **Concurrent submission elsewhere** — RFS prohibits it (the *permitted* exception is the RFS–SFS Cavalcade dual submission, which is not a violation).
- **No plan to release code** — RFS requires public code release as a condition of publication; signal compliance early.
- If two strong sub-fields could referee the paper (e.g., asset pricing and intermediation), suggest at least one from each so the editor can triangulate.
- If results are not yet in hand but the design is strong, the **Registered Reports** (Stage 1) route can pre-empt a "results-driven" desk reject entirely.

### Cover-letter referee note
- Keep it to a few sentences: name suggested referees and a one-clause reason each; name opposed referees with a brief professional reason; confirm no concurrent submission elsewhere (note an RFS–SFS Cavalcade dual submission if applicable — that route is permitted).

## Checklist

- [ ] Suggested referees are sub-field experts who can judge novelty AND rigor
- [ ] No conflicted names suggested (coauthors, advisors, same institution)
- [ ] No current RFS editor suggested as a referee
- [ ] Opposed list is short and professionally justified
- [ ] Top 5–8 likely objections written out with a planned response
- [ ] Each anticipated objection has supporting evidence already in the paper/IA
- [ ] The "not novel enough" risk is specifically pre-empted in the intro

## Anti-patterns

- A long opposed-referee list — signals defensiveness; editors discount it.
- Suggesting only friendly or conflicted referees.
- Ignoring the "incremental" objection because the empirics are clean.
- Discovering a fatal objection only after the reports arrive.
- Suggesting referees who cannot evaluate the method (e.g., pure theorists for a microstructure paper).

## Output format

```
【Suggested referees】[names + why each: sub-field + method fit]
【Opposed】[short, justified]
【Top objections】[objection → planned response → where evidence lives]
【Novelty defense】one-paragraph pre-empt for the "incremental" risk
【Next step】rfs-submission (finalize) → await decision → rfs-rebuttal
```
