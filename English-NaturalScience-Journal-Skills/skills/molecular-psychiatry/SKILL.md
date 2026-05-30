---
name: molecular-psychiatry
description: Use when targeting Molecular Psychiatry (Mol Psychiatry) or deciding whether a biological psychiatry or translational neuroscience manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Molecular Psychiatry (molecular-psychiatry)

## Journal positioning

Molecular Psychiatry, published by Springer Nature, is a leading journal in biological psychiatry and translational neuroscience, focusing on the molecular, genetic, cellular, and circuit mechanisms underlying psychiatric disorders and their interface with clinical phenomena. It occupies the space between basic neuroscience journals and clinical psychiatry journals, demanding both mechanistic depth and clear translational or clinical relevance. The readership spans psychiatric genetics researchers, translational neuroscientists, clinical researchers, and psychiatrists interested in biological mechanisms, so a paper must articulate both the mechanism and its disease relevance. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on nature.com/mp.

## When to trigger

- The author names Molecular Psychiatry or Mol Psychiatry as the target venue.
- A psychiatric genetics, neuroimaging genetics, or mechanistic psychiatry study has both biological depth and patient-relevant findings.
- A translational neuroscience manuscript in depression, schizophrenia, bipolar disorder, autism, OCD, or addiction needs venue calibration at this tier.
- The author needs Molecular Psychiatry's desk-reject risks, significance bar, and a credible re-routing within biological psychiatry.

## Scope & topic fit

- Psychiatric genetics and genomics: GWAS, polygenic risk score applications with mechanistic follow-up, rare variant analyses with functional characterization in psychiatric conditions.
- Translational neuroscience: animal models of psychiatric disorders validated with human genetic or biomarker evidence; circuit-level mechanisms with direct psychiatric disease relevance.
- Neuroimaging in psychiatry: brain structure/function alterations in clinical populations — publishable when paired with genetic, molecular, or mechanistic insight, not as standalone descriptive imaging.
- Molecular mechanisms: synaptic, receptor, or intracellular signaling mechanisms in the context of psychiatric disease biology.
- Biomarkers and biological stratification: peripheral or central biomarkers with translational utility, when validated in clinical cohorts with appropriate size.
- Drug mechanism of action: preclinical and translational pharmacology when mechanistic insight into psychiatric drug action is primary.

## Method & evidence bar

- Dual-level evidence is the expectation: mechanistic biological data combined with human/clinical relevance. Either element alone is insufficient for the top tier.
- Psychiatric genetics papers: GWAS or sequencing studies should include functional characterization or downstream mechanistic analyses; association-only papers without mechanistic insight are better suited to specialist genetics journals.
- Animal model studies must include validated face, construct, or predictive validity for the psychiatric phenotype modelled; behavioural claims must include appropriate blinding and controls.
- Human studies (neuroimaging, clinical cohorts) require appropriate sample sizes, statistical power, and correction for multiple comparisons; replication in an independent cohort strongly preferred.
- Reporting guidelines: ARRIVE for animal work; CONSORT for clinical trials; relevant biomarker reporting standards.

## Structure & house style

- Standard IMRAD structure with unstructured abstract; Molecular Psychiatry follows Springer Nature format with a structured Methods and, for longer papers, supplementary information.
- The introduction must foreground the psychiatric disease context first, then the biological gap — the framing is translational, not basic-science-first.
- Significance statement for press/editorial highlights may be requested; the abstract should be accessible to a clinician-scientist without deep molecular biology background.
- Data availability statement and code availability statement are required; raw data and analysis code should be deposited in appropriate repositories.
- Review articles and perspectives are published — check the current policy on whether reviews are fully invited or whether unsolicited reviews are considered.

## Official-submission checklist

- Search the live site for "Molecular Psychiatry submission guidelines" and follow the current Springer Nature version.
- Re-check article-type options: original research articles, meta-analyses, reviews, perspectives, letters — confirm scope and length conventions for each.
- Complete the relevant reporting checklists: ARRIVE for animal experiments, CONSORT for trials, STROBE for observational studies; attach the checklist at submission.
- Confirm data and code availability: genomics data to dbGaP or EGA or equivalent; imaging data to relevant repositories; deposition accession numbers required.
- Verify ethics approvals: IACUC for animals, IRB/ethics board for human subjects, informed consent confirmation for patient-sample studies.
- Check competing-interests, funding, AI-use disclosure, and Springer Nature preprint policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence connecting the biological mechanism studied to a specific psychiatric condition and its unresolved clinical or translational question.
- [ ] Human evidence (genetic, clinical cohort, patient samples, or human neuroimaging) is present or the animal model is explicitly validated against human biology.
- [ ] For genetic studies, functional characterization or at minimum mechanistic hypotheses grounded in converging evidence are included.
- [ ] Reporting checklists (ARRIVE, CONSORT, etc.) are completed and ready to attach; all statistical corrections and sample-size justifications are in place.
- [ ] Data and code repositories are confirmed; accession numbers or links are ready for the data availability statement.

## Common desk-reject triggers

- Pure basic neuroscience mechanism without a specific, credible link to a psychiatric disorder — this belongs in Nature Neuroscience or Neuron.
- Psychiatric genetics association studies (GWAS hits, PRS analyses) without functional or mechanistic follow-up — better suited to Nature Genetics or Biological Psychiatry.
- Neuroimaging studies in clinical populations that are purely descriptive (group difference, no genetics, no mechanism) — insufficient for this tier.
- Animal behavioral studies without validation of the psychiatric disease model or without human/translational evidence.
- Small-N clinical or imaging studies without replication or power justification for the effect size claimed.

## Re-routing decision

- Basic neuroscience mechanism without strong psychiatric disease tie → `nature-neuroscience` or `neuron`.
- Clinical psychiatric trial or meta-analysis → JAMA Psychiatry, The Lancet Psychiatry, or `nejm` for landmark trial.
- Human behaviour and cognition across clinical/non-clinical spectrum → `nature-human-behaviour`.
- Psychiatric genetics (association primary) → `nature-genetics` or Biological Psychiatry.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Molecular Psychiatry
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the study provide both mechanistic depth and human/translational relevance?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / reporting checklist / data-code deposition / ethics / replication / sample size>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
