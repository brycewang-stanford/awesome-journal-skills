---
name: pnas-data
description: Use to build PNAS's Data Availability Statement and deposition plan — mandatory deposition of data in an approved repository at submission, accession numbers/DOIs, public + archived code, and materials sharing. "Available on request" is not sufficient for primary data.
---

# Data & Code Availability (pnas-data)

## When to trigger

- There is no **Data Availability Statement**, or it says "available on request".
- Sequences/structures/datasets are not deposited or have no accession numbers.
- Custom analysis code is not in a public, archived repository.
- Unique reagents/strains/cell lines have no sharing plan.

## PNAS's standard (the bar)

PNAS requires a **Data Availability Statement** in every research article, and that the **data and materials needed to support the conclusions be deposited and available at the time of submission/publication**. For data types with an established public repository, **deposition is required**, and the **accession numbers/DOIs go in the Data Availability Statement**. **"Available upon request" is not sufficient for the primary data** underlying the figures and conclusions.

## Deposit in approved repositories (with accessions)

| Data type                          | Deposit in (examples)                      |
|------------------------------------|--------------------------------------------|
| Nucleotide / genome sequences      | GenBank / ENA / DDBJ                        |
| High-throughput sequencing         | GEO / SRA / ArrayExpress                    |
| Protein/macromolecular structures  | PDB; maps → EMDB                            |
| Proteomics                         | PRIDE / ProteomeXchange                     |
| Crystallographic data              | CCDC / CSD                                  |
| Generic datasets                   | Dryad / Zenodo / Figshare / OSF            |
| Code                               | GitHub/GitLab **+ archived** to Zenodo (DOI) |

- Obtain **accession numbers / DOIs before/at submission**; cite them in the Data Availability Statement and Materials and Methods.
- Code that produces the results must be **public and archived** (a versioned release with a citable DOI; a bare GitHub link is not durable).

## Data Availability Statement (template)

> *All study data are included in the article and/or SI Appendix. [Sequencing data have been deposited in GEO (accession GSEXXXXXX).] [Structures have been deposited in the PDB (XXXX).] [Analysis code has been deposited in Zenodo (DOI: 10.5281/zenodo.XXXXXXX).] [Previously published data used in this work are available at …] [Restricted data (e.g., human-subjects data) are available under … from … subject to …]*

Avoid bare "data available on request" for primary data; restricted human/clinical data must state the access procedure and the controlling body.

## Where the statement and the data live

- The **Data Availability Statement** is a required element of the article (near the end, before/with the references — confirm placement in current guidelines).
- Datasets too large for a figure but central to the conclusions can go in **SI Appendix** or, if very large, in an external repository cited by accession/DOI — not "available on request."
- Reference the deposited data in **both** the Data Availability Statement **and** the Materials and Methods, so a reader following the methods can reach the data.

## Materials & reagents

- Unique materials (plasmids, cell lines, strains, antibodies) should be available, e.g., via Addgene/repositories or under an MTA; state how.
- Identify key reagents with RRIDs where available.

## Ethics & compliance (as applicable)

- Human-subjects: IRB/ethics approval + informed consent statement.
- Animal work: IACUC/animal-ethics approval and guideline compliance.
- Field/biodiversity: permits and the Nagoya Protocol where relevant.
- Dual-use / biosafety: flag if applicable.

## Output format

```
【Data deposited】 type → repository → accession/DOI (list each) | gaps
【Code public + archived DOI】 yes/no (link + DOI)
【Data Availability Statement】 drafted? compliant (no "on request" for primary data)?
【Materials sharing】 plan for unique reagents (Addgene/MTA)
【Ethics approvals】 IRB / IACUC / permits present where needed?
【Next】 pnas-significance
```

## Anti-patterns

- **Do not** write "data available on request" for the primary data behind the figures.
- **Do not** link only to a personal/lab website (not durable) — use an archival repository with a DOI.
- **Do not** forget to make code public and versioned; reviewers may try to run it.
- **Do not** submit without accession numbers in hand for deposited data.
