---
name: gastroenterology
description: Use when targeting Gastroenterology (AGA) or deciding whether a GI/hepatology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Gastroenterology (gastroenterology)

## Journal positioning

Gastroenterology is the flagship journal of the American Gastroenterological Association, published by Elsevier, and the leading venue for the full spectrum of gastrointestinal and liver science — from mechanistic cell and molecular biology through clinical trials, epidemiology, and endoscopy. Unlike Gut (which skews toward clinical GI/hepatology under a BMJ framework), Gastroenterology's AGA identity means the journal explicitly values and publishes high-quality basic and translational science alongside clinical trials, making it the natural home for mechanistic studies with clear disease relevance in the gut, liver, and pancreas. The readership spans GI clinicians, hepatologists, and GI scientists, requiring papers to be accessible across that spectrum.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AGA / Elsevier Gastroenterology platform.

## When to trigger

- The author names Gastroenterology or the AGA as the target venue for a GI or liver manuscript.
- A GI/hepatology paper needs venue selection between Gastroenterology and Gut.
- A mechanistic gut, liver, or pancreas study with translational human-data bridge needs framing guidance.
- The author needs Gastroenterology's desk-reject risks and credible alternative venues before submitting.

## Scope & topic fit

- Mechanistic studies of gut, liver, and pancreatic disease — inflammatory bowel disease, colorectal cancer, NAFLD/MASH, hepatitis, celiac disease, gastrointestinal motility — from cellular/molecular to in vivo model levels with human translational data.
- Randomized clinical trials in GI disease (IBD, liver cirrhosis, GI cancers, functional bowel disorders) that meet AGA practice-change or guideline-informing significance.
- Gut microbiome and host-microbiome interaction studies with mechanistic or clinical depth beyond descriptive microbial profiling.
- GI epidemiology and population-based studies establishing disease burden, risk factors, or prevention evidence at a scale that matters for AGA clinical practice.
- Endoscopy and GI procedural advances where diagnostic yield, safety, or clinical management is rigorously validated.
- Clinical guidelines, technical reviews, and systematic reviews commissioned or endorsed by the AGA (primarily invited or concept-approved).

## Method & evidence bar

- Mechanistic studies must include human tissue, clinical samples, or genetic evidence corroborating the in vitro or animal findings; a murine model alone without human validation will not meet the bar.
- RCTs must be prospectively registered, CONSORT-compliant, and powered for a clinically meaningful primary endpoint with AGA/clinical-practice relevance.
- Microbiome studies must use pre-specified analytical approaches, appropriate controls, and integrate functional validation beyond 16S or metagenomic profiling alone; compositional analysis standards are expected.
- Observational epidemiology studies must employ validated exposure and outcome definitions, appropriate confounding control, and pre-specified analysis plans.
- Prediction models and scoring systems require TRIPOD-compliant reporting with external validation in an independent cohort.
- ARRIVE checklist for animal experiments; data and code availability statements required; pre-registration of observational studies encouraged.

## Structure & house style

- Structured abstract for clinical research; unstructured abstract may be acceptable for basic/mechanistic papers — re-check current format requirements.
- The introduction should frame the key mechanistic question or clinical gap, citing the current state of AGA clinical understanding; make explicit what the result changes for either disease understanding or clinical practice.
- Lay summary or translation-to-clinical-practice paragraph is valued and in some article types required; the AGA readership spans basic scientists and gastroenterologists.
- Figures should be self-explanatory; mechanistic papers typically carry detailed methods in supplementary materials but must retain the core experimental logic in the main text.
- Research Article vs. Brief Report vs. Letter distinctions carry different length norms — confirm current limits; Clinical Research articles follow the structured format for trials.
- Reporting guideline checklists must be uploaded with submission.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Gastroenterology author instructions" on the Elsevier/AGA platform and follow the current version.
- Re-check article-type classification (Research Article, Brief Report, Clinical Research, Review, Letter) and confirm length/figure limits.
- Confirm trial or study pre-registration and upload ethics/IRB/consent documentation; confirm IACUC documentation for animal studies.
- Complete and upload the applicable reporting guideline checklist (CONSORT, STROBE, PRISMA, TRIPOD, ARRIVE, or equivalent).
- Verify AGA conflict-of-interest policy compliance and funding disclosure for all authors.
- Confirm data and code availability statement, open-access/APC options, and current AI-use disclosure policy.
- Re-check microbiome data deposition requirements (NCBI SRA or equivalent) if applicable.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this paper advances GI disease understanding or AGA clinical practice in a way that matters to both clinicians and scientists.
- [ ] The contribution is framed as a mechanism discovery, definitive clinical evidence, or validated tool — not as an uncontrolled case series or descriptive survey.
- [ ] Human validation data is explicitly included for any mechanistic study; the bridge from model to human is stated clearly in Results, not only in Discussion.
- [ ] The applicable reporting guideline checklist is complete and registration/ethics documents are ready for upload.
- [ ] Microbiome or multi-omics data are deposited in a public repository and the accession number is included in the manuscript.
- [ ] Article type matches scope and length: a mechanistic advance belongs in Research Article, not a Letter.

## Common desk-reject triggers

- Basic-science or animal studies with no human translational evidence (tissue, genetic, biomarker) corroborating the primary finding.
- Descriptive microbiome surveys (16S compositional data alone) without mechanistic or functional follow-through.
- Small underpowered single-center clinical trials or retrospective case series without pre-specified hypotheses.
- Epidemiologic studies with inadequate confounding control or absent pre-specified analysis plans presented as providing causal evidence.
- Papers primarily of interest to surgeons or interventional endoscopists without broader GI-science framing — may fit better in a subspecialty GI or endoscopy journal.

## Re-routing decision

- A clinical GI/hepatology trial or cohort study with strong UK/European BMJ clinical framing and hepatology depth → `gut` (BMJ; clinical GI/hepatology focus, mechanism welcome but not required).
- A GI cancer biology study with strong translational/oncology framing → `cancer-discovery` (AACR) or `journal-of-clinical-investigation`.
- A gut microbiome mechanistic study at the host-pathogen or microbial-ecology interface → `cell-host-and-microbe`.
- A large-scale GI prevention RCT or global-burden epidemiology study → `nejm`, `the-lancet`, or `jama` if the significance is truly practice-changing at that level.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Gastroenterology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the human-validation bridge / reporting guideline / AGA clinical relevance clear the Gastroenterology bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / abstract format / CONSORT or equivalent / trial registration / IACUC / data deposition / AGA COI>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
