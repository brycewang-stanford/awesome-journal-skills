---
name: gut
description: Use when targeting Gut (BMJ) or deciding whether a GI/hepatology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Gut (gut)

## Journal positioning

Gut is published by BMJ and is the official journal of the British Society of Gastroenterology, with a scope that covers clinical gastroenterology, hepatology, and pancreatology alongside translational and mechanistic science. Compared with Gastroenterology (AGA), Gut carries a stronger clinical and epidemiological identity shaped by the BMJ culture of rigorous evidence-based medicine, open-data ethos, and methodological transparency — while also welcoming mechanistic studies that are closely tethered to clinically relevant disease processes. Hepatology occupies a larger share of Gut's pages than in most GI journals, reflecting the journal's BSG heritage and a strong liver disease community. The readership is international: European and global gastroenterologists, hepatologists, and GI researchers.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the BMJ / Gut author platform.

## When to trigger

- The author names Gut or the BSG as the target venue for a GI or hepatology manuscript.
- A GI/hepatology paper needs venue selection between Gut and Gastroenterology.
- A hepatology or clinical IBD paper with European epidemiology or registry data needs framing guidance.
- The author needs Gut's desk-reject risks and alternative venues before submitting.

## Scope & topic fit

- Clinical and epidemiological studies in inflammatory bowel disease (Crohn's, ulcerative colitis), liver disease (NAFLD/MASH, hepatitis, cholestatic disease, cirrhosis complications), pancreatic disease, and GI cancer.
- Translational and mechanistic hepatology: liver fibrosis mechanisms, steatohepatitis pathogenesis, hepatocellular carcinoma biology — with human liver tissue, biopsy, or clinical cohort evidence as a primary layer.
- Gut microbiome studies with strong functional validation or direct clinical correlation (not purely descriptive composition); microbiota-drug, microbiota-host immunity, and microbiota-liver axis research.
- Clinical trials in GI medicine and hepatology (IBD therapies, antifibrotic strategies, liver cancer interventions) where the evidence has the potential to inform BSG or European clinical practice.
- GI cancer epidemiology, screening, and prevention at population scale; colorectal cancer, gastric cancer, and hepatocellular carcinoma risk-factor research.
- Endoscopy innovation where clinical performance is rigorously validated in prospective or randomized designs.

## Method & evidence bar

- Clinical and epidemiological studies must use validated exposure and outcome definitions, pre-specified analysis plans, and rigorous confounding control aligned with BMJ standards; retrospective audits without hypothesis framing are insufficient.
- Mechanistic and translational papers must include human tissue, clinical samples, or patient-level data as a central evidentiary layer — not merely supportive; pure animal-only or cell-only studies without human corroboration will not clear the bar.
- RCTs must be prospectively registered, CONSORT-compliant, and powered for a pre-specified primary endpoint; Gut follows the BMJ group's trial reporting expectations.
- Microbiome studies require pre-specified analytical pipelines, appropriate controls, functional validation (germ-free colonization, metabolomics, in vitro mechanistic assays), and data deposition in public repositories.
- Reporting guideline checklists (CONSORT, STROBE, PRISMA, TRIPOD, ARRIVE) are required at submission; BMJ group journals check compliance rigorously.
- Open-data ethos: data availability statements are required; Gut strongly encourages open-access data sharing in line with BMJ policy.

## Structure & house style

- Structured abstract for clinical research (Objective / Design / Results / Conclusions); unstructured "Summary" for basic/translational papers — confirm current format.
- The introduction should frame the clinical or mechanistic gap relative to current clinical practice or guidelines; purely academic novelty framing without clinical relevance context is insufficient.
- Significance statement or "Significance of this study" box (What is already known / What are the new findings / How might this affect clinical practice) is a Gut-specific requirement for most article types — this must be filled with genuinely specific, non-generic content.
- Figures must be publication-quality; pathology, histology, and liver imaging figures should include scale bars and appropriate controls.
- Letters to the Editor and Brief Communications have strict length limits; re-check current specifications.
- BMJ Open Access options and hybrid licensing are available — re-check current APC and CC licensing details on the BMJ platform.

## Official-submission checklist

- Search the live site for "Gut author instructions" on the BMJ Journals / Gut platform and follow the current version.
- Re-check article-type classification (Original Article, Research Letter, Review, Editorial) and confirm current length and figure limits.
- Confirm trial or study pre-registration (ISRCTN, ClinicalTrials.gov, or equivalent); upload ethics/IRB and consent documentation per BMJ policy.
- Complete and upload the applicable reporting guideline checklist (CONSORT, STROBE, PRISMA, TRIPOD, ARRIVE, or equivalent).
- Verify BMJ conflict-of-interest and funding disclosure requirements; confirm data-sharing statement is complete and explicit.
- Re-check microbiome or omics data deposition requirements (NCBI SRA, Zenodo, or equivalent) and accession number inclusion.
- Check "Significance of this study" box format specifications and completeness requirements.
- Confirm current AI-use disclosure policy and open-access/APC options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this finding changes clinical understanding or practice in GI/hepatology in a way that matters to international clinicians.
- [ ] The "Significance of this study" box answers all three sub-questions with specific, not generic, content about this paper's contribution.
- [ ] Human tissue, clinical cohort, or patient-level data is a central evidentiary layer, not only a supplementary validation.
- [ ] The applicable reporting guideline checklist is complete; BMJ conflict-of-interest forms are ready for all authors.
- [ ] Data availability statement is explicit and data deposition accession numbers are included where applicable.
- [ ] The paper distinguishes its contribution clearly from Gastroenterology-published work in the same area; scope and framing reflect Gut's clinical/translational identity.

## Common desk-reject triggers

- Basic mechanistic studies (animal or cell models only) without human tissue, genetic, or clinical correlation as the primary evidentiary layer.
- Purely descriptive microbiome composition surveys without functional validation or clinical correlation.
- Small retrospective single-center audits or case series without a pre-specified clinical question or adequate controls.
- Missing or generic "Significance of this study" box — Gut editors check this as an early triage criterion.
- Incomplete reporting guideline checklist or absent trial registration; missing data-sharing statement.

## Re-routing decision

- A GI/hepatology mechanistic paper that has a stronger basic-science identity (deeper molecular biology, less clinical data) → `gastroenterology` (AGA; more tolerant of basic-science depth with translational relevance).
- A hepatology mechanistic paper with deep molecular/genetic mechanism and limited clinical epidemiology → `journal-of-clinical-investigation` or `hepatology`.
- A GI cancer biology paper with translational oncology framing → `cancer-discovery` (AACR) or `gastroenterology`.
- A global hepatitis or liver-disease epidemiology or clinical trial changing international practice → `the-lancet`, `nejm`, or `jama` if significance warrants that tier.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Gut
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the human-data primary layer / Significance box / BMJ reporting standard clear the Gut bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Significance box / CONSORT or equivalent / BMJ COI / data deposition / open-access options>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
