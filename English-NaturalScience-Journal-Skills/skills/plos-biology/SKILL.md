---
name: plos-biology
description: Use when targeting PLOS Biology (PLOS Biol) or deciding whether a general biology manuscript fits this open-access venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, transparency culture, official-submission re-check, and desk-reject heuristics.
---

# PLOS Biology (plos-biology)

## Journal positioning

PLOS Biology is the flagship journal of the Public Library of Science (PLOS) and one of the most prominent fully open-access journals in general biology. It publishes significant, rigorous advances across the biological sciences — from cell and molecular biology to ecology, evolution, neuroscience, and systems biology — judged on scientific rigor and completeness, with a strong editorial culture around data sharing, reporting transparency, and methods reproducibility. The readership is the broad biological research community, and the journal's open-access mandate means papers are accessible worldwide without institutional subscription. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on journals.plos.org/plosbiology.

## When to trigger

- The author names PLOS Biology or PLOS Biol as the target venue.
- A manuscript has clear biological significance but benefits from an open-access outlet with strong transparency and data-sharing norms.
- A manuscript spans multiple biological disciplines or uses computational/quantitative methods alongside experimental data.
- The author needs PLOS Biology's desk-reject risks, reporting-guideline expectations, and a credible routing alternative.

## Scope & topic fit

- Cell and molecular biology, genetics, genomics, and systems biology with clear mechanistic or conceptual insight.
- Evolutionary biology, ecology, and organismal biology — PLOS Biology publishes both fundamental and quantitative ecological work.
- Neuroscience and computational neuroscience at the level of significant biological insight.
- Methods and resources are published when the new tool, dataset, or approach offers clear and broadly applicable biological utility.
- Interdisciplinary work bridging quantitative/computational approaches with experimental biology is well-suited.
- Community-page and primer articles (invited or commissioned) complement research articles — these are not the route for unsolicited reviews.

## Method & evidence bar

- Significance bar is high: a paper must represent a substantial advance in understanding, not merely an incremental addition to an existing paradigm.
- Data availability is non-negotiable: underlying data for all figures must be deposited in a public repository or provided as supporting files; PLOS enforces this at acceptance.
- Reporting guidelines must be applied: ARRIVE for animal studies, CONSORT for trials, STROBE for observational studies, MIQE for qPCR — a checklist submission is expected.
- Statistical reporting: PLOS Biology actively recommends against sole reliance on p < 0.05 thresholds; effect sizes, confidence intervals, and sample-size justifications are expected.
- Code and computational pipelines must be made publicly available; scripts and analysis code deposited in Zenodo, GitHub, or equivalent.

## Structure & house style

- Research articles use a standard IMRAD structure with an unstructured abstract; a separate Author Summary (plain-language summary; re-check the current length limit) is required — this is PLOS Biology-specific and distinct from the abstract.
- The Author Summary must be written for a scientifically literate non-specialist audience; it is published prominently alongside the article.
- Figure panels must be accompanied by underlying data ("source data files") for all quantitative displays.
- Supporting information (supplemental figures, tables, methods) is hosted alongside the paper under the same open-access license.
- PLOS Biology uses a transparent editing process where editors' decisions and reviewers' identities (if they consent) can be published.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "PLOS Biology submission guidelines" and follow the current version at journals.plos.org/plosbiology.
- Re-check required reporting checklists (ARRIVE, CONSORT, STROBE, or equivalent) and confirm all applicable guidelines have been completed and attached.
- Confirm data availability statement and deposition: all primary data underlying figures must be accessible; deposition in an approved repository (Zenodo, Dryad, GEO, SRA, etc.) is expected.
- Re-check code availability: all analysis scripts, pipelines, and software must be publicly available with an appropriate open-source license.
- Verify Author Summary requirements and format; confirm article processing charge (APC) or fee-waiver eligibility under current PLOS policy.
- Check competing-interests, funding acknowledgment, AI-use disclosure, and preprint posting policy (PLOS actively supports preprints).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence articulating why this paper advances biological understanding for the broad PLOS Biology readership, not only for specialists in one subfield.
- [ ] The Author Summary is drafted (plain language; re-check the current length limit) for a non-specialist audience.
- [ ] All primary data are deposited or ready for deposition; source data files are prepared for each quantitative figure.
- [ ] Applicable reporting guidelines (ARRIVE, CONSORT, etc.) have been completed and the checklist is ready to attach.
- [ ] Code and computational workflows are in a public repository with documentation sufficient for reproduction.

## Common desk-reject triggers

- Insufficient significance: incremental advances that refine an established finding without conceptual or mechanistic novelty.
- Missing or incomplete data availability — PLOS Biology editorial staff check for deposited data or source files at submission; absence is a desk-reject risk.
- Reporting checklist absent or incomplete for animal/human/clinical studies.
- Manuscripts framed as clinical research without appropriate reporting compliance (CONSORT, trial registration).
- Reviews or opinion pieces submitted as unsolicited manuscripts — PLOS Biology does not publish unsolicited narrative reviews.

## Re-routing decision

- Flagship-level conceptual advance → `nature`, `science`, `cell`, or `pnas`.
- Prefer eLife's Reviewed-Preprint model and public reviews → `elife`.
- Genomics and computational biology are the primary focus → `genome-biology`.
- Clinical/translational emphasis → `plos-medicine` or `nature-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] PLOS Biology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the advance and evidence clear PLOS Biology's significance and transparency bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <reporting checklist / data deposition / code availability / Author Summary / APC / ethics>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
