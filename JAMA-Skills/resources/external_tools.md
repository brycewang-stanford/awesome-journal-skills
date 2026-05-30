# Clinical-Research External Tools & Resources

Tools, standards, and data sources useful when preparing a clinical manuscript for
JAMA. Always confirm journal-specific requirements on JAMA's official Instructions
for Authors page; the resources below are field standards, not JAMA policy.

## 1. Reporting guidelines (EQUATOR Network)

| Guideline | Use for | Source |
|-----------|---------|--------|
| CONSORT | Randomized clinical trials (+ flow diagram) | equator-network.org |
| STROBE | Observational studies (cohort, case-control, cross-sectional) | equator-network.org |
| PRISMA | Systematic reviews / meta-analyses (+ selection diagram) | prisma-statement.org |
| STARD | Diagnostic-accuracy studies | equator-network.org |
| SPIRIT | Trial protocols | spirit-statement.org |
| TRIPOD | Prediction models | equator-network.org |
| SQUIRE | Quality-improvement studies | squire-statement.org |
| CHEERS | Economic evaluations | equator-network.org |

The EQUATOR Network (equator-network.org) is the master library — search it for the
guideline matching any design, plus abstract-level extensions (e.g., CONSORT for Abstracts).

## 2. Trial & protocol registration

| Registry | Use |
|----------|-----|
| ClinicalTrials.gov | Primary US trial registry (ICMJE-accepted) |
| WHO ICTRP | Portal to ICMJE-accepted primary registries worldwide |
| ISRCTN | International trial registry |
| PROSPERO | Systematic-review protocol registration |

Register trials **prospectively (before first enrollment)** per ICMJE policy.

## 3. Statistical software

### R
- `survival`, `survminer` — time-to-event analysis and Kaplan-Meier plots
- `meta`, `metafor` — meta-analysis and forest plots
- `mice` — multiple imputation for missing data
- `tableone` — baseline-characteristics (Table 1) generation
- `gtsummary` — publication-ready tables with effect estimates + CIs
- `pwr` — power / sample-size calculations

### Stata
- `stcox`, `sts graph` — Cox models and survival curves
- `meta` (Stata 16+) — meta-analysis and forest plots
- `mi` — multiple imputation
- `power` — sample-size and power
- `roctab` / `roccomp` — diagnostic accuracy / ROC analysis

### Python
- `lifelines` — survival analysis
- `statsmodels` — regression, confidence intervals
- `scipy.stats` — hypothesis tests, distributions
- `pandas` — data management

### Sample size (standalone)
- G*Power — power analysis
- PASS — sample-size software

## 4. Reference management & style

| Tool | Note |
|------|------|
| EndNote | Has an AMA / JAMA output style |
| Zotero | Free; AMA style available |
| Mendeley | Elsevier; AMA style available |

JAMA follows the **AMA Manual of Style** for references, units, abbreviations, and
statistical notation. Set your manager to the AMA style and verify against the manual.

## 5. Figures

- Flow diagrams: draw.io, Lucidchart, or the CONSORT/PRISMA diagram generators
- Forest plots: `metafor`/`meta` (R), `meta` (Stata)
- Kaplan-Meier: `survminer` (R), `sts graph` (Stata) — include numbers at risk
- Vector formats (EPS/PDF/TIFF) at the resolution the journal specifies
- Colorblind-safe palettes (e.g., viridis); confirm grayscale legibility

## 6. Integrity & screening

- iThenticate / Turnitin — text-overlap screening
- ICMJE Disclosure of Potential Conflicts of Interest form — collect from every author
- Retraction Watch / database checks — verify cited references are not retracted

## 7. Key references to keep on hand

- ICMJE Recommendations (icmje.org) — authorship, registration, disclosures, data sharing
- EQUATOR Network (equator-network.org) — reporting guidelines
- AMA Manual of Style — house style
- GRADE (gradeworkinggroup.org) — certainty-of-evidence rating for reviews

## 8. Notes

1. Verify all JAMA-specific limits and required files on the current author instructions.
2. Do not cite editor names, fees, or impact factors from memory — check the journal site.
3. Keep analysis code and a locked dataset for the data-sharing statement and statistical review.
4. Prospective registration cannot be fixed retrospectively — register before enrollment.
