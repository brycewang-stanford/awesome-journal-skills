---
name: journal-of-the-american-mathematical-society
description: Use when targeting Journal of the American Mathematical Society (JAMS) or deciding whether a pure mathematics manuscript fits this AMS flagship venue. Encodes the journal's fit, framing, proof standard, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of the American Mathematical Society (journal-of-the-american-mathematical-society)

## Journal positioning

The Journal of the American Mathematical Society (JAMS) is the flagship research journal of the American Mathematical Society, publishing the most important new mathematics across all areas of pure and applied mathematics. Together with Annals of Mathematics and Inventiones Mathematicae, it forms the top tier of general mathematics journals. JAMS publishes at a selective frequency, accepting only papers that its editorial board — drawn from across the mathematical spectrum — judges to be of the highest significance. It is an AMS publication, carries the AMS's institutional prestige, and is widely read by mathematicians across specialties who use it as a signal of landmark results.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AMS site (ams.org/journals/jams) and confirm current submission procedures.

## When to trigger

- The author is targeting JAMS and wants to assess fit, significance level, and submission norms.
- A mathematics paper is being considered for one of the top three general math journals and the author is choosing between JAMS, `annals-of-mathematics`, and `inventiones-mathematicae`.
- The author wants to understand AMS editorial culture, JAMS-specific norms, and desk-reject risks.

## Scope & topic fit

- All areas of pure mathematics: algebra, analysis, geometry, topology, number theory, combinatorics, probability, dynamical systems, logic.
- Applied mathematics and mathematical physics where the primary contribution is a new theorem or rigorous mathematical result.
- Results that are of broad interest across mathematics — the editorial board includes generalists and the paper must connect to the wider mathematical enterprise.
- Survey or expository papers are not within scope; all published content is primary original research delivering new theorems.
- Cross-area results that forge new connections between previously separate mathematical fields are especially valued.

## Method & evidence bar

- Full mathematical rigor: every theorem, proposition, lemma, and corollary must be completely and correctly proved; there are no exceptions for "standard" or "well-known" arguments — if needed, provide the argument or cite a specific complete reference.
- Significance, not just correctness: the result must be genuinely important to the mathematical community; the editorial board makes an affirmative judgment about mathematical importance, not merely a negative judgment about errors.
- Novelty of ideas: proof by application of known machinery to a new case, without novel mathematical insight, is not typically at the JAMS level; the argument should introduce something new to the toolkit or understanding of mathematics.
- Mathematical exposition must be precise: definitions must be complete, hypotheses stated explicitly, and notation consistent throughout.
- MSC codes must be accurate and assigned; arXiv preprint posting is strongly conventional.

## Structure & house style

- Standard mathematical structure: introduction (precise theorem statements, motivation, significance, proof outline), technical preliminaries, core proof sections, appendix if needed.
- The introduction must serve a dual purpose: convince the editorial board of significance on first reading, and orient specialist referees — balance is required between accessibility and precision.
- AMS LaTeX class file (amsart) is expected; re-check the current JAMS formatting requirements at ams.org/journals/jams/about.
- References follow AMS style (MathSciNet citation format preferred); include complete bibliographic information.
- arXiv identifier should be included in the submission when the paper has been posted; arXiv posting is the norm.
- Length is determined by the mathematics; JAMS papers range from short focused results to long comprehensive treatments.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Check ams.org/journals/jams for current submission instructions; submit via the AMS editorial system.
- Use the current AMS amsart class file and follow JAMS formatting guidelines.
- Assign MSC primary and secondary classification codes.
- Post to arXiv if not already done; note the arXiv identifier.
- Prepare a cover letter stating the main result, its significance, and potential referee suggestions (and conflicts).
- Confirm AMS ethical standards compliance (no duplicate submission, all authors consent).
- Check current AMS open-access options if applicable; JAMS is a subscription journal — verify current terms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the main theorem and why it is important to mathematics — both within its area and more broadly.
- [ ] Every stated result is completely proved in the paper; no gaps, "it can be shown," or implicit cases.
- [ ] The introduction states theorems precisely, motivates their significance, and outlines the key proof ideas for a broad mathematical audience.
- [ ] AMS amsart class file is used; MSC codes are correctly assigned; arXiv is posted.
- [ ] An honest self-assessment: does this result belong at the JAMS / top-three level, or is `inventiones-mathematicae` or a specialty journal more appropriate?
- [ ] Cover letter is prepared with a clear significance statement.

## Common desk-reject triggers

- A correct, technically solid paper that does not rise to the level of mathematical importance JAMS requires — significance desk-rejection is the modal outcome for strong papers.
- A narrow technical result important only within a specialized sub-community without broader mathematical resonance.
- An incomplete proof: any gap identified by the editorial board or referees will lead to rejection.
- A paper extending known methods to a new case without introducing a new mathematical idea or surprising result.
- An introduction that fails to communicate significance to non-specialists on the editorial board, preventing a positive significance assessment.

## Re-routing decision

Results at the very apex of mathematical significance → `annals-of-mathematics`. Equivalent significance level with Springer preference or particular area fit → `inventiones-mathematicae`. Excellent but more specialized pure mathematics → area-specific venues (Duke Mathematical Journal, Compositio Mathematica, Geometric and Functional Analysis, Transactions of the American Mathematical Society for broader/longer works). Applied mathematics heavy with computation → SIAM journals.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of the American Mathematical Society
[Topic tags] <2–3 MSC areas>
[Method/evidence] <is the main theorem completely proved, conceptually novel, and of broad mathematical importance?>
[Top risk] <the single most likely reason for rejection — usually significance level>
[Official items to re-check] <AMS submission system / amsart class file / MSC codes / arXiv / cover letter / ethics>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
