# External Tools and Resources for Econometrica Submissions

This document collects the external tools, typesetting infrastructure, computational
software, and data sources that are useful when preparing an Econometrica manuscript.
Because Econometrica spans econometric theory, microeconomic / game / decision theory,
and rigorous structural and empirical work, the relevant toolchain is broader than for
a purely applied journal: it must support symbolic proof work, large-scale simulation,
and a strictly enforced replication policy.

> Verify current portal rules, the Data and Code Availability Policy, and any
> submission fee / member-discount figures on the official Econometrica site before
> relying on them: https://www.econometricsociety.org/publications/econometrica

## 1. Typesetting and Mathematics

Econometrica is mathematically dense. LaTeX is the de facto standard for theory and
methods papers; clean, theorem-numbered source is expected at the revision and
final-files stage.

| Tool | Use |
|------|-----|
| LaTeX (TeX Live / MacTeX) | Primary typesetting; `amsthm`, `amsmath`, `amssymb`, `mathtools` |
| Overleaf | Online collaborative LaTeX with version history |
| `cleveref` / `hyperref` | Robust theorem / equation cross-references |
| BibTeX / BibLaTeX | Bibliography management; keep a single `.bib` source of truth |
| `econometrica.bst` / journal style | Use the journal's reference style at final-files stage (verify current file) |

Theorem environments (Definition → Assumption → Lemma → Proposition → Theorem →
Corollary) should be numbered consistently and referenced by number, never by "the
theorem above."

## 2. Symbolic and Proof Tooling

| Tool | Use |
|------|-----|
| Mathematica / Maple | Symbolic algebra, checking comparative-statics derivatives, series expansions |
| SymPy (Python) | Open-source symbolic algebra; verify hand derivations |
| Lean / Coq (optional) | Formal proof checking for delicate measure-theoretic / fixed-point arguments |

Use symbolic tools to *check* algebra (Jacobians, Hessians, expansions), not to replace
a written proof. Every claimed step in the paper must hold up to a referee reading it by
hand.

## 3. Econometric-Theory Computation

For asymptotic-theory and estimator papers, the bar includes finite-sample (Monte Carlo)
evidence.

### Python
- `numpy`, `scipy` — linear algebra, optimization, special functions, numerical integration
- `statsmodels` — baseline estimators and asymptotic standard errors for comparison
- `numba` / `cython` — speed up inner Monte Carlo loops
- `joblib` / `multiprocessing` — parallelize replications across seeds
- `matplotlib` — simulation figures (size/power curves, coverage plots)

### R
- `Matrix`, `MASS` — linear algebra and multivariate normal draws
- `sandwich`, `lmtest` — robust and clustered inference baselines
- `boot` — bootstrap procedures
- `future.apply` / `parallel` — parallel replications

### MATLAB
- Widely used in structural estimation and dynamic-programming-based models
- Optimization Toolbox, Symbolic Math Toolbox

### Julia
- Increasingly used for heavy structural and computational work (fast loops, autodiff)

## 4. Structural / Empirical Estimation

| Need | Tools |
|------|-------|
| GMM / minimum distance | Stata `gmm`, Python `statsmodels`, custom MATLAB/Julia |
| Dynamic discrete choice / DP | MATLAB, Julia, Python; value-function iteration / NFXP |
| Numerical optimization | `scipy.optimize`, KNITRO, Ipopt, `Optim.jl` |
| Automatic differentiation | JAX, `ForwardDiff.jl`, `autograd` |
| Quadrature / simulation of integrals | Gauss–Hermite, sparse grids, Halton/Sobol sequences |

## 5. Reproducibility and Replication

The Data and Code Availability Policy is strictly enforced (verify current text and the
role of the Data Editor). Build the package as you go, not at the end.

| Tool | Use |
|------|-----|
| Git | Version control for code and manuscript |
| Docker / `renv` / `conda` / `Project.toml` | Pin the computational environment |
| Make / master script (`run_all`) | One command reproduces every exhibit |
| Set/seeded RNG | Bit-for-bit reproducibility of Monte Carlo tables |
| README with run instructions | Hardware, runtime, software versions, data provenance |
| Data deposit | Journal-designated repository (e.g., openICPSR / Econometric Society supplement) — verify current location |

## 6. Reference and Literature Search

| Tool | Use |
|------|-----|
| Google Scholar | Citation tracing, working-paper versions |
| RePEc / EconPapers / IDEAS | Economics working papers and journal indexing |
| NBER / CEPR working papers | Pre-publication versions of methods and theory work |
| Zotero / EndNote | Reference management; export to BibTeX |
| MathSciNet / zbMATH | Locating the precise mathematical results a proof relies on |

## 7. Submission Logistics

- Submission portal: Editorial Express (verify current URL via the journal site).
- Submission fee with an Econometric Society member discount (verify current amounts and
  any waivers).
- Supplementary / Online Appendix is a first-class component: full proofs, Monte Carlo,
  and additional results live there.
- Long review times and multiple demanding rounds are normal; co-editors and referees
  read proofs closely.

## 8. Notes and Cautions

1. Keep a single canonical `.bib` and a single canonical theorem-numbering scheme;
   renumbering during revision is a common source of broken cross-references.
2. Seed every random draw and record seeds; a Monte Carlo table that cannot be
   reproduced bit-for-bit will fail replication review.
3. Symbolic-algebra output is a check, not a proof — never paste CAS output in lieu of an
   argument.
4. Verify all volatile specifics (fee, member discount, portal URL, current Data and Code
   Availability Policy, Data Editor procedures) on the official journal page before
   submitting.
