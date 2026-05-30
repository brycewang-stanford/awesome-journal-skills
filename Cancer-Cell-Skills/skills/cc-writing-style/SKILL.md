---
name: cc-writing-style
description: Use when polishing prose for a Cancer Cell (Cell Press) manuscript — the Summary/Introduction/Results/Discussion craft, claim calibration, and Cell Press nomenclature/house style. It edits language and framing; it does not design experiments or build figures.
---

# Writing Style & Claim Calibration (cc-writing-style)

## When to trigger

- The Results read like a lab notebook rather than a mechanistic narrative
- The Discussion overstates therapeutic / clinical impact
- Claims outrun the evidence (single-system conclusions stated broadly)
- Nomenclature, tense, or section structure are inconsistent with Cell Press

## Cell Press article structure (narrative roles)

| Section | Role |
|---------|------|
| Summary | One-paragraph mechanistic arc (see `cc-structured-abstract`) |
| Introduction | Concise; the gap and the hypothesis, not a textbook review |
| Results | The mechanistic story, figure by figure, each claim tied to data |
| Discussion | Interpretation, limitations, and **calibrated** translational implications |
| STAR Methods | Structured methods + Key Resources Table (see `cc-reporting-standards`) |

## Results: write the mechanism as a story

- Open each Results subsection with the **question/claim**, then the evidence, then the conclusion.
- Each paragraph maps to a figure/panel; every assertion cites a panel.
- Foreground **causality and orthogonal validation** ("loss of X reduced Y in cells and in PDX tumors") over a list of assays.
- Use past tense for what was done/found; present tense for established facts.

## Claim calibration (the signature Cancer Cell discipline)

Match verb strength to evidence strength:

| Evidence | Acceptable verb |
|----------|-----------------|
| Correlation in human data | "associated with," "correlates with" |
| Perturbation in cells | "promotes," "is required for" (in this system) |
| In vivo perturbation | "drives," "is necessary in vivo" |
| In vivo efficacy + human data | "represents a therapeutic vulnerability" |

- Do not call a target "therapeutic" without in vivo efficacy and/or human evidence.
- Distinguish "necessary" from "sufficient"; do not conflate the two.
- State limitations explicitly (model caveats, single-cohort findings) — reviewers reward candor.
- Avoid "novel," "first," "unprecedented," "proves"; let the data carry the weight.

## Nomenclature & house style

- Use approved gene/protein nomenclature (HGNC for human, MGI for mouse); italicize genes, roman for proteins; correct species capitalization (human BRCA1 vs mouse Brca1).
- Define each abbreviation once; keep terminology consistent across text, figures, and front matter.
- Cite using the Cell Press reference style (verify current format); reference key prior work fairly.
- Active voice and direct sentences; avoid hedging chains ("might possibly suggest").

## Checklist

- [ ] Introduction is concise and ends on a clear hypothesis/gap
- [ ] Each Results paragraph maps to a figure and states claim → evidence → conclusion
- [ ] Causality and orthogonal validation are foregrounded
- [ ] Verbs match evidence level; no therapeutic claim without in vivo/human support
- [ ] "Necessary" vs "sufficient" used correctly
- [ ] Discussion states limitations and calibrated implications
- [ ] Gene/protein nomenclature and species formatting correct and consistent
- [ ] Hype words removed; tense usage consistent

## Anti-patterns

- Results as an assay catalog with no narrative thread
- Overstated translational/therapeutic claims beyond the data
- Conclusions generalized from a single system
- "Novel/first/unprecedented/proves" sprinkled throughout
- Inconsistent gene nomenclature or species capitalization
- A Discussion with no limitations paragraph

## Output format

```
【Results narrative】claim→evidence→conclusion per subsection? Y/N
【Claim calibration】overstated verbs flagged: [...]
【Therapeutic claims】backed by in vivo/human? Y/N
【Limitations】present in Discussion? Y/N
【Nomenclature】gene/protein/species correct & consistent? Y/N
【Hype words】removed? Y/N
【Next step】cc-cover-letter or cc-submission
```
