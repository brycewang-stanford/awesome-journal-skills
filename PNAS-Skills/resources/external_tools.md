# External Tools & Resources for PNAS Submissions

A working list of repositories, software, and references useful when preparing a manuscript for *PNAS* (Proceedings of the National Academy of Sciences). Always confirm specifics against the current [PNAS Information for Authors](https://www.pnas.org/author-center/submitting-your-manuscript).

## 1. Data & code deposition (with accession/DOI)

| Data type | Deposit in |
|-----------|-----------|
| Nucleotide / genome sequences | [GenBank](https://www.ncbi.nlm.nih.gov/genbank/), [ENA](https://www.ebi.ac.uk/ena), [DDBJ](https://www.ddbj.nig.ac.jp/) |
| High-throughput sequencing | [GEO](https://www.ncbi.nlm.nih.gov/geo/), [SRA](https://www.ncbi.nlm.nih.gov/sra), [ArrayExpress](https://www.ebi.ac.uk/biostudies/arrayexpress) |
| Protein/macromolecular structures | [PDB](https://www.rcsb.org/); maps → [EMDB](https://www.ebi.ac.uk/emdb/) |
| Proteomics | [PRIDE](https://www.ebi.ac.uk/pride/) / [ProteomeXchange](http://www.proteomexchange.org/) |
| Small-molecule crystallography | [CCDC / CSD](https://www.ccdc.cam.ac.uk/) |
| Generic datasets | [Dryad](https://datadryad.org/), [Zenodo](https://zenodo.org/), [Figshare](https://figshare.com/), [OSF](https://osf.io/) |
| Code (archive a release for a DOI) | GitHub/GitLab + [Zenodo integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) |
| Materials / plasmids | [Addgene](https://www.addgene.org/) |

> PNAS requires a **Data Availability Statement** and deposition in an approved repository where one exists. "Available upon request" is not acceptable for the primary data behind the figures. Get accession numbers/DOIs **before/at** submission.

## 2. Reporting & integrity standards

- [ORCID](https://orcid.org/) — author identifiers.
- [RRID / SciCrunch](https://scicrunch.org/resources) — Research Resource Identifiers for reagents, antibodies, software.
- [ARRIVE 2.0](https://arriveguidelines.org/) — animal research reporting.
- [EQUATOR Network](https://www.equator-network.org/) — index of reporting guidelines by study type.
- [CRediT](https://credit.niso.org/) — author contribution taxonomy (useful for the contributions statement).

## 3. Figures & visualization

- Vector tools: Adobe Illustrator, [Inkscape](https://inkscape.org/) (free).
- Plotting: [matplotlib](https://matplotlib.org/), [ggplot2](https://ggplot2.tidyverse.org/), [SciencePlots](https://github.com/garrettj403/SciencePlots).
- Colorblind-safe palettes: [viridis](https://bids.github.io/colormap/), [ColorBrewer](https://colorbrewer2.org/), [Okabe-Ito](https://jfly.uni-koeln.de/color/).
- Image integrity: keep unprocessed source images; [Fiji/ImageJ](https://imagej.net/software/fiji/) with logging.
- Size figures to PNAS column widths (~9 / 11.4 / 18 cm); prepare RGB for online and check grayscale legibility (see `pnas-figures`).

## 4. Statistics & reproducibility

- R ([tidyverse](https://www.tidyverse.org/), [lme4](https://cran.r-project.org/package=lme4), [emmeans](https://cran.r-project.org/package=emmeans)), Python ([statsmodels](https://www.statsmodels.org/), [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html), [pingouin](https://pingouin-stats.org/)).
- Power analysis: [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower).
- Environments: [conda](https://docs.conda.io/), [renv](https://rstudio.github.io/renv/), [Docker](https://www.docker.com/); record versions and seeds.
- Pre-registration (esp. Social Sciences division): [OSF Registrations](https://osf.io/registries), [AsPredicted](https://aspredicted.org/).

## 5. References & writing

- Reference managers: [Zotero](https://www.zotero.org/), [EndNote](https://endnote.com/) — use the **PNAS** CSL/style (numbered, in order of appearance); verify full author lists and journal abbreviations on a final pass.
- LaTeX: PNAS provides an Overleaf [PNAS template](https://www.overleaf.com/latex/templates/tagged/pnas); Word is also accepted.
- Journal abbreviations: [CASSI / ISO 4](https://cassi.cas.org/).

## 6. Useful pages

| Page | URL |
|------|-----|
| PNAS Information for Authors | https://www.pnas.org/author-center/submitting-your-manuscript |
| PNAS Editorial & Journal Policies | https://www.pnas.org/author-center/editorial-and-journal-policies |
| PNAS submission tracks (Direct / Contributed) | https://www.pnas.org/author-center/submitting-your-manuscript |
| PNAS Classification & subject areas | https://www.pnas.org/author-center |
| PNAS Significance Statement guidance | https://www.pnas.org/author-center/submitting-your-manuscript |

## 7. Notes

1. **Submission track** is unique to PNAS: most authors use **Direct Submission**; **Contributed Submission** is available only to NAS-member authors, with an annual quota (≈2/year — confirm) and a requirement to arrange ≥2 independent reviewers (see `pnas-track`).
2. Every research article needs a **≤120-word Significance Statement** written for a broad audience (`pnas-significance`) — distinct from the ~250-word abstract.
3. Choose a **Classification**: one major division (Biological / Physical / Social Sciences) + a minor subject area, plus keywords (`pnas-writing`).
4. **Materials and Methods stay in the main text** (extended detail → SI Appendix) — unlike Science Reports / Cell.
5. Keep raw source data and unprocessed images; editors/reviewers can request them at any stage.
