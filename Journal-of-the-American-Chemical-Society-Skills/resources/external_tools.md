# External Tools and Resources for JACS Submissions

This document collects the databases, characterization platforms, deposition
services, and software commonly needed when preparing a chemistry manuscript for
the **Journal of the American Chemical Society (JACS)**. JACS is broad-scope, so
the relevant tools depend on whether your work is organic, organometallic,
inorganic, catalysis, materials, physical, analytical, or biological chemistry.

> Always confirm current requirements, formats, and deposition policies on the
> official ACS author page for JACS before submitting; specifics change over time.

## 1. Structure deposition and persistent identifiers

| Resource | Use | Notes |
|----------|-----|-------|
| CCDC / Cambridge Structural Database (CSD) | Deposit single-crystal X-ray structures; obtain CCDC numbers | Cite CCDC deposition numbers in the SI/text; deposit CIFs before submission |
| ICSD | Inorganic crystal structures | For inorganic/extended solids |
| Protein Data Bank (PDB) | Macromolecular / protein–ligand structures | For biological chemistry; obtain PDB ID |
| BMRB | Biomolecular NMR data | For biomolecular NMR assignments |
| ORCID | Author identifier | Increasingly expected; link in Paragon Plus |
| Crossref / DOI | Cite datasets and prior work | Use DOIs for data and software citations |

## 2. Characterization platforms (data you must report)

| Technique | Typical instrument | What JACS expects reported |
|-----------|--------------------|----------------------------|
| NMR (¹H, ¹³C{¹H}, and as needed ¹⁹F, ³¹P, 2D) | 300–800+ MHz spectrometers | Solvent, field, chemical shifts (δ, ppm), multiplicity, J (Hz), integration; copies of spectra in SI |
| HRMS | ESI / APCI / EI / MALDI-TOF, Orbitrap, FT-ICR | Ion formula, calcd vs found m/z, ionization mode |
| IR | FT-IR (ATR or transmission) | Key diagnostic bands (cm⁻¹) |
| UV-vis / fluorescence | Diode-array / scanning spectrophotometer | λmax, ε, emission λ, quantum yield method |
| Elemental analysis (CHN(S)) | Combustion analyzer | calcd vs found %; an accepted purity criterion |
| HPLC / GC | Reversed/normal phase, chiral columns | Purity %, ee/dr, method (column, eluent, flow, detector) |
| Single-crystal XRD | Diffractometer + software (below) | Crystal data table, R factors, CCDC number, CIF |
| PXRD | Powder diffractometer | Phase ID, indexing for solids/materials |
| Microscopy | SEM / TEM / AFM / STM | Scale bars, sample prep, representative + statistics |
| Surface/composition | XPS, EDX, TGA, BET, ICP-MS/OES | As appropriate for materials/physical work |
| Electrochemistry | Potentiostat (CV, DPV, bulk electrolysis) | Reference electrode, scan rate, electrolyte, vs Fc/Fc⁺ |

## 3. Crystallography software

- Data reduction / solution / refinement: **SHELX (SHELXT / SHELXL)**, **OLEX2**, **WinGX**, **CRYSTALS**.
- Validation: **checkCIF/PLATON** (run before deposition; resolve A/B-level alerts or justify them).
- Visualization: **Mercury** (CCDC), **ORTEP**, **VESTA** (extended solids), **PyMOL** (macromolecules).

## 4. Computational / theory tools (when mechanism or properties are computed)

| Tool | Use |
|------|-----|
| Gaussian, ORCA, Q-Chem, NWChem | DFT/ab initio energies, optimized geometries, TS searches |
| VASP, Quantum ESPRESSO, CP2K | Periodic/solid-state and surface DFT |
| GROMACS, AMBER, NAMD | Molecular dynamics |
| GaussView, Avogadro, VMD, Multiwfn | Building inputs / analyzing wavefunctions |
| Report | Functional, basis set/pseudopotentials, solvation model, software version; provide optimized coordinates (xyz) in SI |

## 5. Drawing and figure preparation (ACS style)

- **ChemDraw** is the de facto standard for structures, schemes, and reaction figures; use ACS document settings for bond length, font, and line weight.
- Spectra/plots: **OriginPro**, **MestReNova** (NMR processing and export), **Igor Pro**, **Matplotlib**, **ggplot2**.
- Figure assembly: **Adobe Illustrator**, **Inkscape** (vector preferred); export at the resolution ACS specifies for the figure type.
- Keep a single consistent color palette; ensure readability in grayscale and for color-vision deficiency.

## 6. Reference management and ACS citation style

| Tool | Notes |
|------|-------|
| Zotero | Free; install the ACS / *JACS* citation style (CSL) |
| EndNote | ACS output styles bundled; verify against current ACS guidelines |
| Mendeley / Papers | ACS style available |

JACS follows the **ACS numbered citation style** (superscript numbers; references in citation order). Use the *ACS Style Guide* conventions for author lists, abbreviated journal titles, and DOIs.

## 7. Submission system and manuscript prep

- **ACS Paragon Plus** is the submission portal for JACS.
- Manuscript: ACS provides Word and LaTeX templates; main text + a separate **Supporting Information** PDF + CIFs.
- Graphics: a **Table of Contents (TOC) / abstract graphic** is required; follow ACS size and content rules.
- Cover letter: required; states the advance and why it fits JACS (see `jacs-cover-letter`).

## 8. Reproducibility and integrity

1. Report procedures so that yields, conditions, ee/dr, and spectra are reproducible from the text alone.
2. Keep raw data (FIDs, chromatograms, diffraction frames) archived; editors/referees may request them.
3. Disclose all reagents, sources, and any safety hazards (pyrophoric, peroxide-forming, toxic, high-pressure).
4. Follow ACS ethical guidelines: no image manipulation beyond uniform adjustments, full author/conflict disclosure, and proper data availability statements.

## 9. Useful links (verify currency)

| Site | Purpose |
|------|---------|
| https://pubs.acs.org/journal/jacsat | JACS journal home |
| ACS Paragon Plus | Manuscript submission |
| ACS Author Guidelines (JACS) | Scope, formats, characterization and SI policy |
| https://www.ccdc.cam.ac.uk | Crystal-structure deposition (CCDC) |
| ACS Style Guide | Citation and nomenclature conventions |
| ORCID.org | Author identifiers |
