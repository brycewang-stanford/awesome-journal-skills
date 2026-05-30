---
name: restud-replication-package
description: Use when assembling the data and code replication deposit for an accepted empirical The Review of Economic Studies (REStud) manuscript, writing the README, or auditing reproducibility before the journal's data-availability check. Builds a deposit-ready package; does not run the analysis. Verify the current REStud/OUP data policy on the official page.
---

# REStud Replication Package (restud-replication-package)

## When to trigger

- A conditional acceptance arrived and a data/code deposit is required
- Drafting the README at any point (recommended: from day one of the project)
- Auditing reproducibility before submitting the deposit
- A prior deposit was returned for incomplete provenance or non-running code

## REStud / OUP data-availability policy

For accepted empirical papers, REStud (published by Oxford University Press, run by The Review of Economic Studies Ltd) requires deposit of the data and code needed to reproduce the reported results, with a README sufficient for an independent researcher. The exact repository, forms, and timing are set by the journal/OUP and are **subject to change — verify the current policy and submission portal on the journal's official page** before depositing. The durable principle: *everything a replicator needs to reproduce every number, table, and figure, with documented data provenance.*

## Repository structure

```text
replication-package/
├── README.md (or README.pdf)
├── LICENSE                     (MIT/CC-BY for code; data per source license)
├── data/
│   ├── raw/                    (original files, never modified)
│   ├── intermediate/           (cleaned analytic datasets)
│   └── codebook/               (variable definitions, source mapping)
├── code/
│   ├── 00_setup.do             (or .R / .py)
│   ├── 01_clean.do
│   ├── 02_analysis.do
│   ├── 03_tables.do
│   └── 04_figures.do
├── output/
│   ├── tables/
│   └── figures/
└── docs/
    ├── data_appendix.pdf
    └── computing_environment.txt
```

## README required sections

1. **Overview** — what the package does, which paper, software required.
2. **Data availability and provenance** — for every dataset: source (URL/institution), citation, license/terms, date accessed, whether included and if not, why. Restricted data: commit to ≥ 5-year preservation, assist reasonable requests, make code public, document access fully.
3. **Dataset list** — table: Filename | Description | Source | Notes.
4. **Computational requirements** — OS, software versions, packages, runtime, peak memory.
5. **Description of programs** — what each script does and the run order; name the master script.
6. **Instructions to replicators** — literal step-by-step from clean state.
7. **List of tables/figures → programs** — map every published exhibit to the script and line that produces it.

## Coding discipline (adopt from day one)

- **One master script** runs the whole pipeline end-to-end.
- **Relative paths only** — never `/Users/yourname/...`.
- **Set the random seed** explicitly in any stochastic step.
- **Version-pin packages**: Stata `version 18.0` + a setup do-file; R `renv`; Python `requirements.txt` with `==` pins.
- **Log files** for every run.
- For structural/theory-empirical papers: deposit the estimation code, the solver/optimizer settings, and the counterfactual code; document convergence criteria and starting values.

## Checklist

- [ ] Master script runs from a clean state on a different machine
- [ ] All paths relative; random seeds set
- [ ] Software and package versions documented and pinned
- [ ] README covers every dataset's provenance
- [ ] Every published table/figure mapped to its producing script and line
- [ ] Restricted data: provenance + runnable code + synthetic-data smoke test where possible
- [ ] Files visible in the repository, not hidden behind one opaque ZIP
- [ ] Current journal/OUP forms and policy verified on the official page

## Anti-patterns

- Waiting until acceptance to start the deposit
- "Data available from the authors upon request" — does not satisfy a modern policy
- A README written for collaborators rather than for an unknown replicator
- Hardcoded absolute paths; unpinned packages; a master script that errors on a clean machine
- Depositing summary tables but not the code that produced the regressions
- Assuming the policy is identical to AEA's — confirm REStud/OUP specifics

## Output format

```
【DEPOSIT TYPE】public-data | restricted-data | hybrid
【README STATUS】complete / incomplete
【REPRODUCIBILITY CHECK】self-tested clean / not yet
【STRUCTURAL CODE INCLUDED】yes / n/a
【POLICY VERIFIED ON OFFICIAL PAGE】yes / no
【NEXT SKILL】restud-referee-strategy | restud-submission
```
