---
name: cell-data
description: Use to build Cell's data and code deposition plan and the Data and Code Availability statement that lives inside STAR Methods Resource Availability — approved repositories, accessions/DOIs at submission, and Cell's three-bullet availability format with Mendeley Data as Elsevier's default.
---

# Data & Code Availability (cell-data)

## When to trigger

- There is no Data and Code Availability statement, or it says "available on request."
- Sequences/structures/proteomics/datasets are not deposited or lack accessions.
- Custom analysis code is not in a public, archived repository.
- You need to draft the three-bullet statement for STAR Methods Resource Availability.

## Where the statement lives

Cell's **Data and Code Availability** statement is a required subsection of **Resource Availability** inside **STAR Methods** (see `cell-star-methods`) — not a free-floating paragraph. Datasets deposited for *this paper* must also appear in the **Key Resources Table** under "Deposited Data."

## Deposit in approved repositories (with accession/DOI)

| Data type | Deposit in (examples) |
|-----------|------------------------|
| High-throughput sequencing | **GEO** / **SRA** |
| Nucleotide / genome sequences | GenBank / ENA / DDBJ |
| Protein/macromolecular structures | **PDB**; cryo-EM maps → **EMDB** |
| Proteomics / mass spec | **PRIDE** / **ProteomeXchange** |
| Imaging / general structured datasets | **BioStudies** / BioImage Archive |
| Generic datasets (Elsevier default) | **Mendeley Data**, or Zenodo / Dryad |
| Plasmids / unique reagents | **Addgene** |
| Code (archive a release for a DOI) | GitHub/GitLab **+ Zenodo** (citable DOI) |

> **Mendeley Data is Elsevier's default repository** and is the natural home for datasets without a dedicated community repository. Use a community repository (GEO, PDB, PRIDE) when one exists for the data type.

- Obtain **accession numbers / DOIs before submission**; reviewers and editors expect them in hand.
- Code that reproduces the results must be **public and archived** (a citable DOI via Zenodo) — a bare GitHub link is not durable.

## Cell's three-bullet Data and Code Availability format

Cell uses a standardized **three-statement** block. Provide a sentence for each bullet:

```
Data and Code Availability

• [DATA] [Datatype] data have been deposited at [Repository] and are publicly
  available as of the date of publication. Accession numbers are listed in the
  Key Resources Table. / This paper analyzes existing, publicly available data
  [accessions in KRT]. / This paper does not report standardized datasets.

• [CODE] All original code has been deposited at [Zenodo/Mendeley Data] and is
  publicly available as of the date of publication. DOIs are listed in the Key
  Resources Table. / This paper does not report original code.

• [ADDITIONAL] Any additional information required to reanalyze the data
  reported in this paper is available from the Lead Contact upon request.
```

Each of the three bullets must be addressed even if the answer is "this paper does not report…". Restricted human/clinical data must state the controlled-access procedure and the controlling body.

## Materials & ethics cross-links

- Unique materials sharing belongs in **Materials Availability** (`cell-star-methods`); use Addgene/MTA and state how.
- Ethics approvals (IRB/IACUC, consent, permits) belong in **Experimental Model and Subject Details**.
- Identify key reagents with **RRIDs** in the Key Resources Table.

## Output format

```
【Data deposited】 type → repository → accession/DOI (list each)  | gaps
【Code public + archived DOI】 yes/no (repo + Zenodo/Mendeley DOI)
【Three-bullet statement】 DATA ☐ / CODE ☐ / ADDITIONAL ☐ — all drafted?
【In KRT "Deposited Data"】 accessions listed? yes/no
【Restricted data】 controlled-access procedure stated where needed?
【Next】 cell-summary
```

## Anti-patterns

- **Do not** write "available on request" for the primary data behind the figures.
- **Do not** link only to a personal/lab website — use an archival repository with a DOI.
- **Do not** leave any of the three bullets unaddressed.
- **Do not** forget to mirror accessions into the Key Resources Table.
- **Do not** submit without accession numbers/DOIs in hand.

> Confirm repository requirements and the exact three-bullet wording against current Cell Press / STAR Methods guidelines.
