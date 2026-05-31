---
name: inventiones-mathematicae
description: Use when targeting Inventiones Mathematicae (Invent. Math.) or deciding whether a pure mathematics manuscript fits this Springer venue. Encodes the journal's fit, framing, proof standard, house style, official-submission re-check, and desk-reject heuristics.
---

# Inventiones Mathematicae (inventiones-mathematicae)

## Journal positioning

Inventiones Mathematicae, published by Springer, is one of the world's leading research mathematics journals, alongside Annals of Mathematics and the Journal of the American Mathematical Society. It publishes significant original mathematics across all major areas of pure mathematics and is read by the global research mathematics community. The editorial standard is exceptional significance and full rigor: papers must deliver new theorems of broad mathematical importance, proved completely and presented with precision. Compared with Annals, Inventiones publishes at a slightly higher volume and across a wide range of pure-math fields, but the significance bar remains very high and most submitted manuscripts are declined.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer / Inventiones Mathematicae site and confirm current submission procedures.

## When to trigger

- The author is targeting Inventiones Mathematicae and wants to assess fit and significance level.
- A pure mathematics paper is strong but the author is calibrating whether Annals, Inventiones, or `journal-of-the-american-mathematical-society` is the right tier and field fit.
- An author wants to understand Inventiones' editorial culture and specific desk-reject risks.

## Scope & topic fit

- Algebraic geometry, number theory, and arithmetic geometry — historically among the strongest areas in Inventiones.
- Algebraic topology, differential geometry, and geometric analysis.
- Representation theory, Lie theory, and automorphic forms.
- Analysis, complex analysis, and harmonic analysis at the research frontier.
- Dynamical systems, ergodic theory, and mathematical physics at the rigorous-proof level.
- Combinatorics, probability theory, and logic when the result is of broad pure-mathematics significance.
- All areas are in scope; the determining criterion is significance and proof completeness, not sub-field.

## Method & evidence bar

- Complete, rigorous proof is the non-negotiable minimum: every theorem must be fully established in the paper; no deferred proofs, gaps, or "analogous arguments show."
- Significance: the result must be important to the broader research-mathematics community; work of interest only within a highly specialized sub-sub-field is unlikely to clear the editorial bar.
- Novelty of argument: papers that introduce new mathematical ideas, new structural insights, or new connections between areas are especially valued; computational verification without conceptual insight is generally not appropriate here.
- Precision in statements: theorems, lemmas, and corollaries must be stated with complete mathematical precision; hypotheses must be explicit.
- MSC classification must be accurate; incorrect or overly broad classification can impede referee assignment.
- arXiv posting is the standard practice; include the arXiv identifier in the submission.

## Structure & house style

- Standard mathematical paper structure: introduction (motivating the result, stating main theorems, outlining proof strategy), preliminary notation and known results, core argument sections, and optional appendix.
- The introduction must be written for a broad mathematical audience: the significance of the result and the key ideas of the proof should be legible to mathematicians outside the immediate specialty.
- Springer formatting requirements apply; re-check the current Inventiones Mathematicae style file and submission format on the Springer site.
- LaTeX is required; Springer provides a class file — use the current version from the official site.
- References must be complete; cite the published version where available, and include arXiv identifiers for preprints.
- No page limit as such; the paper should be as long as mathematical completeness requires, no shorter and no longer.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Check the current submission instructions on the Springer Inventiones Mathematicae page; submit via the designated editorial system.
- Use the current Springer/Inventiones LaTeX class file; do not submit in non-standard formats.
- Assign MSC primary and secondary codes.
- Post the paper on arXiv (standard practice) and include the arXiv identifier.
- Prepare a cover letter explaining the main result and its significance, and disclosing any conflicts with potential referees.
- Confirm no APC applies (Inventiones is a subscription journal; re-check current open-access options if needed).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the main theorem and its significance to research mathematics broadly.
- [ ] Every claim is fully proved; no gaps, unresolved cases, or deferred arguments.
- [ ] The introduction is written for a broad mathematical readership: the significance and proof strategy are clear without requiring full expertise in the sub-field.
- [ ] MSC codes are correctly assigned; arXiv version is posted or ready.
- [ ] The Springer/Inventiones LaTeX class file is used; formatting meets current requirements.
- [ ] An honest assessment has been made: is this result at the Inventiones significance level?

## Common desk-reject triggers

- A correct and solid paper judged by the board to fall below the significance level expected for Inventiones.
- A result that is important within a narrow specialty but lacks the cross-field resonance the editorial board values.
- Incomplete proof: any identifiable gap or unverifiable step will lead to rejection.
- A paper that is a long and technical generalization of a known result without a conceptually new idea or surprising conclusion.
- Introduction that is inaccessible to a broad mathematical audience, making it impossible for the editorial board to assess significance.

## Re-routing decision

Exceptional results at the highest significance level → `annals-of-mathematics`. AMS-published venue at comparable prestige → `journal-of-the-american-mathematical-society`. Strong but more specialized research mathematics → Duke Mathematical Journal, Geometric and Functional Analysis, Compositio Mathematica, or area-specific society journals. Applied mathematics or mathematical physics with numerical components → appropriate applied-math or mathematical-physics journals.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Inventiones Mathematicae
[Topic tags] <2–3 MSC areas>
[Method/evidence] <is the main theorem fully proved, conceptually novel, and broadly significant in pure mathematics?>
[Top risk] <the single most likely reason for rejection — usually significance level or proof gap>
[Official items to re-check] <submission system / Springer style file / MSC codes / arXiv / cover letter>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
