---
name: nature-biotechnology
description: Use when targeting Nature Biotechnology or deciding whether a biotechnology/enabling-methods manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Biotechnology (nature-biotechnology)

## Journal positioning

Nature Biotechnology is the Nature Portfolio's venue for enabling technologies, platforms, and methods that have broad applied impact across biological research, medicine, or industry — with the distinguishing emphasis on translational potential and broad adoption at scale. Where Nature Methods' primary criterion is generalizable methodological advance for research, Nature Biotechnology additionally asks whether the technology could be (or already is) transformative for a wider application domain: therapeutics, diagnostics, agriculture, bioindustrial production, or research infrastructure. Papers must demonstrate both technical rigor and a compelling case for broad utility. The readership spans researchers, clinicians, engineers, and industry scientists.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Nature Portfolio site or submission system.

## When to trigger

- The author names Nature Biotechnology as the target venue.
- A new platform technology, cell-engineering approach, or therapeutic tool is being assessed for venue fit against Nature Methods, Nature Medicine, or Cell Chemical Biology.
- A study delivering a biotechnological platform with demonstrated in vivo proof-of-concept needs to assess its significance level.
- The author needs Nature Biotechnology's specific desk-reject risks and re-routing options.

## Scope & topic fit

- Genome editing and gene therapy: new base editors, prime editors, CRISPR delivery systems, epigenome editors — when the advance is the enabling technology rather than the biological discovery.
- Cell engineering and synthetic biology: CAR-T and adoptive-cell therapy platforms, synthetic gene circuits, biosensors, cellular reprogramming methods with therapeutic or industrial application.
- Protein and nucleic-acid therapeutics: mRNA delivery, antisense oligonucleotides, AAV capsid engineering, antibody engineering — at the platform/enabling level.
- Sequencing and multi-omics technologies with broad applied impact: new sequencing chemistry, spatial multi-omics platforms, single-cell proteomics — when the technology itself is the advance.
- Bioprocessing, biomanufacturing, and synthetic biology for industrial applications: metabolic engineering of microbes or cell lines for production, biosynthetic pathways with commercial relevance.
- AI/ML-driven design tools for biology: protein design (de novo or structure-guided), antibody optimization, genome prediction — when the algorithmic advance has broad application demonstrated empirically.

## Method & evidence bar

- Broad demonstrated utility is required: the technology must be shown to work across multiple targets, cell types, organisms, or application contexts — not just optimized for one system.
- In vivo proof of concept substantially strengthens applications in therapeutics; cell-culture-only demonstration of a therapeutic tool is often insufficient.
- Benchmarking against the existing gold-standard technology is expected: efficacy, specificity, safety, and scalability compared honestly.
- For therapeutic applications: preclinical animal models with PK/PD, efficacy, and preliminary safety data are expected; IND-enabling data, while not required, are noted favorably.
- Reproducibility and manufacturability: methods must be reproducible in principle by other groups; highly specialized custom instruments weaken the case.
- Data/code availability: software, pipelines, and protocols deposited; Nature reporting summary required.

## Structure & house style

- Nature Portfolio format: unstructured abstract; main text; Extended Data figures for additional benchmarking and validation; Supplementary Information for methods details and large tables.
- Nature reporting summary required; ARRIVE guidelines for animal studies; human-subjects documentation where applicable.
- The introduction should establish the unmet need in biology, medicine, or industry that the technology addresses — not only the scientific gap.
- Results should follow: (1) technology design and mechanism, (2) in vitro performance and benchmarking, (3) in vivo or applied demonstration, (4) breadth of application.
- Titles should convey the technology and its application domain; they are often more applied in tone than a basic-science journal.
- Competing-interests and IP disclosure is particularly important at this venue given frequent industry involvement; re-check current requirements.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search "Nature Biotechnology author information" on the Nature Portfolio site and follow the current version.
- Re-check article types (Article vs. Brief Communication), length and figure limits, and Extended Data policy.
- Confirm Nature reporting summary requirements and applicable field-specific checklists (ARRIVE, ICH guidelines for preclinical studies).
- Re-check code/software deposition requirements and protocol deposition (protocols.io).
- Verify competing-interests disclosure — including patent applications, company affiliations, and equity — which is scrutinized closely at this venue.
- Re-check data availability requirements and open-access/APC options.
- Confirm preprint policy and AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what technological capability this paper delivers and for which application domain it is transformative.
- [ ] The technology is demonstrated across multiple targets, systems, or organisms — not only the authors' favored context.
- [ ] In vivo demonstration or equivalent applied-context validation is included (or its absence is justified for early-stage platform papers).
- [ ] Benchmarking against the current gold-standard technology is honest and rigorous.
- [ ] Competing-interests including IP and company affiliations are fully disclosed.
- [ ] Nature reporting summary, code/protocol deposition, and data availability are prepared.

## Common desk-reject triggers

- A technology demonstrated only in one cell line or one model system with no evidence of generalizability.
- A narrow incremental improvement (better editing efficiency by a modest margin) in a system already well-served by existing tools.
- A tool paper better suited to `nature-methods` (research-methods focus with no applied/translational horizon) or to a specialist technology journal.
- A biological discovery using an existing technology — the biology, not the tool, is the advance.
- Undisclosed IP conflicts or lack of transparency about industry sponsorship.

## Re-routing decision

- Primary advance is a generalizable research method without a strong translational/industrial application → `nature-methods`.
- Platform delivers a clinical/translational advance with strong mechanism and in vivo/clinical data → `nature-medicine` (if patient benefit is the frame) or `science-translational-medicine`.
- Genomics or bioinformatics tool with strong benchmarking and biological application → `nature-methods` or `genome-biology`.
- Strong applied biotechnology below Nature Biotechnology significance → `nature-communications`, ACS Synthetic Biology, or Nucleic Acids Research (`nucleic-acids-research`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Biotechnology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the technology demonstrate broad utility and in vivo / applied proof-of-concept?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Extended Data / reporting summary / competing-interests & IP / code-protocol deposition>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
