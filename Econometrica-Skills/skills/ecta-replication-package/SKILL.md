---
name: ecta-replication-package
description: Use when assembling the code and data deposit for an Econometrica manuscript under the journal's Data and Code Availability Policy, including reproducible Monte Carlo and (for empirical work) data provenance. Builds and audits the replication package; it does not design the simulations (use ecta-robustness) or format exhibits (use ecta-tables-figures).
---

# Replication Package (ecta-replication-package)

## When to trigger

- You are preparing the deposit required under the Data and Code Availability Policy
- Monte Carlo tables cannot be regenerated bit-for-bit from a clean checkout
- An empirical paper has no documented data provenance or access path
- You are at acceptance / final-files stage and the Data Editor will verify reproducibility

Econometrica (and the other Econometric Society journals) enforce a **single ES-wide Data and
Code Availability Policy**. Concrete, Econometrica-specific specifics that differ from the
AER/AEJ (AEA Data Editor + openICPSR) pipeline:

- The policy applies to papers with **empirical, experimental, and/or simulation** results.
  A **pure-theory paper with no such results is effectively exempt** — but any requested
  exemption or limitation on data/code availability must be stated **at initial submission**
  (the handling Co-Editor decides; exemptions are not considered later).
- Reproducibility is verified **before final acceptance** by the **Econometric Society Data
  Editor** team. In practice you submit final files at **Conditional Acceptance** to a
  separate Editorial Express account for the Data Editor's checks and correspondence.
- The package must include a **README in PDF**; the Social Science Data Editors' README
  template is recommended and covers every required item.
- For packages **conditionally accepted after July 1, 2023**, the replication package is
  deposited at the **Econometric Society Journals' Community at Zenodo** (you may reserve a
  DOI in advance). Another trusted open repository with a permanent DOI can satisfy the
  requirement with Data Editor approval — but **not** the AEA/openICPSR route by default.

Verify the *current* policy text and deposit location on the official ES Data Editor site
before finalizing — the specifics evolve.

> Build the package as you go, not the night before final files. A package assembled from
> memory at the end almost never reproduces — and here a real human Data Editor will run it.

## What the package must contain

| Component | Requirement |
|-----------|-------------|
| Code | All scripts that produce every table, figure, and number in the paper *and* Supplemental Material |
| Master script | One command (`run_all`) regenerates every exhibit end to end |
| Random seeds | Every stochastic step seeded and recorded, so Monte Carlo tables reproduce bit-for-bit (simulations are covered by the ES policy) |
| Environment | Software, version numbers, and pinned dependencies (Docker / `renv` / `conda` / `Project.toml`) |
| README (PDF) | Hardware, expected runtime, data sources, file-by-file description, exhibit ↔ script map; use the Social Science Data Editors' README template |
| Data (empirical) | The data, or — when proprietary/restricted — exact provenance and an access path that lets a replicator obtain it |
| Deposit | The Econometric Society Journals' Community at **Zenodo** (after the Data Editor's checks; reserve a DOI in advance), unless a trusted DOI repository is approved |
| License / terms | Any data-use restrictions documented; redistribution rights respected |

## Reproducibility discipline for Monte Carlo

- **Seed everything** and record the seed alongside each table. Re-running must reproduce the
  exact numbers, not merely "similar" ones.
- **Master script** runs all simulations and writes outputs to named files that map to table
  numbers.
- **Runtime honesty.** State how long the full simulation takes and on what hardware; if it is
  days, provide a smaller smoke-test path that runs quickly and a way to verify the full run.
- **No manual steps.** No "then copy the number into the table by hand" — exhibits should be
  generated programmatically where feasible.

## Empirical data provenance

- **Public data:** include it (or a script that downloads a fixed version) plus the citation.
- **Proprietary / restricted data (e.g., licensed firm-level, confidential admin data):** you
  generally cannot redistribute it. Document the exact source, version, access procedure,
  required licenses/fees, and contact, so a replicator can obtain the *same* data. Provide all
  code, and where allowed, a synthetic or example dataset that exercises the pipeline.
- **Confidentiality:** strip personal identifiers; respect data-provider agreements; state any
  approvals obtained.

## Recommended structure

```
replication/
  README.md            # provenance, environment, runtime, exhibit↔script map
  run_all.{do,R,py,jl} # master script: one command rebuilds everything
  code/                # numbered scripts (setup → simulate/estimate → tables → figures)
  data/                # public data or a synthetic example; provenance for restricted data
  output/              # generated tables/figures (regenerable, not hand-edited)
  env/                 # Dockerfile / renv.lock / environment.yml / Project.toml
```

## Checklist

- [ ] Every table, figure, and number (paper + Supplemental Material) regenerated by code
- [ ] Single master script reproduces everything end to end
- [ ] Every random draw seeded; Monte Carlo tables reproduce bit-for-bit (simulations are in-scope)
- [ ] Environment pinned (versions + dependencies)
- [ ] README in **PDF** (Social Science Data Editors' template) documents hardware, runtime, data sources, and exhibit↔script map
- [ ] Public data included or downloaded by script with a fixed version
- [ ] Restricted data: provenance + access path documented; synthetic example provided if allowed
- [ ] Any exemption/limitation requested **at initial submission** (theory paper with no empirical/experimental/simulation results may be exempt)
- [ ] Deposit plan: Econometric Society Journals' Community at **Zenodo** (DOI reserved); Data Editor checks pass at conditional acceptance
- [ ] Confidentiality and data-use terms respected; identifiers removed
- [ ] Verified against the *current* ES Data and Code Availability Policy and Data Editor site

## Anti-patterns

- Unseeded simulations, so tables only reproduce "approximately"
- A pile of scripts with no master file and undocumented run order
- Numbers transcribed into tables by hand, untraceable to any script
- "Data available on request" with no provenance, version, or access procedure
- An environment that only runs on the author's machine (unpinned versions)
- Redistributing proprietary data in violation of the license
- Leaving package assembly to the final-files deadline

## Output format

```
【Package status】complete / gaps
【Master script】present / missing
【Seeds recorded】yes/no — bit-for-bit reproducible: yes/no
【Environment pinned】yes/no (tool: ...)
【Data】public-included / restricted-provenance-documented / theory-exempt / MISSING
【Exhibit↔script map】complete / gaps: [...]
【Deposit】Zenodo (ES Journals' Community) DOI reserved: yes/no
【Policy check】verified against current ES Data Editor policy: yes/no
【Next step】ecta-referee-strategy
```
