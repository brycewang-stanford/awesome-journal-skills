# External Tools & Resources for Cancer Cell Submissions

This document collects the external repositories, reporting frameworks, and software a molecular / translational oncology lab typically needs when preparing a Cancer Cell (Cell Press) manuscript. Always confirm the currently required repository and accession format on the live Cell Press author and STAR Methods pages before submitting.

## 1. Mandatory Data-Deposition Repositories

Cell Press requires that newly generated large datasets be deposited in a recognized public repository and that the accession number(s) appear in the Key Resources Table and the Data and code availability statement. "Available on request" is not acceptable for these data types.

| Data type | Primary repository | Notes |
|-----------|--------------------|-------|
| Bulk / single-cell RNA-seq, ChIP-seq, ATAC-seq, microarray | GEO (NCBI Gene Expression Omnibus) | Provide GSE accession; release on/before publication |
| Raw high-throughput sequencing reads | SRA (Sequence Read Archive) | Often linked from the GEO record |
| Whole-genome / exome, controlled-access human genomics | dbGaP or EGA | For patient-identifiable genomic data |
| Mass-spectrometry proteomics / phosphoproteomics | PRIDE (via ProteomeXchange) | Provide PXD accession |
| Metabolomics | MetaboLights or Metabolomics Workbench | Study identifier in availability statement |
| Macromolecular structures | PDB (wwPDB) | X-ray / cryo-EM / NMR coordinates |
| Cryo-EM maps | EMDB | Pair with PDB where a model is built |
| Flow / mass cytometry | FlowRepository | Where applicable |
| Imaging (large microscopy datasets) | BioImage Archive / IDR | Where applicable |

## 2. Oncology Reference & Mining Resources (for analysis, not deposition)

| Resource | Use |
|----------|-----|
| TCGA / GDC Data Portal | Pan-cancer genomic, transcriptomic, clinical reference cohorts |
| cBioPortal | Interactive mining of cancer genomics; survival / mutation queries |
| GTEx | Normal-tissue expression baselines |
| DepMap (CCLE + CRISPR/RNAi screens) | Cell-line dependencies, essentiality, drug sensitivity |
| Human Protein Atlas | Protein expression / localization across tumors and normals |
| COSMIC | Catalogue of somatic mutations in cancer |
| ICGC / PCAWG | International cancer genome cohorts |
| Single Cell Portal / CELLxGENE | Reference single-cell tumor atlases |

## 3. Reporting & Rigor Frameworks

| Framework | Scope |
|-----------|-------|
| STAR Methods (Cell Press) | Structured, Transparent, Accessible Reporting; includes the Key Resources Table |
| ARRIVE 2.0 | Reporting of in vivo animal experiments (design, randomization, blinding, sample size) |
| Cell-line authentication | STR profiling; reference ATCC / Cellosaurus; report mycoplasma testing |
| Antibody validation | Cite catalog + clone + RRID; validation strategy (KO/KD controls, IHC titration) |
| RRIDs (Research Resource Identifiers) | Unique IDs for antibodies, cell lines, organisms, software, plasmids |
| MIAME / MINSEQE | Minimum information for array / sequencing experiments |
| BioRender / RRID for tools | Schematic and software attribution |

## 4. Bioinformatics & Statistical Software

### Sequencing / omics pipelines
- Alignment / quant: `STAR`, `salmon`, `HISAT2`, `bwa`, `bowtie2`
- RNA-seq differential expression: `DESeq2`, `edgeR`, `limma-voom`
- Single-cell: `Seurat` (R), `Scanpy` (Python), `CellRanger`, `scVI`, `Harmony` (batch correction)
- ChIP/ATAC: `MACS2/3`, `deepTools`, `HOMER`, `ChIPseeker`
- Variant calling: `GATK`, `Mutect2`, `VarScan`, `ANNOVAR` / `VEP`
- Pathway / enrichment: `GSEA`, `clusterProfiler`, `fgsea`, `MSigDB`

### Statistics & plotting
- R: `tidyverse`, `survival` + `survminer` (Kaplan-Meier / Cox), `ggplot2`, `rstatix`
- Python: `pandas`, `numpy`, `scipy.stats`, `statsmodels`, `lifelines`, `matplotlib`, `seaborn`
- GraphPad Prism: common for bench-scale n; report exact test, n, and correction
- Multiple-comparison correction: Holm / Tukey / Bonferroni (few groups); Benjamini-Hochberg FDR (omics)

### Structure & imaging
- Cryo-EM: `RELION`, `cryoSPARC`; model building `Coot`, `PHENIX`, `ChimeraX`
- Microscopy quantification: `Fiji/ImageJ`, `CellProfiler`, `QuPath` (digital pathology / IHC scoring)
- Flow cytometry: `FlowJo`, `Cytobank`

## 5. Figure, Image-Integrity & Manuscript Tools

- Schematics / graphical abstract: BioRender, Adobe Illustrator, Inkscape
- Image integrity: keep unprocessed raw blots / micrographs; avoid splicing without clear delineation; apply linear adjustments uniformly across the whole image
- Western blot: show full-length / uncropped blots in supplement; molecular-weight markers visible
- Reference management: Zotero, EndNote, Mendeley, Paperpile
- Manuscript prep: Word or LaTeX; figures as high-resolution TIFF/EPS/PDF per Cell Press specs

## 6. Submission Logistics

- Submission portal: Cell Press / Editorial Manager-style system linked from the Cancer Cell author page (verify current URL)
- Presubmission inquiry: Cell Press allows an editorial presubmission inquiry to gauge fit before full submission
- File formats: manuscript (DOC/DOCX or PDF), figures (TIFF/EPS/PDF), supplemental items, Key Resources Table
- ORCID: register and link author ORCIDs

## 7. Good-Practice Notes

1. **Deposit early.** Create private GEO/PRIDE/PDB records during writing so accession numbers and reviewer tokens are ready at submission.
2. **RRID everything.** Antibodies, cell lines, organisms, plasmids, and key software should carry RRIDs in the Key Resources Table.
3. **Authenticate and test.** STR-authenticate human cell lines and document mycoplasma-negative status before the work is done, not after review.
4. **Preregister code.** Put analysis code in a versioned, citable repository (e.g., Zenodo DOI from a GitHub release) and cite it in the availability statement.
5. **Verify everything volatile.** Word/figure limits, fees, and required statements change — confirm on the official Cell Press / Cancer Cell author pages.
