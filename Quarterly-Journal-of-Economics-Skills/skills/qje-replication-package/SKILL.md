---
name: qje-replication-package
description: Use when assembling the data and code replication package for a Quarterly Journal of Economics (QJE) manuscript — required for accepted empirical papers. Builds a reproducible deposit; it does not perform the analysis itself.
---

# Replication Package (qje-replication-package)

## When to trigger

- The paper is heading toward acceptance and a data/code deposit is required
- You want a reproducible pipeline early, to pre-empt referee replication requests
- Reviewers or a data editor asked for materials that regenerate every exhibit
- Raw data are restricted/proprietary and you need a disclosure-compliant plan

## Why this matters at QJE

Accepted empirical papers at QJE are expected to provide **data and code replication materials**; the journal participates in the discipline-wide push toward verified reproducibility (an independent reproducibility check on accepted papers is standard practice across the AEA/top-5 ecosystem). Verify the current deposit policy, repository, and any data-editor requirements on the official journal page — specifics evolve. The durable requirement: a stranger should regenerate every number, table, and figure from your deposit.

## Package anatomy

```
replication/
  README.{md,pdf}        # the contract: data sources, software, run order, runtime
  data/
    raw/                 # as obtained (or access instructions if restricted)
    derived/             # built by code, never hand-edited
  code/
    00_setup            # installs/pins packages, sets paths
    01_build            # raw -> analysis sample
    02_analysis         # analysis sample -> estimates
    03_exhibits         # estimates -> every table & figure
  output/
    tables/  figures/    # regenerated, byte-checked against the paper
```

## README must specify

- **Data provenance**: every source, version/vintage, access date; for restricted data, exact application steps and who can obtain it.
- **Software environment**: Stata/R/Python versions and *pinned* package versions (e.g., a `requirements.txt`, `renv.lock`, or a list of `ssc`/`net` packages with versions).
- **Run instructions**: a single master script (`run_all`) and the order; expected wall-clock runtime and hardware.
- **Mapping**: a table linking every exhibit in the paper to the script and line that produces it.
- **Seeds**: set and report random seeds for any simulation, bootstrap, or randomization inference.

## Restricted-data plan

- State clearly which results can be reproduced with public data and which require restricted access.
- Provide code that runs against the restricted data plus a synthetic or public subsample so the pipeline is checkable end-to-end.
- Include the data-use agreement constraints and a disclosure-review note where applicable.

## Checklist

- [ ] One master script regenerates every table and figure from raw inputs
- [ ] Software and package versions are pinned and documented
- [ ] Every exhibit maps to a specific script/line in the README
- [ ] Random seeds set and reported for all stochastic steps
- [ ] Restricted/proprietary data have documented access steps + a runnable proxy
- [ ] No hand-edited derived data; all derived files are code-produced
- [ ] Absolute paths removed; runs from a single configurable root
- [ ] Output regenerated and checked against the manuscript numbers
- [ ] Current QJE/data-editor deposit policy verified on the official page

## Anti-patterns

- A zip of do-files with no README and no run order
- Hard-coded local paths (`/Users/me/Desktop/...`) that break on any other machine
- Derived datasets edited by hand and not reproducible from raw data
- Unpinned packages, so results drift with the next package update
- "Data available on request" with no access procedure for restricted sources
- Missing seeds, so bootstrap/RI numbers cannot be reproduced

## Output format

```
【Master script】run_all present? [Y/N]
【Env pinned】Stata/R/Python versions + package versions documented? [Y/N]
【Exhibit map】every table/figure mapped to code? [Y/N]
【Seeds】set + reported? [Y/N]
【Restricted data】access steps + runnable proxy? [Y/N / NA]
【Reproduced output】matches paper? [Y/N]
【Next step】qje-referee-strategy
```
