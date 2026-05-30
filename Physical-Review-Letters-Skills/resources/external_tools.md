# External Tools and Resources for PRL Submissions

This document collects the manuscript-preparation, computation, figure, and data-repository
tools commonly used when preparing a Physical Review Letters (PRL) submission. It is a
practical reference; always verify current APS/PRL requirements on the official author page.

## 1. Manuscript preparation (APS-specific)

| Tool | Use |
|------|-----|
| **REVTeX 4.x** | The APS LaTeX document class for PRL/PR journals — the canonical submission format |
| **TeX Live / MacTeX** | Full LaTeX distributions |
| **Overleaf** | Online LaTeX collaboration; has an APS/REVTeX template |
| **TeXstudio / VS Code + LaTeX Workshop** | Local LaTeX editors |
| **BibTeX / BibLaTeX** | Reference management within LaTeX; use the APS bibliography style |
| **APS length checker** | The automated length check run at submission (the deductible budget) — verify current behavior |

> The length limit counts body text + figures + equations + references together. Use the
> current APS length guide / formula, not a raw word count, to estimate fit.

## 2. Figure preparation

| Tool | Use |
|------|-----|
| **matplotlib** (Python) | Publication figures; export to PDF/EPS (vector) |
| **gnuplot** | Quick scientific plots; LaTeX-friendly output |
| **Origin / OriginPro** | Common in experimental physics labs |
| **Veusz** | Scientific plotting with vector export |
| **Inkscape** | Vector editing; finalize EPS/PDF, build schematics |
| **TikZ / PGFPlots** | Vector figures authored directly in LaTeX |
| **ImageMagick** | Format conversion and raster handling |

Figure norms: single-column where possible, fonts legible at print size, color-blind-safe
palettes (e.g. avoid red/green-only encoding), vector for line art, high-resolution raster
for images. Figures count against the length limit — budget them with the text.

## 3. Computation and analysis

### Python
- `numpy`, `scipy` — numerical computation, fitting, special functions
- `sympy` — symbolic algebra (derivations destined for the SM)
- `matplotlib` — figures
- `uncertainties` / `lmfit` — error propagation and curve fitting with uncertainties
- `pandas` — tabular data handling
- `qutip` — quantum dynamics / open systems (quantum information, AMO)
- `astropy` — astronomy/astrophysics data and units

### Julia
- `DifferentialEquations.jl`, `LinearAlgebra`, `Plots.jl` — high-performance simulation

### Mathematica / Maple
- Symbolic derivations, special functions, analytic checks

### MATLAB
- Signal processing, control, and legacy lab analysis pipelines

### Domain solvers (examples by subfield)
- Condensed matter: VASP, Quantum ESPRESSO, Wannier90 (DFT / electronic structure)
- Quantum many-body: ITensor, ALPS (tensor networks / Monte Carlo)
- Particle/nuclear: ROOT, Geant4 (analysis / detector simulation)
- Lattice/statistical: custom Monte Carlo; report convergence in the SM

## 4. Data and code availability

| Repository | Use |
|------------|-----|
| **Zenodo** | DOI-minting archive for datasets and code |
| **figshare** | Datasets, figures, supplementary files with DOIs |
| **GitHub / GitLab** | Code hosting; pair with a Zenodo release for a citable DOI |
| **arXiv** | Preprint posting (cond-mat, quant-ph, hep-*, gr-qc, etc.) — disclose to APS |
| **Materials Project / NOMAD** | Materials/electronic-structure data sharing |

Provide a concrete data-availability pointer rather than "available on request"; verify the
current APS data policy and what must be deposited versus stated.

## 5. Reference management

| Tool | Use |
|------|-----|
| **Zotero** | Open-source reference manager; exports BibTeX |
| **JabRef** | BibTeX-native manager |
| **Mendeley** | Reference management with PDF handling |
| **NASA ADS** | Authoritative bibliographic source for physics/astro; exports BibTeX |
| **INSPIRE-HEP** | Bibliographic database for high-energy physics; exports BibTeX |
| **Crossref / DOI** | Resolve and verify citation metadata |

## 6. Writing and review aids

- **Grammarly / LanguageTool** — grammar and style (English)
- **APS author tools / templates** — verify the current toolset on the author page
- **Overleaf track-changes / git** — collaboration and version control for revisions
- **latexdiff** — generate a marked-up "changes" PDF for resubmission

## 7. Useful links (verify before relying on them)

| Resource | Purpose |
|----------|---------|
| APS Physical Review Letters author/information pages | Authoritative scope, length, format, and policy rules |
| APS editorial submission system | Manuscript submission portal |
| REVTeX documentation | The APS LaTeX class manual |
| arXiv | Preprints across physics |
| NASA ADS / INSPIRE-HEP | Bibliographic search and BibTeX |

## 8. Notes

1. **Verify volatile specifics** (length limit, length formula, classification scheme,
   portal URL, required statements) on the official APS / PRL author page — they change.
2. **Budget figures with text.** A large or double-column figure can cost a paragraph.
3. **Keep the SM honest.** It is peer-reviewed; it is not a place to hide weak results.
4. **Vector figures** for line art; legible fonts at print size; color-blind-safe palettes.
5. **Reproducibility.** Archive code/data with a DOI and disclose any arXiv version to APS.
