# Management-Research Tools & Resources (AMJ)

This document lists external data sources, analysis software, and writing tools commonly used when preparing an empirical management manuscript for the **Academy of Management Journal (AMJ)**. AMJ accepts archival, survey, experimental, multi-method, and field designs, so the toolkit spans several research traditions. Always verify licensing terms and current AMJ/AOM policies before using any resource.

## 1. Data Sources

### Archival firm / strategy data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat | S&P Global Market Intelligence | Firm financials, performance |
| CRSP | Center for Research in Security Prices | Stock returns, market data |
| BoardEx | Management Diagnostics | Boards, executives, networks |
| Execucomp | S&P Global | Executive compensation |
| Thomson/Refinitiv (SDC) | LSEG | M&A, alliances, IPOs |
| Orbis / Amadeus | Bureau van Dijk | Global firm-level data |
| USPTO / PatentsView | US Patent & Trademark Office | Innovation, patents, citations |
| GEM | Global Entrepreneurship Monitor | Entrepreneurship rates |

### Survey / micro and panel data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Qualtrics / Prolific / MTurk | Various | Online surveys and experiments |
| O*NET | US Dept. of Labor | Job and occupation attributes |
| GSS | NORC, U. Chicago | Attitudes, work values |
| PSID / NLSY | U. Michigan / BLS | Careers, labor, longitudinal |
| GLOBE | GLOBE project | Cross-cultural leadership/culture |

### Text / alternative data
| Source | Use |
|--------|-----|
| SEC EDGAR (10-K, proxy) | Disclosure text, governance |
| LinkedIn / job postings | Mobility, hiring, skills |
| Glassdoor | Employee ratings, culture |
| News / press archives (Factiva, LexisNexis) | Events, reputation |

## 2. Analysis Software & Packages

### Structural equation modeling (SEM) & measurement
- **Mplus** — latent variables, complex SEM, multilevel SEM, missing data (FIML).
- **R**: `lavaan` (SEM/CFA), `semTools` (reliability, measurement invariance), `psych` (alpha, EFA).
- **Stata**: `sem`, `gsem` (generalized SEM).
- **AMOS** (SPSS) — graphical SEM.

### Multilevel / hierarchical linear models (HLM)
- **HLM** (Raudenbush & Bryk software).
- **R**: `lme4`, `nlme`, `lmerTest`; `multilevel` (ICC, r_wg).
- **Stata**: `mixed`, `melogit`; `Mplus` for multilevel SEM.

### Mediation / moderation
- **SPSS / R PROCESS macro** (Hayes) — conditional indirect effects, bootstrapped CIs.
- **R**: `mediation`, `lavaan` (indirect effects), `interactions` (simple slopes plots).

### Panel / archival econometrics
- **Stata**: `xtreg` (FE/RE), `reghdfe` (high-dimensional FE), `ivreg2`/`ivreghdfe` (IV/2SLS), `psmatch2`/`teffects` (matching), `did`/`csdid` (modern DiD), `heckman`.
- **R**: `plm`, `fixest`, `did`, `MatchIt`, `sandwich` (robust/clustered SE).

### Experiments
- Power analysis: **G*Power**, R `pwr` / `simr` (simulation-based power for interactions/multilevel).
- Pre-registration: **AsPredicted**, **OSF Registries**.

### Qualitative / mixed methods
- **NVivo**, **ATLAS.ti**, **Dedoose** — coding and analysis.
- Reporting templates for Gioia-method data structures and process models.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; supports APA/AOM-style output |
| EndNote | Broad journal style support |
| Mendeley | Elsevier |
| Overleaf / LaTeX | Optional; verify the portal accepts the format |
| Grammarly | Language polish |

The AOM Style Guide is APA-based; configure your reference manager to an APA style and reconcile against the current AOM Style Guide.

## 4. Submission & Process

- **Submission portal**: ScholarOne Manuscripts (verify the current AMJ link on the official AOM/AMJ site).
- **ORCID**: keep an ORCID linked to your account.
- **Plagiarism/originality**: journals commonly screen with iThenticate.
- **Reporting standards**: follow current AOM/AMJ transparency and data-availability policies; pre-register experiments where feasible.

## 5. Reproducibility & Transparency

1. Keep clean, commented analysis scripts (do-files, R scripts, Mplus inputs) that regenerate every table/figure.
2. Document data sources, sample-construction steps, and exclusion rules.
3. Prepare an online appendix/supplementary file for additional analyses and robustness checks.
4. Where data can be shared, prepare a de-identified dataset and codebook consistent with current policy.
5. Verify all licensing and confidentiality terms before depositing or sharing data.

## 6. Verify Before You Rely

Editorial team, submission links, formatting limits, fees, and transparency/data policies change over time. Always confirm the current requirements on the official AMJ submission page and the AOM Style Guide before submitting.
