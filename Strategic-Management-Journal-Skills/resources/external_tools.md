# External Tools & Data Sources for Strategy Research

This document lists data sources, software, and tools commonly used for empirical Strategic Management Journal (SMJ) submissions. Availability and licensing vary by institution; confirm access and terms before relying on any source.

## 1. Data sources

### Firm financials, performance, markets
| Source | Provider | Typical use in strategy |
|--------|----------|--------------------------|
| Compustat (North America / Global) | S&P Global | Firm financials, accounting performance (ROA, sales, R&D) |
| CRSP | University of Chicago / WRDS | Stock returns, market value, event studies |
| Compustat–CRSP merged | WRDS | Tobin's q, market-based performance |
| Orbis / Osiris | Bureau van Dijk (Moody's) | Global private + public firm financials, ownership |
| Worldscope / Datastream | LSEG (Refinitiv) | International firm and market data |

### Corporate actions, deals, alliances
| Source | Provider | Typical use |
|--------|----------|-------------|
| SDC Platinum (M&A, Alliances/JVs) | LSEG (Refinitiv) | Acquisitions, alliances, joint ventures, IPOs |
| Capital IQ | S&P Global | Transactions, ownership, segments |
| Zephyr | Bureau van Dijk | M&A deals (global) |

### Governance, boards, executives
| Source | Provider | Typical use |
|--------|----------|-------------|
| BoardEx | Management Diagnostics / WRDS | Boards, TMT, director networks |
| Execucomp | S&P Global / WRDS | Executive compensation, incentives |
| ISS (RiskMetrics) | ISS | Governance provisions, takeover defenses |
| Thomson/Refinitiv ownership | LSEG | Institutional ownership |

### Innovation, technology, nonmarket
| Source | Provider | Typical use |
|--------|----------|-------------|
| USPTO PatentsView / Google Patents | USPTO | Patents, citations, technology classes |
| PATSTAT | EPO | Global patent statistics |
| KLD / MSCI ESG | MSCI | CSR / ESG ratings (nonmarket strategy) |
| Lobbying / OpenSecrets | CRP | Political/nonmarket activity (US) |

### Industry & macro context
| Source | Provider | Typical use |
|--------|----------|-------------|
| NAICS/SIC industry data | US Census / BEA | Industry concentration, environment |
| World Bank WDI / OECD | World Bank / OECD | Cross-country institutional context |

> WRDS (Wharton Research Data Services) is the common access layer for many of the above. Survey or hand-collected data are also accepted when well documented.

## 2. Statistical software

### Stata (widely used in strategy empirics)
- `xtreg`, `reghdfe` — panel fixed effects (high-dimensional FE)
- `ivreg2`, `ivreghdfe` — instrumental variables / 2SLS with diagnostics
- `xtivreg` — panel IV
- `heckman`, `heckprobit` — selection models
- `did_imputation`, `csdid`, `eventstudyinteract` — modern staggered-DID estimators (Borusyak; Callaway–Sant'Anna; Sun–Abraham)
- `psmatch2`, `teffects`, `cem` — propensity-score and coarsened-exact matching
- `rdrobust` — regression discontinuity
- `margins`, `marginsplot` — marginal effects and interaction plots
- `estout` / `esttab` — publication-style regression tables

### R
- `fixest` — fast high-dimensional FE, IV, and clustered SEs
- `did`, `didimputation`, `fixest::sunab` — staggered DID
- `AER`, `ivreg` — instrumental variables
- `sampleSelection` — Heckman selection
- `MatchIt`, `cobalt` — matching and balance diagnostics
- `marginaleffects`, `interactions` — marginal effects / interaction plots
- `modelsummary` — regression tables; `ggplot2` — figures

### Python
- `pandas`, `numpy` — data construction
- `linearmodels` — panel FE, IV (PanelOLS, IV2SLS)
- `statsmodels` — regression, diagnostics
- `econml`, `dowhy` — causal / ML-based inference (use cautiously, justify)
- `matplotlib` / `seaborn` — figures

## 3. Identification toolkit by design

| Design | Tools |
|--------|-------|
| Staggered DID | `csdid`, `did_imputation`, `eventstudyinteract` (Stata); `did`, `fixest::sunab` (R) |
| Instrumental variables | `ivreg2`/`ivreghdfe` (Stata); `fixest`/`ivreg` (R); `linearmodels` (Python) |
| Matching + DID | `cem`, `psmatch2`, `teffects` (Stata); `MatchIt` (R) |
| Selection (Heckman) | `heckman` (Stata); `sampleSelection` (R) |
| Regression discontinuity | `rdrobust`, `rddensity` (Stata/R) |
| Sensitivity to unobservables | `sensemakr` (R), Oster bounds (`psacalc`, Stata) |

## 4. Writing, references, and reproducibility

### Reference management
| Tool | Note |
|------|------|
| Zotero | Free, open; set to the SMJ/Wiley reference style |
| EndNote | Broad journal style support |
| Mendeley | Elsevier product |

> Verify the current SMJ reference style on the official Author Guidelines and apply the matching citation-style file rather than a manager default.

### Manuscript & exhibits
- LaTeX (TeX Live / MacTeX; Overleaf for collaboration) or Word, per author preference
- `estout`/`esttab`, `modelsummary` for tables; `ggplot2`/`matplotlib`/`marginsplot` for figures
- Greyscale-legible figures (SMJ is widely read/printed in B&W)

### Reproducibility
- Git + GitHub/GitLab for code versioning
- Keep a clean replication folder (code + variable construction + data provenance) — useful for review and any data-availability statement
- Plagiarism/originality: iThenticate (publisher-side) is commonly used; keep self-citation transparent

## 5. Notes & cautions

1. **Verify volatile specifics** (word limit, fees/open access, required statements, reference style) on the official SMJ page; this file covers durable tools only.
2. **Data licensing**: respect WRDS / vendor agreements; do not redistribute proprietary data.
3. **Identification first**: choose tools from the *threat* (selection, reverse causality, unobserved heterogeneity), not from convenience.
4. **Document everything**: SMJ reviewers probe sample construction and measurement; keep an auditable trail.
