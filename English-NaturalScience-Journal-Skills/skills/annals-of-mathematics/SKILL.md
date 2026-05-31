---
name: annals-of-mathematics
description: Use when targeting Annals of Mathematics (Ann. of Math.) or deciding whether a pure mathematics manuscript fits this Princeton/IAS venue. Encodes the journal's fit, framing, proof standard, house style, official-submission re-check, and desk-reject heuristics.
---

# Annals of Mathematics (annals-of-mathematics)

## Journal positioning

Annals of Mathematics, published by Princeton University and the Institute for Advanced Study, is widely regarded as the most prestigious journal in pure mathematics. It publishes only results that are genuinely exceptional in significance and depth — theorems that solve long-standing open problems, introduce fundamentally new methods that reshape a field, or deliver a result whose importance extends well beyond its immediate area. The bar for acceptance is correspondingly severe: excellent mathematics that is merely interesting or technically difficult is not sufficient. Refereeing is slow and exacting; a paper may be under review for one to two years or longer.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Annals of Mathematics site (annals.math.princeton.edu) and confirm submission procedures.

## When to trigger

- The author is considering submitting to Annals of Mathematics and wants to assess significance and fit.
- A paper resolves a major open problem or introduces a method of likely lasting importance and the author is choosing among Annals, `inventiones-mathematicae`, and `journal-of-the-american-mathematical-society`.
- A colleague or advisor suggests Annals as a potential venue and the author wants to calibrate expectations.
- The author needs to understand Annals' editorial culture and common reasons for rejection before proceeding.

## Scope & topic fit

- Pure mathematics across all major areas: algebra, algebraic and differential geometry, topology, number theory, analysis, probability theory, combinatorics, dynamical systems, mathematical physics.
- Proofs of outstanding open problems that have resisted solution for a significant period or that the community regards as milestones.
- Introduction of new mathematical structures, techniques, or frameworks whose impact reaches across multiple sub-areas.
- Results that are broadly significant within mathematics — not just within a highly specialized sub-community — are preferred over narrowly specialized advances, however technically deep.
- Survey or expository work is not published; the contribution must be primary research delivering new theorems.

## Method & evidence bar

- The primary standard is mathematical correctness: every claim must be fully proved; no partial results, conditional results (unless conditionality is the explicit contribution), or proof sketches in place of complete proofs.
- Significance is judged by the editorial board's assessment of mathematical importance, not by citation counts, applications, or the fame of the problem alone.
- Novelty of technique matters: a proof that introduces a powerful new idea even while solving a known result may be preferred over a brute-force argument for a harder result.
- Exposition quality is part of the bar: arguments should be presented with clarity and mathematical precision so that expert referees can verify correctness; obscure or unnecessarily compressed proofs slow review and raise doubts.
- MSC (Mathematics Subject Classification) codes must be assigned correctly; this signals scope and assists in referee assignment.
- arXiv posting is standard practice for Annals submissions; most papers appear on arXiv before or contemporaneously with submission.

## Structure & house style

- There is no imposed structural template beyond mathematical convention: introduction (setting context, stating results, outlining the proof strategy), preliminary material, core proof sections, and optionally an appendix for technical lemmas.
- The introduction is critical: it should state the main result precisely (not just informally), explain its significance in terms accessible to a broad mathematical audience, and sketch the key ideas of the proof — this is read by the editorial board before a referee is assigned.
- LaTeX is standard; Annals uses its own style file — re-check current formatting requirements on the submission site.
- References must be complete and correctly formatted; cross-references to recent arXiv preprints should include stable identifiers.
- Length is determined by mathematical necessity; there is no page limit as such, but unnecessarily long papers attract scrutiny; concise, complete arguments are valued.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Check the current submission instructions at annals.math.princeton.edu; submission is by email or through the indicated system — re-verify the current procedure.
- Assign MSC primary and secondary classification codes.
- Post to arXiv (or confirm prior posting) with the arXiv identifier ready to include in correspondence.
- Prepare a cover letter that states the main result, its significance, and an honest assessment of who the appropriate referees are (and who should be excluded due to conflicts).
- Confirm that all co-authors have approved the submission.
- There is no APC; confirm no fee is required under current editorial arrangements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the main theorem and why it is important to mathematics broadly, not only to the immediate sub-field.
- [ ] Every claim in the paper is fully proved; no gaps, sketches, or "it can be shown" in place of proof.
- [ ] The introduction states the main result precisely, explains its significance, and outlines the key proof ideas.
- [ ] The paper is posted or ready to post on arXiv with correct MSC codes.
- [ ] An honest assessment has been made: is this result truly at the Annals significance level, or would `inventiones-mathematicae` or `journal-of-the-american-mathematical-society` be a more appropriate first submission?
- [ ] Formatting uses the current Annals style file and references are complete.

## Common desk-reject triggers

- A correct, technically demanding paper that is judged as not exceptional in significance — the editorial board desk-rejects the large majority of submissions on significance grounds alone.
- A result that is important in a narrow sub-field but does not have the mathematical breadth of interest expected for Annals.
- An incomplete proof: any identifiable gap, unresolved case, or unjustified claim will lead to rejection.
- A paper that is an incremental extension of a known technique or result, however correct, without a conceptually new idea.
- Introduction that does not make the significance of the result clear to mathematical generalists on the editorial board.

## Re-routing decision

Excellent mathematics at a slightly narrower or more specialized level → `inventiones-mathematicae` or `journal-of-the-american-mathematical-society`. High-quality research mathematics across all fields → `inventiones-mathematicae`. AMS-published flagship with comparable prestige → `journal-of-the-american-mathematical-society`. Combinatorics, probability, or applied-adjacent pure mathematics may also consider venue-specific society journals (Duke Mathematical Journal, Geometric and Functional Analysis, etc.).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Annals of Mathematics
[Topic tags] <2–3 MSC areas>
[Method/evidence] <is the main theorem fully proved, novel in technique, and of exceptional significance?>
[Top risk] <the single most likely reason for rejection — usually significance level>
[Official items to re-check] <submission procedure / MSC codes / arXiv posting / cover letter / style file>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
