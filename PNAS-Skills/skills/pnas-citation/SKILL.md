---
name: pnas-citation
description: Use to convert references to PNAS's numbered citation style — cited in order of appearance, a numbered reference list, full author lists, abbreviated journal titles. Provides formats for article/book/chapter/dataset/preprint and an author-date → PNAS conversion table. Late-stage style pass.
---

# Reference Style (pnas-citation)

## When to trigger

- References are in author–date (APA/Harvard) or another journal's style and must become PNAS style.
- The reference list is not ordered by citation appearance.
- Author lists are truncated with "et al." in the bibliography.
- In-text citations are not numeric.

## PNAS citation mechanics

- **Numbered, in order of appearance** in the text, as numbers in parentheses: **(1)**, **(2, 3)**, **(4–6)**.
- A **single numbered reference list**, numbered consecutively in the order references first appear in the text.
- The reference list gives **full author lists** (PNAS does not truncate to "et al." in the bibliography for typical author counts — confirm any cap for very long lists).
- **Journal titles abbreviated** (standard ISO/CASSI abbreviations); include volume, page or article number, and year.
- Each reference includes the **article title**.

> This is PNAS's own numbered format. It resembles Science in being numbered-by-appearance, but follow the PNAS reference template for punctuation, ordering of elements, and abbreviation conventions — do not assume Science's exact formatting.

## Reference formats (shape — confirm details in current PNAS guidelines)

- **Journal article:**
  `1. A. B. Author, C. D. Author, E. F. Author, Article title. J. Abbrev. Volume, page–page (Year).`
- **Book:**
  `2. A. B. Author, Book Title (Publisher, ed. X, Year).`
- **Book chapter:**
  `3. A. B. Author, Chapter title in Book Title, C. D. Editor, Ed. (Publisher, Year), pp. xx–yy.`
- **Dataset:**
  `4. A. B. Author, Dataset title. Repository. Accession/DOI. Deposited DD Month Year.`
- **Preprint:**
  `5. A. B. Author, Title. Repository [Preprint] (Year). DOI/identifier (accessed DD Month Year).`

> Initials precede surnames; article titles in sentence case; journal abbreviated. Use a reference-manager PNAS style file to enforce this mechanically, then do a manual pass.

## Common conversion fixes

| From                              | To (PNAS)                                     |
|-----------------------------------|-----------------------------------------------|
| "(Smith et al., 2021)"            | "(12)"                                         |
| "Smith, J. (2021)."               | "J. Smith, …"                                  |
| Truncated "et al." in biblio      | full author list                              |
| Alphabetical reference list       | ordered by first appearance                   |
| In-text author–date everywhere    | sequential numbers (1), (2), … in text        |

## Worked conversion (author-date → PNAS numbered)

Source (APA, in text and list):

> "Recent work (Smith & Lee, 2021; Okafor et al., 2022) shows …"
> Smith, J., & Lee, K. (2021). Title of the article. *Journal Name*, 12(3), 45–58.

PNAS:

> "Recent work (1, 2) shows …" — where (1) is the first to appear in the text.
> `1. J. Smith, K. Lee, Title of the article. J. Name 12, 45–58 (2021).`

Note the changes: in-text becomes sequential numbers in appearance order; initials lead surnames; the article title is kept; the journal is abbreviated and italic-by-convention; volume is given without the issue number; full author list (no "et al." in the bibliography).

## Tooling

- Use Zotero/EndNote with the **PNAS** CSL/style; do a final manual pass on abbreviations and author-list completeness (managers often truncate).
- Verify every in-text number resolves and the list has no gaps/duplicates; renumber after any reordering of the text.

## Output format

```
【Style detected】 author-date / other → PNAS numbered
【Numbering】 by appearance? single numbered list? yes/no
【Author lists】 full (not et al.) in biblio? yes/no
【Journal abbreviations】 applied? yes/no
【Element shapes】 article/book/chapter/dataset/preprint correct?
【Unresolved/duplicate refs】 [...]
【Next】 pnas-submission
```

## Anti-patterns

- **Do not** leave author–date citations anywhere in a PNAS manuscript.
- **Do not** alphabetize the reference list — order is by appearance.
- **Do not** truncate author lists with "et al." in the bibliography.
- **Do not** assume Science's exact reference formatting — use the PNAS template.
