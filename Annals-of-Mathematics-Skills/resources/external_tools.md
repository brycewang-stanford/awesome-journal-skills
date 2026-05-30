# External Tools and Resources for Pure-Mathematics Manuscripts

This document collects the typesetting tools, reference databases, proof-assistant
software, and writing aids that are useful when preparing a theorem-and-proof
manuscript for **Annals of Mathematics**. Always verify current requirements on the
journal's official page (annals.math.princeton.edu) before submitting.

## 1. Typesetting

Annals of Mathematics is typeset in TeX, in the AMS / Annals house style. A manuscript
should compile cleanly with a standard distribution and use AMS packages.

| Tool | Notes |
|------|-------|
| TeX Live / MacTeX | Full distributions; ship `amsmath`, `amsthm`, `amssymb`, `amscd` |
| Overleaf | Online collaboration; pin a TeX Live version for reproducibility |
| TeXShop / TeXstudio / VS Code + LaTeX Workshop | Common editors |
| `latexmk` | Reliable multi-pass builds (handles BibTeX, cross-refs, index) |

### Core AMS packages

- `amsmath` — display equations, aligned environments, multiline formulas
- `amsthm` — `theorem`/`lemma`/`proposition`/`definition`/`remark` environments and `proof`
- `amssymb`, `amsfonts` — blackboard bold, fraktur, standard symbols
- `amscd` or `tikz-cd` — commutative diagrams
- `mathtools` — fixes and extensions to `amsmath`
- `hyperref` — internal links; load last (with care on the Annals style)
- `cleveref` — consistent `\cref` references to theorems, equations, sections

> Use a single, consistent theorem-numbering scheme (e.g. number all environments
> within section: Theorem 1.1, Lemma 1.2). Confirm the journal's preferred scheme.

## 2. Bibliography and Reference Databases

| Resource | Use |
|----------|-----|
| MathSciNet (AMS) | Authoritative reviews; canonical BibTeX via "Citations → BibTeX" |
| zbMATH Open | Open abstracting/reviewing database; free citation export |
| arXiv (math.*) | Preprints; cite with arXiv identifier until a version of record exists |
| MathOverflow | Locating folklore results and pointers to the literature (not a citation) |
| Google Scholar | Cross-checking citation completeness and finding later work |

- Prefer the **published version of record**; if you must cite a preprint, label it as
  such and update at proof stage.
- MathSciNet `\MR{}` numbers and standardized journal abbreviations keep the
  bibliography uniform; use BibTeX with `amsplain` or `alpha`-style keys.

## 3. Proof Assistants and Verification Aids (optional)

These do not replace a human-readable proof, but can catch errors in long arguments.

| Tool | Use |
|------|-----|
| Lean / mathlib | Formalizing definitions and lemmas; growing library |
| Coq | Interactive theorem proving |
| Isabelle/HOL | Formal verification of substantial results |
| SageMath | Exploratory and exact symbolic/number-theoretic computation |
| GAP | Computational group theory and discrete structures |
| Magma | Algebra, number theory, algebraic geometry computation |
| Macaulay2 | Commutative algebra and algebraic geometry |

> If a result depends on machine computation, describe the computation precisely,
> make the code/data available, and state what was checked — referees must be able
> to reproduce or audit it.

## 4. Diagrams and Figures (rare in pure math)

| Tool | Use |
|------|-----|
| `tikz-cd` | Commutative diagrams (preferred, vector output) |
| `amscd` | Simple commutative diagrams |
| TikZ / PGF | General mathematical figures, when genuinely needed |
| Inkscape | Hand-drawn vector figures exported to PDF |
| Asymptote | Programmatic precise vector graphics |

- Figures are optional and uncommon; include one only when it clarifies the argument
  more efficiently than prose. Use vector formats (PDF/EPS), never raster screenshots.

## 5. Writing and Collaboration Aids

| Tool | Use |
|------|-----|
| Git + GitHub/GitLab | Version the `.tex` source and track proof revisions |
| `latexdiff` | Generate marked-up "changes" PDF for revisions to referees |
| chktex / lacheck | Lint LaTeX source for common errors |
| Grammarly / language services | Light language polish for non-native authors |

## 6. Submission Logistics

- Submission is electronic; check the official **Submission** page for the current
  portal, accepted formats (typically a compiled PDF plus, on acceptance, TeX source),
  and any cover-letter expectations.
- Keep an arXiv preprint identifier handy if you have posted one; many authors do.
- Expect a long review: detailed verification of proofs by experts can take a year or
  more. Plan correspondence and revisions accordingly.

## 7. Notes and Good Practice

1. **Reproducibility of computation**: archive code/data for any computer-assisted step.
2. **Reference hygiene**: every cited result you rely on must be published and verifiable;
   avoid leaning on unpublished claims or private communications for essential steps.
3. **Source cleanliness**: a manuscript that compiles without errors and uses standard
   AMS environments eases both review and production.
4. **Backups and versioning**: keep the full TeX history; you will need precise
   line-level diffs when responding to a referee.
5. **Verify volatile details** (portal URL, file-format rules, length expectations) on
   the journal's official page — these change over time.
