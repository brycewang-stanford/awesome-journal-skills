---
name: sci-citation
description: Use to convert references to Science's numbered citation style — cited in order of appearance, combined main+SM list, full author lists, abbreviated journal titles. Late-stage style pass.
---

# Reference Style (sci-citation)

## When to trigger

- References are in author–date (APA/Harvard) or Nature style and must become Science style.
- The reference list is not ordered by citation appearance.
- Author lists are truncated with "et al." in the bibliography.
- Notes and references are split when Science combines them.

## Science citation mechanics

- **Numbered, in order of appearance** in the text, as italic numbers in parentheses: *(1)*, *(2, 3)*, *(4–6)*.
- A **single reference list** numbered consecutively; in Science, **main text and Supplementary Materials share one continuous numbering** (the SM continues the count). Confirm against current guidelines, but design for one list.
- **Notes and references are combined** — explanatory notes get a number in the same list.
- The reference list gives **full author lists** (Science does not truncate to "et al." in the bibliography for typical author counts).
- **Journal titles abbreviated** (per standard abbreviations); include volume, page (or article number), year.

## Reference formats (shape)

- **Journal article:**
  `A. B. Author, C. D. Author, E. F. Author, Title of the article. *Journal Abbrev.* **Volume**, page (year).`
- **Book:**
  `A. B. Author, *Book Title* (Publisher, ed., year), pp. xx–yy.`
- **Chapter:**
  `A. B. Author, in *Book Title*, C. Editor, Ed. (Publisher, year), pp. xx–yy.`
- **Dataset/code:** cite with repository, accession/DOI, and year (consistent with `sci-data`).
- **Preprint:** include the repository and DOI/identifier.

> Initials precede surnames; titles are in sentence case; journal in italics; volume in bold. Use a reference manager style file for Science to enforce this mechanically.

## Common conversion fixes

| From                              | To (Science)                                  |
|-----------------------------------|-----------------------------------------------|
| "(Smith et al., 2021)"            | "*(12)*"                                       |
| "Smith, J. (2021)."               | "J. Smith, …"                                 |
| Truncated "et al." in biblio      | full author list                              |
| Alphabetical reference list       | ordered by first appearance                   |
| Separate "Notes" section          | merged into the numbered list                 |

## Tooling

- Use Zotero/EndNote with the **Science** CSL/style; do a final manual pass on abbreviations and author-list completeness (managers often truncate).
- Verify every in-text number resolves and the list has no gaps/duplicates after the SM merge.

## Output format

```
【Style detected】 author-date / Nature / other → Science
【Numbering】 by appearance? single continuous list incl SM? yes/no
【Author lists】 full (not et al.) in biblio? yes/no
【Journal abbreviations】 applied? yes/no
【Unresolved/duplicate refs】 [...]
【Next】 sci-cover-letter
```

## Anti-patterns

- **Do not** leave author–date citations anywhere in a Science manuscript.
- **Do not** alphabetize the reference list — order is by appearance.
- **Do not** truncate author lists with "et al." in the bibliography.
- **Do not** keep separate main-text and SM reference numbering if guidelines call for one continuous list.
