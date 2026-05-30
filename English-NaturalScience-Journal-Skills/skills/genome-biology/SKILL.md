---
name: genome-biology
description: Use when targeting Genome Biology or deciding whether a genomics or computational biology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Genome Biology (genome-biology)

## Journal positioning

Genome Biology, published by BioMed Central (Springer Nature), is a leading open-access journal at the intersection of genomics, computational biology, and quantitative biological methods. It specializes in studies that combine large-scale genomic or epigenomic data with new computational tools, statistical frameworks, or biological insights, and is notable for its software- and benchmark-friendly editorial policy. The readership spans computational biologists, functional genomicists, bioinformaticians, and experimental biologists who use large-scale sequencing approaches. Papers are judged on whether they deliver both a methodological or analytical advance and meaningful biological insight; pure software papers are also publishable when rigorously benchmarked. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on genomebiology.biomedcentral.com.

## When to trigger

- The author names Genome Biology as the target venue.
- A manuscript describes a new genomics method, software tool, or computational pipeline alongside biological validation.
- A large-scale functional genomics, epigenomics, or transcriptomics study needs a venue that rewards both analytical rigor and biological interpretation.
- The author needs Genome Biology's desk-reject risks, software/data standards, and a credible alternative routing.

## Scope & topic fit

- New computational methods for genome analysis: variant calling, genome assembly, epigenome profiling, single-cell data analysis, multi-omics integration.
- Functional genomics: large-scale CRISPR screens, regulatory element mapping, chromatin organization, gene regulation mechanisms at genome scale.
- Epigenomics: DNA methylation, histone modification landscapes, 3D genome organization with functional insight.
- Single-cell genomics: new methods for cell-type classification, trajectory inference, doublet detection, or spatially resolved transcriptomics analysis.
- Comparative genomics and population genomics when the primary advance is analytical or delivers broad biological inference.
- Benchmark studies: systematic, independent comparisons of existing tools are explicitly welcomed and peer-reviewed as primary contributions.

## Method & evidence bar

- Software and methods papers must be benchmarked against existing tools on publicly available or shared datasets; performance claims require quantitative comparison.
- Biological validation of computational findings is expected: a new method should demonstrate non-trivial biological discovery on real data, not only synthetic benchmarks.
- Code must be open-source, version-controlled (GitHub or equivalent), and deposited with a persistent identifier (Zenodo); Docker/Singularity containers encouraged for reproducibility.
- All genomic data must be deposited in appropriate public repositories (GEO, SRA, ENA, ArrayExpress, ENCODE portals) prior to publication.
- Statistical rigor: multiple-testing correction, robust cross-validation, and honest reporting of failure modes are expected, especially for methods papers.

## Structure & house style

- Standard IMRAD for research articles; Methods articles, Software articles, and Database articles have distinct format expectations — verify current article-type definitions.
- Software articles are a recognized article type with specific requirements: the code must be open-source, documented, installable, and the paper must describe usage and benchmarking clearly.
- Data availability statements must include specific accession numbers for all deposited datasets; "available upon request" is not acceptable.
- Code availability statements must include a direct link to a public repository (GitHub/Zenodo) with the version used for publication.
- Figures for genomics papers should include genome-browser tracks, heatmaps, or quantitative comparisons — raw sequencing data visualization without analysis does not constitute a figure.

## Official-submission checklist

- Search the live site for "Genome Biology submission guidelines" and follow the current BioMed Central version.
- Re-check article-type options (Research, Method, Software, Database, Comment, Review) and their respective scope and format requirements.
- Confirm data deposition: all sequencing data to GEO/SRA/ENA with accession numbers; processed data and tables as supplementary.
- Verify code/software deposition: open-source license, GitHub repository, Zenodo DOI for the version of record.
- Check reporting standards: MINSEQE for sequencing experiments, MIAME for microarray data, or relevant community standards.
- Confirm open-access licensing (CC-BY default), article processing charge or waiver eligibility, competing-interests and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the computational/methodological advance and the biological insight it enables — both must be present.
- [ ] The software or pipeline is publicly available with an open-source license, documentation, and a persistent Zenodo DOI.
- [ ] All genomic/sequencing data are deposited with accession numbers confirmed; processed data and count matrices included as supplementary.
- [ ] Benchmarking against existing tools uses fair, publicly available comparison datasets; failure modes are honestly reported.
- [ ] Statistical multiple-testing correction and cross-validation strategy are described explicitly.

## Common desk-reject triggers

- Software or method presented without biological validation or without benchmark comparison against existing tools.
- Genomic data not deposited or without confirmed accession numbers at submission.
- Code not publicly available at the time of submission (proprietary, "available upon request," or behind a registration wall).
- Large-scale genomics studies that are primarily descriptive catalogues without new analytical framework or mechanistic interpretation.
- Scope more appropriate for a clinical genomics or translational journal (e.g., variant association without methodological novelty).

## Re-routing decision

- Broader biological significance beyond genomics → `plos-biology` or `elife`.
- Genetics/genomics with population-scale or GWAS-to-mechanism framing → `nature-genetics`.
- Focused molecular biology mechanism → `molecular-cell` or `the-embo-journal`.
- Computational/statistical methods with broader biological or mathematical scope → PLOS Computational Biology or Bioinformatics (OUP).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Genome Biology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the computational advance + biological validation clear Genome Biology's dual bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / data deposition / code repository / benchmarking / reporting standard / APC>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
