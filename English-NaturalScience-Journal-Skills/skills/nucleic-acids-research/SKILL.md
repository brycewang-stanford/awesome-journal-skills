---
name: nucleic-acids-research
description: Use when targeting Nucleic Acids Research (NAR) or deciding whether a nucleic-acid biology, database, or web-server manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nucleic Acids Research (nucleic-acids-research)

## Journal positioning

Nucleic Acids Research is an Oxford University Press open-access journal covering the full breadth of nucleic-acid biology — DNA, RNA, and their interactions with proteins, small molecules, and cellular machinery — from biochemistry and structural biology through genomics and computational analysis. NAR is structurally unique in publishing two recurring special issues per year: the Database Issue (January), which catalogues new and significantly updated bioinformatics databases, and the Web Server Issue (July), covering freely available web-based tools for nucleic-acid and sequence analysis. These special issues operate under separate editorial criteria from the main research track. The readership spans molecular biologists, structural biochemists, genomicists, and bioinformaticians who share the common currency of nucleic-acid science. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the NAR Oxford Academic site.

## When to trigger

- The author names NAR as the target for a nucleic-acid biology study, a new biological database, or a web-based analysis tool.
- A manuscript combines sequence analysis, structural data, or biochemical experiments on DNA/RNA with computational or bioinformatics methods.
- The author is deciding whether to submit to the Database Issue or the Web Server Issue versus the regular research track.
- The author needs NAR's scope limits and desk-reject triggers before submission, especially for borderline cases that are more genomic or protein-centered than nucleic-acid-centered.

## Scope & topic fit

- Biochemistry and structural biology of DNA replication, repair, recombination, and genome stability; RNA biogenesis, processing, and degradation mechanisms.
- Nucleic-acid–protein interactions: transcription factor binding, RNA-binding proteins, ribosomes, spliceosomes, helicases — structural and mechanistic.
- Non-coding RNA biology: regulatory mechanisms of lncRNAs, miRNAs, siRNAs, and other small RNAs, especially mechanism-oriented studies.
- Nucleic-acid–based methods and technologies: CRISPR tools, antisense oligonucleotides, aptamers, synthetic nucleic-acid systems.
- Computational genomics and sequence analysis methods with a clear nucleic-acid biology application: sequence alignment, genome annotation, epigenomics, transcriptomics, motif analysis.
- Database Issue: new databases or major updates to existing databases of nucleic-acid sequences, genomic variants, epigenomic data, RNA structures, or related annotations — must be publicly accessible.
- Web Server Issue: free-to-use web tools for sequence analysis, structural prediction, regulatory-element annotation, or related nucleic-acid biology tasks.

## Method & evidence bar

- Research articles must present a conceptual advance in nucleic-acid biology, not merely a new dataset or protocol without mechanistic or analytical insight.
- Biochemical and structural studies require standard validation: reproducibility across biological replicates, appropriate controls, deposition in public databases (GenBank, PDB, EMDB, GEO, SRA as appropriate).
- Computational methods must be benchmarked against existing tools on representative datasets; code and any required databases must be publicly available.
- Database Issue submissions: the database must be publicly accessible at a stable URL, updated to a recent release, and described with sufficient technical detail for independent re-use; content coverage and growth should be documented.
- Web Server Issue submissions: the tool must be freely accessible without registration requirements (or with minimal registration), maintained, and benchmarked or validated on real biological data.
- Reproducibility and open-data standards are integral to NAR's open-access ethos.

## Structure & house style

- Standard research Article is the primary format; shorter Breakthrough Articles exist for exceptional advances — re-check current article-type definitions on the live site.
- Abstracts are unstructured; the opening sentences should state the biological question and the main finding, not background.
- Database and Web Server papers follow the special-issue template: motivation for the resource, technical implementation, example use cases, and comparison to related resources; availability and update frequency must be stated.
- Figures for computational tools should include performance benchmarks with real data, alongside illustrative examples.
- Supplementary data and code availability are expected; for computational tools, a GitHub repository or equivalent is standard practice.
- NAR is fully open access (Oxford Academic); authors must choose a Creative Commons licence.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Nucleic Acids Research instructions to authors" and follow the current OUP version.
- Re-check submission deadlines for the Database Issue and Web Server Issue — they have fixed annual submission windows distinct from the rolling research-article track.
- Re-check article-type definitions, length and figure limits, abstract format, and open-access licence options (CC-BY is standard).
- Re-check data deposition requirements: sequence data (GenBank/SRA), structure data (PDB/EMDB), gene-expression data (GEO/ArrayExpress), etc., as appropriate.
- For Database/Web Server papers: confirm that the resource URL, availability statement, and update-frequency statements meet current editorial requirements.
- Confirm competing-interests, funding, and AI-use disclosures; re-check the current policy on preprint compatibility (bioRxiv posting is generally supported).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the nucleic-acid biology insight, the database's scope and value, or the tool's capability that is novel relative to existing resources.
- [ ] The submission track (regular research, Database Issue, or Web Server Issue) matches the manuscript type and the issue's submission window.
- [ ] For research articles: the mechanistic or analytical advance is clear and not reducible to "we generated a large dataset."
- [ ] For Database/Web Server: the resource is publicly accessible at a stable URL; benchmarking or example use cases are included.
- [ ] All data are deposited in appropriate public archives; accession numbers are included in the manuscript.
- [ ] Methods and code are sufficiently described for independent reproducibility.

## Common desk-reject triggers

- A research article that is more protein-centered than nucleic-acid-centered without a clear RNA/DNA mechanistic hook.
- A database or tool paper submitted outside the special-issue window, or describing a resource that is not publicly accessible.
- A computational study that lacks benchmarking against existing methods and does not make code or data available.
- A study that is essentially a large-dataset repository paper without biological insight or analytical advance.
- Insufficient novelty for the regular research track: incremental biochemical characterization of a nucleic-acid system without conceptual advance.

## Re-routing decision

- Mechanistic molecular biology of transcription or RNA processing with cell-biological emphasis: `the-embo-journal` or `molecular-cell`.
- Structural mechanism of a nucleic-acid complex at NSMB bar: `nature-structural-and-molecular-biology`.
- Genome-scale functional genomics / epigenomics method with broader computational biology scope: `genome-biology`.
- Bioinformatics tool with scope beyond nucleic-acid biology: Bioinformatics (OUP) or PLOS Computational Biology.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nucleic Acids Research
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the nucleic-acid focus and evidence bar — or database/tool accessibility — clear NAR's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / issue track & deadline / data deposition / open-access licence / resource URL for DB/WS>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
