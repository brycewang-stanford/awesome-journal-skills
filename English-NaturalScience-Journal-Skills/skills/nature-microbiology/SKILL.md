---
name: nature-microbiology
description: Use when targeting Nature Microbiology (Nat Microbiol) or deciding whether a microbiology or microbial-ecology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Microbiology (nature-microbiology)

## Journal positioning

Nature Microbiology is Springer Nature's specialist journal for microbiology and microbial ecology in the broadest sense, covering bacteria, archaea, viruses, fungi, and protozoa across basic science, host-microbe interactions, environmental microbiology, and the microbiome. The journal requires a conceptual advance that moves the field — a new mechanism, a principle of microbial biology with broad implications, or a discovery that shifts understanding of a host-pathogen relationship or a microbial community process. Descriptive microbiology, incremental strain characterization, and applied microbiological improvements without mechanistic insight are out of scope. The readership spans microbiologists, virologists, infectious disease biologists, and microbial ecologists; papers must be written for this full community, not just specialists in one pathogen. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature Nature Microbiology site.

## When to trigger

- The author names Nature Microbiology as the target venue for a microbiology, virology, or microbial-ecology study.
- A host-pathogen, microbiome, or microbial-mechanism paper needs evaluation against the Nature Microbiology significance bar versus Cell Host & Microbe, Nature Immunology, or eLife.
- The author is deciding between Nature Microbiology and a more clinical venue (Lancet Infectious Diseases) for a study combining mechanism with epidemiological or clinical significance.
- The author needs Nature Microbiology's desk-reject criteria and a credible alternative-venue list.

## Scope & topic fit

- Mechanism of microbial pathogenesis: virulence factors, toxin action, immune evasion strategies, and antimicrobial resistance mechanisms — where the molecular or cellular mechanism is the advance.
- Virus biology: viral replication mechanisms, host-receptor interactions, immune antagonism, viral evolution and phylodynamics with mechanistic insight.
- Microbial physiology and genetics: gene regulation, metabolism, stress responses, biofilm formation, sporulation — where mechanistic depth is the contribution.
- Host-microbe interactions beyond classical infection: commensalism, symbiosis, colonization resistance, and the mechanisms by which microbes influence host physiology.
- Microbiome and microbial ecology: community-level mechanisms, microbiome-host signaling, metabolite-mediated interactions — when mechanism or principle is clear, not just compositional description.
- Antimicrobial resistance mechanisms and evolution: horizontal gene transfer, mobile genetic elements, mechanisms of drug action and resistance — with broader evolutionary or clinical significance.

## Method & evidence bar

- Mechanistic claims require direct experimental validation in the relevant biological context: cell culture, organoid, animal model, or clinical sample — not purely in vitro biochemistry without cellular corroboration.
- Microbiome studies that rely solely on 16S amplicon sequencing without mechanistic follow-up or metagenomic validation rarely clear the Nature Microbiology bar.
- Viral phylodynamics and evolutionary analyses must use current model-based inference with uncertainty quantification; sampling-bias awareness is expected for clinical sequences.
- Animal models must be appropriate for the pathogen and the claim; primary human-cell or ex vivo data add translational credibility.
- Data deposition: genomes and sequences in NCBI/ENA, metagenomes in SRA, structures in PDB/EMDB; code for computational analyses must be publicly available.
- A Nature Life Sciences Reporting Summary is required; biosafety and ethics declarations for work with pathogens, human samples, and animal models are mandatory.

## Structure & house style

- Articles are the primary format; Letters (shorter) may exist — re-check current article-type options on the live site.
- The title should convey the biological advance, not the pathogen or technique: "Mechanism of X immune evasion in Y pathogen" beats "Characterization of a Y pathogen protein."
- The abstract must make the conceptual advance accessible to all Nature Microbiology readers — not just specialists in the focal pathogen; jargon must be defined or avoided.
- Extended Data carries additional supporting experiments; Supplementary Information holds secondary technical materials, large datasets, and code.
- A Nature Reporting Summary (Life Sciences) is required; biosafety level and ethics/IRB approval information must be documented.
- Methods must be sufficiently detailed for replication; pathogen strains, cell lines, and animal model details should follow repository/registration standards.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Nature Microbiology author guidelines" and follow the current Springer Nature version.
- Re-check article-type definitions and length/figure limits; confirm current Abstract format (unstructured, character-limited).
- Re-check data-deposition requirements for sequence data, metagenomic data, and structural data; confirm accession-number provision before acceptance.
- Re-check the Life Sciences Reporting Summary, biosafety declarations, ethics and IRB approval documentation, animal-use reporting, and dual-use research of concern (DURC) policy for pathogen studies.
- Confirm competing-interests and funding disclosures, AI-use policy, and preprint policy (bioRxiv posting is generally supported).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the advance in microbiology — what principle or mechanism now understood differently by microbiologists generally?
- [ ] The significance is legible to a microbiologist who does not work on this pathogen, host, or environment.
- [ ] Mechanistic claims are validated in a biologically relevant context — not only in vitro reconstitution.
- [ ] Biosafety, ethics, and DURC considerations are documented; animal model choice is justified.
- [ ] Sequence and genomic data are deposited; code is available in a public repository.
- [ ] Reporting Summary and data/code availability statements are prepared.

## Common desk-reject triggers

- A descriptive microbiology study: new species description, strain characterization, or epidemiological surveillance without mechanistic or conceptual advance.
- A microbiome paper that reports 16S compositional data without mechanism, with weak causal inference, or without functional validation of the key finding.
- A study whose significance is primarily clinical (treatment outcomes, drug trial) rather than mechanistic microbiology: better suited to `the-lancet-infectious-diseases` or a clinical specialty journal.
- An antimicrobial resistance paper that maps resistance genes without illuminating the evolutionary mechanism or the molecular basis of resistance.
- A single-pathogen study whose conclusions are too organism-specific to carry meaning for microbiologists working on other systems.

## Re-routing decision

- Host-pathogen mechanism with strong immunology component: `nature-immunology` or `cell-host-and-microbe` (Cell Press, host-pathogen mechanism focus).
- Clinical significance alongside mechanism (outbreak, trial, epidemiology): `the-lancet-infectious-diseases` or `science-translational-medicine`.
- Microbial evolution and phylogenomics as primary focus: `molecular-biology-and-evolution`.
- Microbial ecology/microbiome with ecological principles: `nature-ecology-and-evolution`.
- Solid mechanistic virology or bacteriology below the Nature Microbiology novelty bar: eLife (`elife`), Cell Host & Microbe (`cell-host-and-microbe`) if host-microbe focus.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Microbiology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the microbial mechanism/advance — in relevant biological context — clear the Nature Microbiology bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / sequence deposition / Reporting Summary / biosafety/DURC / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
