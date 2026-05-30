---
name: ecta-submission
description: Use when running the final pre-submission preflight for an Econometrica manuscript via Editorial Express — manuscript assembly, Online/Supplementary Appendix, anonymization, references, fee, and Data and Code Availability Policy compliance.
---

# Submission Preflight (ecta-submission)

## When to trigger

- "Submitting tomorrow"; final check before clicking submit on Editorial Express
- Unsure how to split the body vs. the Supplementary / Online Appendix
- Unsure which files and declarations the portal needs

> Verify all volatile specifics — portal URL, submission fee, Econometric Society member
> discount, the current Data and Code Availability Policy, and formatting rules — on the
> official journal site before submitting. The items below are durable norms; the figures are not.

## Pre-submission checklist

### Manuscript assembly

- [ ] Main text states the contribution / informal main theorem early
- [ ] Definitions and assumptions are numbered, displayed objects
- [ ] Theorems numbered consistently; cross-references by number
- [ ] Proof sketches in the body; **full proofs in the Supplementary / Online Appendix** if long
- [ ] Online Appendix carries full proofs, Monte Carlo detail, and additional results
- [ ] Every number in the text matches the tables
- [ ] Abstract and JEL codes present; keywords appropriate

### Online / Supplementary Appendix

- [ ] Full, complete proofs of every result not proven in full in the body
- [ ] Complete Monte Carlo design and any additional simulations
- [ ] Additional theorems / extensions referenced from the body
- [ ] Appendix is self-contained and cross-referenced from the main text

### Anonymization (double-blind norms)

- [ ] No author-identifying content in the manuscript body
- [ ] Self-citation phrased in the third person ("X (2020) shows"), not "our earlier work"
- [ ] Acknowledgments / funding removed from the anonymized manuscript
- [ ] File metadata scrubbed of author names
- [ ] (Confirm the journal's current blinding policy — verify on site)

### References

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Theorem-level results cited precisely (which theorem, not just the paper) where the proof relies on them
- [ ] Reference style matches the journal's current requirement
- [ ] Foundational and contemporaneous work cited fairly

### Data and Code Availability Policy

- [ ] Replication package built and reproduces from a clean checkout (see `ecta-replication-package`)
- [ ] Monte Carlo tables reproduce bit-for-bit (seeds recorded)
- [ ] Data provenance / access documented; restricted-data procedures handled
- [ ] Data-availability statement prepared as the policy requires
- [ ] Verified against the **current** policy text and deposit location on the journal site

### Fee and member status

- [ ] Submission fee handled; Econometric Society member discount applied if eligible (verify current amounts)
- [ ] Any waiver process checked if applicable

## Editorial Express operation

- Submit via Editorial Express (verify current URL via the journal site).
- Upload the main manuscript and the Supplementary / Online Appendix as the portal specifies.
- Enter abstract, JEL codes, and keywords accurately.
- Provide qualified, conflict-free referee suggestions (see `ecta-referee-strategy`).
- Choose the correct classification / field for routing to an appropriate co-editor.

## Anti-patterns

- Submitting with proofs only in the body and the Online Appendix not assembled
- Asymptotics in, Monte Carlo left for "the revision" — often a fast rejection
- A replication package that does not actually reproduce
- Self-citations that de-anonymize the manuscript
- Citing a survey where the proof depends on a specific theorem
- Trusting a stale fee / policy figure instead of verifying on the journal site

## Output format

```
【Body vs Appendix】proofs split correctly: yes/no
【Online Appendix assembled】yes/no — missing: [...]
【Anonymization】pass / fix: [...]
【References】in/out consistent: yes/no
【Data & Code Policy】reproduces + statement ready: yes/no
【Fee/member discount】handled: yes/no (verify amounts)
【Next step】await decision / R&R → ecta-rebuttal
```

## Related resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check (manuscript, appendix, anonymization, proofs, simulations, references, replication, portal)
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — standard theory/methods manuscript skeleton (assumptions, theorems, proof sketches, Online Appendix)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — typesetting, symbolic/computation, and reproducibility toolchain
