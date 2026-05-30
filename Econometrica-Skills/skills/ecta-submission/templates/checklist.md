# Econometrica Pre-Submission Checklist

> Verify all volatile specifics (portal URL, submission fee, member discount, the current
> Data and Code Availability Policy, formatting and blinding rules) on the official journal
> site before relying on them. The items below are durable norms.
> https://www.econometricsociety.org/publications/econometrica

## 1. Contribution and fit

- [ ] Contribution stated as a theorem or estimator-plus-asymptotics, not as an application
- [ ] Result holds on the most general natural class, not just a parametric example
- [ ] Clear economic / behavioral / inferential payoff stated
- [ ] Honest placement: this is Econometrica-deep (method/theorem), not general-interest-applied

## 2. Manuscript structure

- [ ] Introduction reaches the (informal) main result quickly
- [ ] Definitions, assumptions numbered and displayed
- [ ] Theorems / Propositions / Lemmas numbered consistently
- [ ] Each main result followed by a short interpretation paragraph
- [ ] Cross-references by number, not "above / below"
- [ ] Conclusion is brief

## 3. Proofs

- [ ] Every proof complete — no "easy to see," no skipped step
- [ ] Proof sketches in the body; full proofs in the Online Appendix if long
- [ ] Every regularity condition used in a proof appears as a numbered assumption
- [ ] No CLT / fixed-point / limit theorem invoked whose hypotheses are unverified
- [ ] Existence and uniqueness (or set characterization) both addressed
- [ ] The novel / hard step is given in full

## 4. Identification and asymptotics (methods papers)

- [ ] Parameter defined as a population functional, separate from the estimator
- [ ] Identification conditions numbered; point vs. partial identification stated
- [ ] Rate of convergence derived; limiting distribution derived
- [ ] Asymptotic variance + a consistent estimator provided
- [ ] Pointwise vs. uniform asymptotics addressed; weak-identification robustness considered

## 5. Finite-sample / Monte Carlo evidence

- [ ] At least one favorable and one boundary / adverse design
- [ ] Multiple sample sizes showing the asymptotics engage
- [ ] Comparison against the natural competitor method(s)
- [ ] Number of replications stated; Monte Carlo error small / reported
- [ ] Size, power (size-adjusted), coverage, length reported as relevant
- [ ] Tuning-parameter sensitivity examined

## 6. Tables and figures

- [ ] Each exhibit self-contained (design, n, replications, nominal level, per-column meaning)
- [ ] Three-line / booktabs style; no vertical rules or shading
- [ ] Figures fully labeled; vector format; readable in grayscale
- [ ] Every number in the text matches the tables exactly

## 7. References

- [ ] Every in-text citation in the reference list and vice versa
- [ ] Theorem-level results cited precisely where a proof depends on them
- [ ] Foundational and contemporaneous work cited fairly
- [ ] Reference style matches the journal's current requirement

## 8. Anonymization

- [ ] No author-identifying content in the manuscript body
- [ ] Self-citation in the third person
- [ ] Acknowledgments / funding removed from the anonymized version
- [ ] File metadata scrubbed of author names

## 9. Online / Supplementary Appendix

- [ ] Full proofs of all results not fully proven in the body
- [ ] Complete Monte Carlo design and additional simulations
- [ ] Additional theorems / extensions referenced from the body
- [ ] Self-contained and cross-referenced from the main text

## 10. Data and Code Availability Policy

- [ ] Replication package reproduces from a clean checkout
- [ ] Monte Carlo tables reproduce bit-for-bit (seeds recorded)
- [ ] Single master script (`run_all`) regenerates every exhibit
- [ ] Environment pinned (software versions + dependencies)
- [ ] Data provenance / access documented; restricted data handled per agreement
- [ ] Data-availability statement prepared as required
- [ ] Verified against the current policy text and deposit location

## 11. Submission portal (Editorial Express)

- [ ] Account ready; correct portal URL (verify on site)
- [ ] Main manuscript + Online Appendix uploaded as specified
- [ ] Abstract, JEL codes, keywords entered accurately
- [ ] Correct field / classification chosen for co-editor routing
- [ ] Qualified, conflict-free referee suggestions provided
- [ ] Submission fee handled; member discount applied if eligible (verify amounts)
