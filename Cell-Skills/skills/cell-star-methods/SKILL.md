---
name: cell-star-methods
description: Use to build Cell's mandatory STAR Methods — the Key Resources Table, the three Resource Availability subsections, Experimental Model and Subject Details, Method Details, and Quantification and Statistical Analysis, in the exact required order.
---

# STAR Methods (cell-star-methods)

## When to trigger

- The manuscript has a free-text Methods section (Cell requires STAR Methods).
- There is no **Key Resources Table**, or reagents lack identifiers/RRIDs/catalog numbers.
- The **Resource Availability** block is missing one of its three required subsections.
- Statistics are scattered in legends with no consolidated analysis section.

**STAR Methods = Structured, Transparent, Accessible Reporting.** It is a Cell Press signature and is **mandatory**. This is the single most important Cell-specific deliverable.

## Mandatory STAR Methods structure (exact order)

1. **Key Resources Table (KRT)**
2. **Resource Availability** — three required subsections:
   a. **Lead Contact**
   b. **Materials Availability**
   c. **Data and Code Availability**
3. **Experimental Model and Subject Details** (or **Experimental Model and Study Participant Details**)
4. **Method Details**
5. **Quantification and Statistical Analysis** (QSA)

> Some versions add **Additional Resources** at the end. Always confirm the current Cell Press STAR Methods structure and headings.

## 1. Key Resources Table (KRT)

A structured table listing **every** reagent and resource, grouped by category, each with its **source** and an **identifier** (RRID, catalog #, accession, DOI, or repository link).

| REAGENT or RESOURCE | SOURCE | IDENTIFIER |
|---------------------|--------|------------|
| **Antibodies** | | |
| Anti-X (clone, host) | Vendor / lab | Cat# ____; RRID:AB______ |
| **Bacterial and Virus Strains** | | |
| **Biological Samples** | | |
| **Chemicals, Peptides, Recombinant Proteins** | | |
| **Critical Commercial Assays** | | |
| **Deposited Data** | | |
| RNA-seq, this paper | This paper | GEO: GSE______ |
| Structure, this paper | This paper | PDB: ______ |
| **Experimental Models: Cell Lines** | | |
| **Experimental Models: Organisms/Strains** | | |
| **Oligonucleotides** | | |
| **Recombinant DNA** (plasmids) | | Addgene #______ |
| **Software and Algorithms** | | RRID:SCR______ / DOI |
| **Other** | | |

Rules:
- [ ] Every antibody, cell line, strain, plasmid, chemical, kit, oligo, dataset, and software package appears.
- [ ] Antibodies carry a **catalog #** and **RRID** where available.
- [ ] Cell lines and organisms identify the source and validation/authentication.
- [ ] Deposited data list the **accession/DOI** for *this paper's* data (see `cell-data`).
- [ ] Software lists version and an identifier (RRID:SCR___ or DOI).
- [ ] Custom code points to its repository + archived DOI.

## 2. Resource Availability (three required subsections)

- **Lead Contact** — one named corresponding author who fields resource/reagent requests, with email. (Cell typically requires exactly one Lead Contact.)
- **Materials Availability** — how unique reagents (plasmids, cell lines, antibodies, mouse lines) are shared, via Addgene/repository or under an MTA; or state "This study did not generate new unique reagents."
- **Data and Code Availability** — the three-bullet statement (data / code / additional information), each with a sentence (built in `cell-data`).

All three subsections must be present even when the answer is "none/not applicable."

## 3. Experimental Model and Subject Details

Organisms, strains, cell lines (sex, age, source, passage), patient/participant details (with ethics approvals and consent), housing, husbandry, and authentication/mycoplasma testing. State IRB/IACUC approvals and protocol numbers here.

## 4. Method Details

Step-by-step procedures in enough detail to reproduce, organized by technique with subheadings, referencing reagents by their KRT entries. Include constructs, conditions, instrument settings, and analysis pipelines.

## 5. Quantification and Statistical Analysis (QSA)

A consolidated section: for each quantified result, the **statistical test**, definition of **n** and what it represents, **dispersion** (SD/SEM/CI), significance thresholds, software used, and how outliers/exclusions were handled. Statistics stated in figure legends must be consistent with QSA.

## Output format

```
【KRT present】 yes/no — categories covered; antibodies w/ Cat#+RRID; deposited data w/ accession
【Resource Availability】 Lead Contact ☐ / Materials Availability ☐ / Data & Code Availability ☐
【Exp. Model & Subject Details】 organisms/lines/participants + ethics (IRB/IACUC)? yes/no
【Method Details】 reproducible, KRT-linked? yes/no
【QSA】 per-result test + n-definition + dispersion + software? yes/no
【Gaps】 [...]
【Next】 cell-data
```

## Anti-patterns

- **Do not** submit a free-text Methods section — Cell requires STAR Methods.
- **Do not** omit RRIDs/catalog numbers for antibodies and software.
- **Do not** drop any of the three Resource Availability subsections.
- **Do not** leave statistics only in legends — consolidate in QSA.
- **Do not** forget to list *this paper's* deposited data with accessions in the KRT.

> The exact STAR Methods headings and KRT categories are set by Cell Press — confirm against the current STAR Methods author guidelines.
