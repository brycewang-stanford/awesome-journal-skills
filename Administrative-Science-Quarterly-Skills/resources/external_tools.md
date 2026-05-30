# External Tools & Resources for ASQ Manuscripts

Tooling for organization-theory research targeting Administrative Science Quarterly (ASQ).
Because ASQ publishes **both** rich qualitative/inductive work and rigorous quantitative work,
this list covers both. Always verify current submission requirements on ASQ's official page.

## 1. Qualitative analysis software (CAQDAS)

| Tool | Notes |
|------|-------|
| ATLAS.ti | Coding, network/relationship views; strong for grounded-theory data structures |
| NVivo | Coding, queries, matrix coding; widely used in management qualitative work |
| MAXQDA | Coding, mixed-methods, visual tools; good document/case management |
| Dedoose | Web-based; team coding, mixed-methods, inter-coder reliability |
| Quirkos | Lightweight, visual coding; good for smaller projects/teaching |

Practices: maintain an **audit trail**, document coder agreement / disagreement resolution,
and keep an exportable record of the first-order → second-order → aggregate-dimension structure.

## 2. Quantitative & statistical software

### R
- `tidyverse` (dplyr/tidyr/ggplot2) — data wrangling and graphics
- `lme4` / `nlme` — multilevel / mixed models
- `plm` — panel data and fixed/random effects
- `survival` / `eha` — event-history / survival models
- `lavaan` — structural equation modeling
- `sandwich` + `lmtest` — robust/clustered standard errors
- `fixest` — high-dimensional fixed effects; modern DiD helpers

### Stata
- `xtreg`, `reghdfe` — panel / high-dimensional fixed effects
- `mixed` — multilevel models
- `stcox`, `streg` — Cox and parametric survival models
- `sem` / `gsem` — structural equation models
- `ivreghdfe` / `ivreg2` — instrumental variables
- `csdid`, `did_multiplegt` — staggered difference-in-differences

### Python
- `pandas`, `numpy` — data handling
- `statsmodels` — regression, panel, time-series
- `linearmodels` — panel and IV estimators
- `lifelines` — survival analysis
- `semopy` — SEM
- `networkx` — organizational/field network analysis

## 3. Network & relational analysis

- `igraph` (R/Python), `statnet`/`ergm` (R) — exponential random graph models
- UCINET + NetDraw — classic SNA toolset
- Gephi — network visualization

## 4. Historical & archival research

- Archival databases and digitized newspaper/periodical collections (institution-dependent)
- Trade-association and regulatory-filing archives for organizational/field histories
- Reference managers (below) for primary-source tracking; spreadsheets/CAQDAS for source coding

## 5. Reference management

| Tool | Notes |
|------|-------|
| Zotero | Open-source; group libraries; SAGE/ASQ author–date styles available |
| EndNote | Broad journal style support |
| Mendeley | PDF management; reference syncing |
| BibTeX/BibLaTeX | For LaTeX workflows |

ASQ uses an author–date citation style; confirm the exact CSL/EndNote style against the
current guidelines.

## 6. Writing, typesetting & figures

- Microsoft Word — most common for management submissions and tracked-changes revisions
- LaTeX (Overleaf, TeX Live/MacTeX) — for quantitative papers with heavy equations
- ggplot2 / matplotlib — publication-quality figures (check grayscale legibility)
- draw.io / OmniGraffle / PowerPoint — process-model and data-structure figures
- Grammarly / language-editing services — prose polish (the contribution still must be yours)

## 7. Submission system

- ScholarOne Manuscripts is the standard editorial system for SAGE journals such as ASQ
- Prepare an anonymized main document + a separate title page
- Accepted text formats are typically Word/PDF; verify size limits and figure formats
  against the current Manuscript Submission Guidelines

## 8. Good-practice reminders

1. **Transparency:** for qualitative work, keep coding records and the data-structure exportable;
   for quantitative work, keep clean, documented analysis code.
2. **Reproducibility:** version your data and code (Git) and label analysis scripts to match tables.
3. **Anonymity:** scrub file metadata and remove identifying acknowledgments before submission.
4. **Verify the volatile details** (limits, fees, editorial team, formatting) on ASQ's official page.
