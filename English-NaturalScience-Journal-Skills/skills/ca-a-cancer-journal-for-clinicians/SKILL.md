---
name: ca-a-cancer-journal-for-clinicians
description: Use when targeting CA: A Cancer Journal for Clinicians (CA Cancer J Clin) or deciding whether an oncology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# CA: A Cancer Journal for Clinicians (ca-a-cancer-journal-for-clinicians)

## Journal positioning

CA: A Cancer Journal for Clinicians is the flagship publication of the American Cancer Society and consistently ranks among the most widely read journals across all of medicine. It publishes authoritative invited reviews, clinical practice updates, and the definitive annual Cancer Statistics report — the primary epidemiological reference for U.S. cancer burden. The readership is broad-practice oncology: oncologists, primary-care clinicians, cancer researchers, and public-health professionals who need synthesis, not primary data discovery. Nearly all content is solicited by the editors; unsolicited primary research manuscripts are not the journal's core output.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ACS / Wiley site and the editorial submission system.

## When to trigger

- An author is invited by the CA editors to write a review, clinical update, or cancer-statistics analysis.
- A manuscript is a comprehensive evidence synthesis or practice-guidance update on a major cancer topic and the author wants to assess whether to approach CA editors.
- The author needs to understand CA's editorial DNA before responding to an invitation or drafting an inquiry letter.
- A primary-research cancer manuscript is being mis-targeted here and needs re-routing.

## Scope & topic fit

- The annual Cancer Statistics series (U.S. incidence, mortality, survival, trends): the defining franchise of the journal.
- Authoritative, clinician-oriented reviews of cancer prevention, screening, diagnosis, treatment, and survivorship across major cancer types.
- Global cancer burden analyses and international epidemiological updates commissioned alongside the statistics reports.
- Clinical practice guideline summaries or evidence-synthesis updates of direct utility to practicing oncologists.
- Emerging modalities (immunotherapy, targeted agents, precision oncology, liquid biopsy) covered as clinician-facing synthesis once sufficient evidence warrants a definitive statement.

## Method & evidence bar

- Reviews must synthesize the highest-quality evidence (meta-analyses, landmark trials, major cohort studies) rather than re-reporting a single dataset.
- The Cancer Statistics content demands rigorous epidemiological methods, transparent data sourcing from registries (SEER, NPCR, ACS surveillance databases), and clear uncertainty/confidence-interval reporting.
- Clinical updates must reflect current guideline landscapes (ASCO, NCCN, ACS guidelines) and situate recommendations within the evidence hierarchy.
- Statistical claims require complete methodological transparency; suppress-rule handling and population-denominator choices must be reported.
- No primary clinical-trial data without a commissioned editorial framework; mechanistic laboratory research is outside scope.

## Structure & house style

- Invited articles follow a narrative review structure with a strong clinical-takeaway orientation throughout; subsection headers should guide busy clinicians efficiently.
- The abstract is typically unstructured and concise, distilling the key clinical message.
- Tables and figures must be publication-quality and clinician-interpretable; data-dense epidemiological maps and trend charts are signature exhibits for the statistics series.
- Author credentials and conflict-of-interest status are prominent; the ACS editorial brand requires transparent funding and affiliation disclosure.
- Referencing must be comprehensive but prioritized toward landmark studies and clinical evidence rather than exhaustive literature cataloguing.

## Official-submission checklist

- Search the live site for "CA: A Cancer Journal for Clinicians author instructions" and follow the current ACS/Wiley version.
- Confirm whether the manuscript type is invited or whether an unsolicited inquiry/proposal is appropriate for the topic; most content is commissioned.
- Re-check abstract format and length, article-type specifications, figure-preparation requirements, and table formatting standards.
- Re-check conflict-of-interest and funding-disclosure requirements (ACS standards are strict given the journal's public-health role), AI-use disclosure, and data-source citation requirements for statistics content.
- If registry or surveillance data are used, confirm data-use agreements, deposition or availability statements, and any suppression or confidentiality obligations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] Confirm the manuscript was invited or that an inquiry to the editors has been sent and received a positive response; submitting unsolicited primary research here wastes review bandwidth.
- [ ] The central message is phrased as a clinical or public-health takeaway, not as a discovery claim.
- [ ] Every epidemiological figure traces to a named registry or surveillance database with explicit methodology.
- [ ] The review covers the current guideline landscape and situates evidence recommendations within it.
- [ ] Conflict-of-interest, ACS affiliation, and funding disclosures are complete and ready.

## Common desk-reject triggers

- Unsolicited primary-research manuscripts (laboratory, clinical trial, or observational study) submitted without editorial invitation or prior inquiry.
- Reviews that rehash a narrow single-institution dataset rather than synthesizing the field-wide evidence base.
- Cancer statistics or epidemiology content that lacks transparent methodology, registry sourcing, or uncertainty quantification.
- Manuscripts addressing highly specialized mechanistic or translational questions of limited direct clinical practice relevance.
- Clinical updates that are not anchored to current major guidelines or evidence hierarchies, reducing utility to practicing clinicians.

## Re-routing decision

Unsolicited primary oncology research belongs at `journal-of-clinical-oncology` (ASCO flagship for definitive clinical trials), `the-lancet-oncology` (practice-changing clinical oncology), or `cancer-discovery` (AACR, high-impact translational/clinical biology). Mechanistic cancer biology without clinical synthesis framing belongs at `cancer-cell`. Epidemiological cancer research as a standalone study fits `jama`, `the-lancet`, or specialty oncology journals rather than CA.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] CA: A Cancer Journal for Clinicians
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the content a commissioned synthesis or statistics analysis, not unsolicited primary data?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <invitation status / article type / abstract / COI disclosure / registry data sourcing>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
