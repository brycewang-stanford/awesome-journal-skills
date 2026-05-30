# External Tools & Resources (REStud-track economics)

Data sources, software, and packages for empirical, structural, and theoretical
economics manuscripts targeted at The Review of Economic Studies. REStud is
general-interest and field-agnostic, so this list spans micro, macro, trade, IO,
labor, public, and development data. Always check each source's current license and
access terms.

## 1. Data sources

### Micro / administrative

| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (USA, CPS, International) | University of Minnesota | Census/survey microdata, labor, demography |
| PSID | University of Michigan | Household panel, income, mobility |
| HRS / SHARE / ELSA | NIA / European consortia | Health, ageing, retirement |
| LEHD / Census LBD | U.S. Census (RDC) | Linked employer-employee, firm dynamics |
| Compustat / CRSP | S&P / WRDS | Firm financials, asset prices |
| World Bank Microdata / LSMS | World Bank | Development household surveys |
| AEA RCT Registry | AEA | Field-experiment pre-registration & PAPs |

### Macro / cross-country

| Source | Provider | Typical use |
|--------|----------|-------------|
| FRED | St. Louis Fed | U.S. & international macro series |
| Penn World Table | UC Davis / Groningen | Cross-country growth, productivity |
| World Development Indicators (WDI) | World Bank | Cross-country development |
| OECD.Stat | OECD | Cross-country comparable indicators |
| IMF IFS / WEO | IMF | International finance & macro |
| Maddison Project | Groningen | Long-run historical GDP |

### Trade / IO / sectoral

| Source | Provider | Typical use |
|--------|----------|-------------|
| UN Comtrade / BACI (CEPII) | UN / CEPII | Bilateral trade flows |
| EU KLEMS | consortium | Productivity, industry growth accounting |
| PatentsView / USPTO | USPTO | Innovation, patents |

## 2. Statistical software

### Stata (common for applied micro)
- `reghdfe`, `ftools` — high-dimensional fixed effects
- `csdid`, `did_multiplegt`, `eventstudyinteract` — modern staggered DID
- `bacondecomp` — Goodman-Bacon decomposition
- `honestdid` — Rambachan-Roth pre-trends sensitivity
- `ivreg2`, `weakivtest` — IV and weak-instrument diagnostics
- `rdrobust`, `rddensity` — RDD estimation and manipulation tests
- `synth`, `sdid` — synthetic control / synthetic DiD
- `estout` / `esttab`, `etable` — publication tables
- `boottest` — wild-cluster bootstrap (few clusters)

### R
- `fixest` — fast fixed-effects estimation and event studies
- `did` (Callaway-Sant'Anna), `didimputation` (Borusyak et al.) — staggered DID
- `HonestDiD` — pre-trends sensitivity
- `rdrobust`, `rddensity` — RDD
- `Synth`, `gsynth`, `synthdid` — synthetic control family
- `ivDiag`, `AER` — IV and weak-IV diagnostics
- `modelsummary` — publication tables and figures
- `fwildclusterboot` — wild-cluster bootstrap

### Python
- `pyfixest` — fixed effects, IV, event studies
- `differences` — Callaway-Sant'Anna DID
- `linearmodels` — panel, IV (2SLS, GMM)
- `statsmodels` — general econometrics
- `rdrobust` (Python port) — RDD
- `numpy` / `pandas` / `matplotlib` — data and figures

### Structural / theory
- MATLAB — DSGE, dynamic programming, value-function iteration
- Dynare (MATLAB/Octave/Julia) — DSGE solution and estimation
- Julia — high-performance structural estimation (`Optim.jl`, `JuMP.jl`)
- Knitro / Ipopt — constrained optimization for structural estimation

## 3. Identification-method references (anchor citations)

- Staggered DID: Callaway & Sant'Anna (2021); Borusyak, Jaravel & Spiess (2024); de Chaisemartin & D'Haultfœuille (2020); Sun & Abraham (2021); Goodman-Bacon (2021)
- Pre-trends: Rambachan & Roth (2023)
- Weak IV: Anderson-Rubin; Olea & Pflueger (2013); Conley, Hansen & Rossi (2012)
- Shift-share: Goldsmith-Pinkham, Sorkin & Swift (2020); Borusyak, Hull & Jaravel (2022); Adão, Kolesár & Morales (2019)
- RDD: Calonico, Cattaneo & Titiunik (2014); Gelman & Imbens (2019); Cattaneo, Jansson & Ma (2020)
- Synthetic control: Abadie, Diamond & Hainmueller (2010); Xu (2017); Ben-Michael, Feller & Rothstein (2021); Arkhangelsky et al. (2021)

## 4. Reproducibility & writing

- **Version control:** Git + GitHub/GitLab
- **Environment pinning:** `renv` (R), `requirements.txt`/`conda` (Python), version do-file (Stata)
- **Typesetting:** LaTeX (TeX Live / MacTeX), Overleaf; author-date bib via `natbib`/`biblatex`
- **Reference management:** Zotero, BibDesk, EndNote
- **Tables/figures:** `booktabs` (LaTeX), vector output (PDF/EPS)

## 5. Notes

1. **Restricted-data papers** (RDC, administrative): document the access process fully and provide runnable code; see `restud-replication-package`.
2. **Pin package versions** but use current stable releases; document them in the README.
3. **Verify current REStud / OUP policy** for data availability, length, abstract limits, and the submission portal on the journal's official page — these change.
