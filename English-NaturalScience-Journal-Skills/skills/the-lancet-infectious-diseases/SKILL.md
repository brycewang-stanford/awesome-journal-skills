---
name: the-lancet-infectious-diseases
description: Use when targeting The Lancet Infectious Diseases or deciding whether an infectious diseases manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The Lancet Infectious Diseases (the-lancet-infectious-diseases)

## Journal positioning

The Lancet Infectious Diseases is one of the most influential specialty journals in the Lancet family, published by Elsevier. It publishes high-impact clinical, epidemiological, and public-health research across all aspects of infectious diseases—bacterial, viral, parasitic, and fungal infections; antimicrobial resistance; vaccines; outbreak science; and health-systems responses to infectious threats. The journal maintains Lancet family editorial standards: pre-registration, CONSORT compliance, global-health equity framing, and a bias toward findings that change clinical practice, public-health policy, or infectious-disease control at population scale. Research that is methodologically competent but locally contained, descriptive without actionable implications, or focused on a narrow pathogen without broader significance will not meet the bar.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Lancet/Elsevier site or submission system.

## When to trigger

- The author names The Lancet Infectious Diseases as the target venue for a clinical trial, outbreak investigation, vaccine efficacy study, or AMR epidemiology analysis.
- A manuscript on infectious disease has global-health or public-health policy implications and needs framing for the Lancet family editorial culture.
- A vaccine, antimicrobial, or antiviral trial has phase III results that could influence WHO or national immunisation or treatment guidelines.
- The author needs the journal's desk-reject risks and credible alternatives before submitting.

## Scope & topic fit

- Phase III vaccine efficacy or effectiveness trials with population-level public-health implications; immunogenicity studies are accepted when tied to correlates of protection in a practice-relevant context.
- Antimicrobial-resistance epidemiology, surveillance, and interventions: burden of AMR, genomic epidemiology of resistant pathogens, stewardship trial results.
- Clinical trials of antimicrobial, antiviral, antifungal, or antiparasitic treatments with definitive superiority, non-inferiority, or equivalence results.
- Outbreak investigation and epidemic characterisation: natural history, transmission dynamics, clinical severity, and response effectiveness.
- Pandemic preparedness and response science: epidemiological modelling with policy implications, health-systems capacity during outbreaks.
- Vector-borne disease, neglected tropical diseases, and HIV/AIDS/TB research with global-health equity framing.

## Method & evidence bar

- Clinical trials must be pre-registered, CONSORT-compliant in full, and powered for clinically or epidemiologically meaningful primary endpoints; for vaccine trials, the primary endpoint should relate to clinical outcomes or established immune correlates of protection.
- Observational and epidemiological studies require STROBE adherence; genomic-epidemiology studies should follow STREGA or equivalent molecular-epidemiology reporting standards.
- Systematic reviews and meta-analyses of ID trials require PRISMA, PROSPERO registration, and GRADE evidence grading, especially for WHO guideline-supporting reviews.
- Outbreak investigations should include case definitions, attack rates with confidence intervals, environmental and laboratory confirmation, and a policy-relevant interpretation.
- Epidemiological models must state assumptions explicitly, validate against observed data, and provide uncertainty ranges; code and data should be publicly available.
- Ethics approval, informed consent, national and institutional review (especially for work in LMICs), and data-sharing statements are mandatory.

## Structure & house style

- The Lancet Infectious Diseases uses the Lancet family structured abstract (background, methods, findings, interpretation) with a mandatory funding statement at the end of the abstract.
- An "Added value of this study" panel (what is already known, what this study adds) is required and must be precise about the evidence gap this study closes.
- Opening paragraphs must establish the global burden, policy context, or clinical unmet need—a local epidemiological context without international relevance is insufficient.
- Epidemiological figures: maps with burden data, epidemic curves, and forest plots for meta-analyses are standard; colour-blind-accessible palettes expected.
- Statistical reporting must include absolute as well as relative effect measures; vaccine efficacy should be reported with confidence intervals and the corresponding absolute risk reduction.
- Data and code availability for modelling studies and genomic analyses should specify the repository and accession identifier.

## Official-submission checklist

- Search the live site for "The Lancet Infectious Diseases information for authors" and follow the current Elsevier/Lancet version.
- Re-check article type, current word and figure limits, and "Added value" panel format.
- Confirm trial or review registration number, ethics approval reference, and informed-consent statement.
- Submit CONSORT (trials), PRISMA (reviews), STROBE (observational), or STREGA (molecular epidemiology) checklist as appropriate.
- Re-check data-sharing statement; for genomic-epidemiology and modelling studies, specify repository accession or DOI.
- Re-check competing-interests declaration, funding disclosure (especially for vaccine-industry-funded trials), ICMJE author-contribution statement, and AI-use disclosure.
- Re-check open-access/APC, licensing, and preprint policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating which clinical practice, public-health guideline, or outbreak-control policy this finding changes or informs.
- [ ] The "Added value" panel is specific: what question was unanswered before this study, and what is now established.
- [ ] The global-health or policy framing is data-supported: burden estimates, LMIC context, or WHO-relevance are documented, not asserted.
- [ ] Reporting-guideline checklist is complete and ready to upload; trial registration and ethics approval are cited in the methods.
- [ ] For genomic or modelling studies, code and data are deposited with a repository identifier.
- [ ] Competing interests, especially industry funding of vaccine or treatment trials, are fully disclosed with sponsor-independence statement.

## Common desk-reject triggers

- Clinical study on a pathogen or intervention with demonstrated local significance but no argument for broader policy or public-health impact.
- CONSORT non-compliance or absent trial registration; primary endpoint switched without documented protocol amendment.
- Epidemiological or modelling study without code or data availability, or whose assumptions are not validated against real-world data.
- "Added value" panel that is generic or duplicates what existing reviews have already established.
- Outbreak report with descriptive epidemiology only, no clinical management, control-intervention, or pathogen-characterisation data that advances beyond a standard line-list analysis.
- Vaccine immunogenicity study without clinical efficacy correlates or policy-relevant comparator.

## Re-routing decision

- ID findings with broader general medicine framing → `the-lancet`.
- Mechanistic host-pathogen biology without clinical trial anchor → `cell-host-and-microbe` or `nature-microbiology`.
- Vaccine trial with predominantly immunological rather than clinical primary endpoint → `nature-medicine`.
- AMR clinical trial with global policy framing → retain here; AMR basic microbiology → specialist microbiology journals.
- HIV, TB, malaria trials of international clinical significance → `the-lancet` if they meet the flagship practice-change bar.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The Lancet Infectious Diseases
[Topic tags] <2–3 closest topics>
[Method/evidence] <does registration / CONSORT / global-health framing / Added-value panel clear the journal's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / structured abstract / Added-value panel / reporting checklist / data & code / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
