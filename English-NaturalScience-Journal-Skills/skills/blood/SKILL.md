---
name: blood
description: Use when targeting Blood (ASH) or deciding whether a hematology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Blood (blood)

## Journal positioning

Blood is the flagship journal of the American Society of Hematology and the highest-impact hematology-specific journal in the world. It spans the full hematology spectrum — from clonal hematopoiesis, bone marrow biology, and coagulation mechanism through to clinical trials in leukemia, lymphoma, myeloma, sickle cell disease, and hemostasis disorders — with an unusual capacity to publish both fundamental mechanistic biology and definitive clinical trial evidence within one journal. The unifying editorial requirement is that work must speak to the hematology field broadly: a pure molecular biology paper without disease relevance, or a clinical trial in a non-hematologic cancer, does not belong here. The readership is the entire ASH membership: hematologists, hematologic oncologists, transfusion medicine specialists, and hematology researchers.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ASH / Blood platform.

## When to trigger

- The author names Blood or the ASH as the target venue for a hematology or hematologic oncology manuscript.
- A paper on leukemia, lymphoma, myeloma, or benign hematology needs venue selection between Blood and other oncology or translational journals.
- A mechanistic hematopoiesis or coagulation study needs framing for the clinical relevance required at Blood.
- The author needs Blood's desk-reject risks and alternative-venue guidance before submitting.

## Scope & topic fit

- Clinical trials in hematologic malignancies (acute and chronic leukemias, lymphoma subtypes, multiple myeloma, MDS, MPN) and benign hematology (sickle cell disease, hemophilia, thrombosis, aplastic anemia) with direct ASH practice-relevance.
- Mechanistic hematopoiesis: stem cell biology, clonal hematopoiesis, lineage commitment, bone marrow microenvironment — with human bone marrow, blood, or genetic data as primary evidence.
- Coagulation and hemostasis mechanism: platelet biology, von Willebrand factor, thrombin, fibrinolysis — from molecular mechanism to clinical hemostasis implications.
- Hematologic oncology translational science: leukemia/lymphoma driver mutations, drug resistance mechanisms, minimal residual disease biology, CAR-T/immune-effector cell biology.
- Benign hematology and transfusion medicine with rigorous mechanistic or clinical trial evidence: red cell disorders, thalassemia, platelet disorders.
- Systematic reviews and meta-analyses of hematology clinical trial evidence where the synthesis is at ASH guideline-informing scale.

## Method & evidence bar

- Mechanistic studies must include human hematopoietic cells, patient-derived bone marrow, peripheral blood samples, or validated patient-derived xenograft (PDX) models as the primary evidentiary layer; mouse-only or cell-line-only studies without human corroboration are insufficient.
- Clinical trials must be prospectively registered, CONSORT-compliant, and powered for a pre-specified primary hematologic endpoint; phase I/II trials are acceptable if the mechanism and translational insight are novel and clearly articulated.
- Genomic and transcriptomic studies (single-cell, bulk RNA-seq, whole-genome sequencing) in hematologic malignancies require pre-specified analytical pipelines, appropriate controls, functional validation of key findings, and public data deposition.
- Clonal hematopoiesis or mutation studies must include clinical correlation (age, cardiovascular risk, malignancy progression) to exceed a purely descriptive variant-identification paper.
- Reporting guideline checklists (CONSORT, STROBE, PRISMA, ARRIVE) must be completed and uploaded.
- Data and code availability statements are expected; sequencing data must be deposited in dbGaP, GEO, or equivalent.

## Structure & house style

- Structured abstract for clinical trials and large clinical studies; unstructured abstract for mechanistic papers — confirm current format requirements.
- The introduction should frame the hematologic disease context and clinical or mechanistic gap; Blood editors expect the significance to be stated in terms of hematology, not generic oncology.
- Blood publishes both full-length Articles and Brief Reports; length norms differ — confirm current article-type specifications.
- A standalone "Key Points" box (two or three bullet points) is a Blood-specific requirement for all original research articles; these must capture the novel finding and its clinical or mechanistic implication precisely.
- Figures should clearly display flow cytometry gating strategies, bone marrow histology with controls, or clinical Kaplan–Meier curves with clear patient-number tables.
- Supplementary data: sensitivity analyses and secondary endpoints may go in a supplement, but primary results, patient flow, and core mechanistic data must be in the main manuscript.

## Official-submission checklist

- Search the live site for "Blood author instructions" on the ASH / Blood platform and follow the current version.
- Re-check article-type classification (Article, Brief Report, Review, Correspondence) and confirm current length and figure limits.
- Confirm prospective trial registration (ClinicalTrials.gov or equivalent) and upload ethics/IRB/consent documentation; IACUC for animal studies.
- Complete and upload the applicable reporting guideline checklist (CONSORT, STROBE, PRISMA, ARRIVE, or equivalent).
- Verify ASH conflict-of-interest and disclosure requirements; confirm all financial relationships with pharmaceutical/biotech companies are disclosed.
- Confirm "Key Points" box format and completeness — this is a mandatory submission element.
- Re-check sequencing data deposition requirements and accession number inclusion in the manuscript.
- Confirm current AI-use disclosure policy and open-access/APC options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this paper advances hematology — either a mechanistic understanding of a blood disorder or direct clinical practice evidence for hematologists.
- [ ] The "Key Points" box is sharp, specific, and non-generic: two or three bullets that can stand alone to convey the paper's contribution.
- [ ] Human hematopoietic cells, patient samples, or PDX models constitute the primary evidence layer; the link from mouse/cell model to human biology is explicit.
- [ ] Trial registration, reporting guideline checklist, ethics/consent, and ASH COI disclosures are complete.
- [ ] Sequencing or multi-omics data are deposited in a public repository with accession number included.
- [ ] Article type matches the scope: a major mechanistic advance belongs in an Article, not a Brief Report.

## Common desk-reject triggers

- Mechanistic studies relying solely on cell lines or mouse models without human hematopoietic cell or patient-sample validation.
- Clinical trials or studies in solid tumors or non-hematologic conditions without a specific hematologic biology or complication focus.
- Missing or generic "Key Points" box — Blood editors treat this as a triage criterion.
- Genomic or mutation studies that are purely descriptive catalogues without functional validation or clinical correlation.
- Small retrospective hematology cohorts without pre-specified hypotheses or adequate confounding control.

## Re-routing decision

- A hematologic oncology trial at the practice-changing, field-defining level of significance → `nejm`, `the-lancet`, or `jama` if the evidence truly warrants that tier.
- A hematology translational paper with deep molecular cancer biology that fits an oncology-biology frame → `cancer-discovery` (AACR) or `cancer-cell`.
- A hematopoiesis mechanism paper with broad stem-cell biology relevance beyond hematology → `journal-of-clinical-investigation` or `cell-stem-cell`.
- A coagulation or platelet mechanistic study with vascular biology framing → `circulation` or `journal-of-thrombosis-and-haemostasis`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Blood
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the human hematopoietic cell layer / Key Points / reporting guideline clear Blood's ASH significance bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Key Points box / CONSORT or equivalent / trial registration / data deposition / ASH COI>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
