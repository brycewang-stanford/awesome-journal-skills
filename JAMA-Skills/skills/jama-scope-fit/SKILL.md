---
name: jama-scope-fit
description: Use when judging whether a clinical study clears JAMA's general-medical-importance bar before investing in a full submission. Assesses fit and article-type match; it does NOT design the study or write the paper.
---

# Scope & Importance Fit (jama-scope-fit)

## When to trigger

- Before committing weeks to formatting a manuscript for JAMA
- The finding feels solid but you suspect it is too narrow / subspecialty
- Choosing between JAMA, a JAMA Network specialty journal, and a field journal
- An editor or mentor asked "is this really a general-medicine paper?"

## The general-medical-importance test

JAMA serves a broad clinician readership across all of medicine. Ask, in order:

1. **Does it change what a practicing clinician thinks or does?** A result that only matters to a single subspecialty lab rarely fits; a result that informs everyday diagnosis, treatment, or prevention does.
2. **Is the question clinically important, not just statistically novel?** Mechanistic novelty alone is off-fit; patient-relevant outcomes (mortality, function, major morbidity, validated patient-reported outcomes) are on-fit.
3. **Is the evidence near the top of the design hierarchy for the question?** RCTs, large well-controlled cohorts, rigorous diagnostic-accuracy studies, and systematic reviews/meta-analyses are the core. Underpowered pilots and uncontrolled case series are off-fit.
4. **Is it timely and generalizable?** Single-center convenience samples that do not generalize weaken fit.

If you cannot answer (1) and (2) affirmatively, JAMA is probably the wrong home — say so plainly.

## Article-type match (verify current types on the journal site)

| Your study                                       | Likely JAMA article type            |
|--------------------------------------------------|-------------------------------------|
| Randomized clinical trial                        | Original Investigation (with CONSORT)|
| Prospective/retrospective cohort, case-control   | Original Investigation (with STROBE) |
| Diagnostic-accuracy study                        | Original Investigation (with STARD)  |
| Systematic review ± meta-analysis                | Review / Original Investigation (PRISMA) |
| Health-policy analysis with clinical bearing     | Special Communication / Viewpoint    |
| Short, focused dataset                            | Research Letter                      |
| Synthesis without systematic methods              | Off-fit as Original Investigation    |

Match the article type to JAMA's current categories and word/format limits — verify on the official Instructions for Authors page (do not assume fixed numbers).

## Checklist

- [ ] The clinical question matters to a broad clinician audience, not one niche
- [ ] Primary outcome is patient-relevant, not a surrogate of unclear value
- [ ] Study design is high on the evidence hierarchy for this question
- [ ] Sample/setting support generalizable conclusions
- [ ] A correct JAMA article type exists for this work
- [ ] If narrow, a JAMA Network specialty journal or field journal is considered as plan B
- [ ] Importance can be stated in one sentence a non-specialist clinician understands

## Anti-patterns

- Pitching a single-center, hypothesis-generating pilot as a definitive Original Investigation
- Leading with mechanistic/molecular novelty rather than clinical consequence
- Surrogate-only endpoints presented as practice-changing
- Assuming high statistical significance equals general medical importance
- Ignoring that a better-fit JAMA Network specialty journal exists

## Output format

```
【Importance verdict】strong fit / borderline / off-fit
【One-sentence clinical importance】...
【Primary outcome patient-relevant?】yes / no
【Evidence level for the question】RCT / cohort / diagnostic / review / weaker
【Proposed JAMA article type】...
【Plan B journal if borderline】...
【Next skill】jama-study-design (if fit) / reconsider venue (if off-fit)
```
