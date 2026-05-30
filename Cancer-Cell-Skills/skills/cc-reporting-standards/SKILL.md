---
name: cc-reporting-standards
description: Use when assembling STAR Methods and the Key Resources Table for a Cancer Cell (Cell Press) manuscript, and when ensuring rigor / reproducibility (cell-line authentication, mycoplasma, antibody validation, ARRIVE animal reporting, data/code deposition). It governs reporting; it does not design experiments.
---

# Rigor, Reproducibility & STAR Methods (cc-reporting-standards)

## When to trigger

- Drafting or auditing the Methods section for a Cell Press submission
- Reviewers may flag unauthenticated cell lines, undefined reagents, or missing deposition
- Need to build the Key Resources Table (KRT) and assign RRIDs
- Animal or sequencing work needs structured rigor reporting

## STAR Methods structure

Cell Press uses **STAR Methods** (Structured, Transparent, Accessible Reporting). Organize methods under standardized headings:

1. **Key Resources Table (KRT)** — at the top; tabulates every critical reagent/resource with source, identifier, and RRID.
2. **Resource availability** — Lead contact; Materials availability (plasmids, cell lines, mouse strains); Data and code availability.
3. **Experimental model and study participant details** — cell lines, animals, human subjects, organoids/PDX provenance.
4. **Method details** — full protocols, reproducible by an expert.
5. **Quantification and statistical analysis** — what test, what `n`, what software (links to `cc-statistics`).

## Key Resources Table — what must carry an RRID / identifier

| Category | Required detail |
|----------|-----------------|
| Antibodies | Host, clone, vendor, catalog #, RRID, dilution/application |
| Cell lines | Name, sex/origin, source, authentication status, RRID (Cellosaurus) |
| Chemicals / inhibitors | Vendor, catalog #, identifier |
| Critical kits | Vendor, catalog # |
| Deposited data | Repository + accession (GEO/SRA/PRIDE/PDB) |
| Oligos / sgRNAs / primers | Full sequences |
| Recombinant DNA / plasmids | Source, Addgene # / RRID |
| Organisms / strains | Strain, source, RRID (e.g., MGI/JAX) |
| Software / algorithms | Name, version, URL, RRID |

## Cell-line rigor (frequent reviewer target)

- **Authenticate** human cell lines (STR profiling); reference Cellosaurus; state the source.
- **Mycoplasma testing** — state that lines were tested negative; give frequency.
- Flag any misidentified/commonly contaminated lines (ICLAC register) and justify use.
- Report passage range and culture conditions enough to reproduce.

## Antibody validation

- Give clone, catalog, RRID, and **application-specific** validation (KO/KD control, single band of expected MW, IHC titration with positive/negative tissue).
- For new/critical antibodies, show validation in the supplement.

## Animal reporting (ARRIVE 2.0 essentials)

- Species, strain, sex, age, source; housing and husbandry.
- **Sample size** rationale; **randomization**; **blinding** of outcome assessment.
- Inclusion/exclusion criteria; humane endpoints; number used and analyzed.
- IACUC protocol number and approving institution (statement routed via `cc-ethics-registration`).

## Data and code availability

- Deposit and cite accessions in the KRT and availability statement:
  - Sequencing / arrays → **GEO/SRA**; controlled human genomics → **dbGaP/EGA**
  - Proteomics → **PRIDE**; metabolomics → MetaboLights/Workbench
  - Structures → **PDB** (+ **EMDB** for cryo-EM maps)
- Custom code → versioned public repo with a citable DOI (e.g., Zenodo).
- "Available on request" is unacceptable for these data types.

## Checklist

- [ ] STAR Methods headings used; KRT at top
- [ ] Every antibody, cell line, organism, plasmid, software has source + RRID
- [ ] Human cell lines STR-authenticated; mycoplasma-negative stated
- [ ] Antibody validation described (and shown for critical ones)
- [ ] Animal section reports sample size, randomization, blinding, exclusions
- [ ] All large datasets deposited; accessions in KRT + availability statement
- [ ] Custom code deposited with DOI
- [ ] Lead contact and materials-availability statements present

## Anti-patterns

- Cell lines with no authentication or mycoplasma statement
- Antibodies listed as "anti-X (Abcam)" with no catalog/RRID/validation
- Animal methods with no randomization/blinding/sample-size basis
- Sequencing data "available upon request" with no accession
- Methods too thin to reproduce the experiment

## Output format

```
【STAR Methods】headings complete? KRT present?
【KRT gaps】reagents missing source/RRID: [...]
【Cell-line rigor】authenticated? mycoplasma? contaminated-line flags?
【Antibody validation】adequate / show in supplement: [...]
【Animal rigor】ARRIVE elements present? [...]
【Deposition】GEO/SRA/PRIDE/PDB accessions + code DOI status
【Next step】cc-statistics or cc-ethics-registration
```
