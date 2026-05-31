---
name: physical-review-letters
description: Use when targeting Physical Review Letters (PRL) or deciding whether a physics manuscript fits this Letter-format, broad-importance venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Physical Review Letters (physical-review-letters)

## Journal positioning

Physical Review Letters is the APS flagship Letters journal and the premier rapid-communication venue across all of physics. Every accepted paper must satisfy two simultaneous editorial criteria: it must be important enough to interest physicists working in fields other than the author's own subfield, and it must report a result of sufficient immediacy to justify the Letter format. The length limit is a permanent structural gate of the journal's identity — not a soft recommendation — and authors must re-check the current official limit before preparing a manuscript. PRL is genuinely cross-subfield: a condensed-matter paper that is relevant only to condensed-matter readers will be redirected regardless of its technical quality.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the APS site and the Physical Review Letters submission system.

## When to trigger

- The author is targeting PRL for a concise result with claimed broad physics significance.
- A manuscript has been rejected from Nature/Science and the author is deciding between PRL and a Physical Review subfield journal (PRB, PRD, PRC, PRE).
- A result is complete and timely but the author is unsure whether it clears PRL's cross-subfield-significance bar versus being appropriate for `physical-review-b`, `physical-review-d`, or `prx-quantum`.
- The author needs PRL's length-gate and significance heuristics before beginning the manuscript.

## Scope & topic fit

- Fundamental results across all subfields of physics: condensed matter, atomic/molecular/optical, high-energy/particle, nuclear, gravitation, astrophysics, plasma, biological physics, quantum information — when the result has implications beyond the parent subfield.
- Experimental discoveries and precise measurements that shift paradigms or resolve long-standing controversies with broad physics relevance.
- Theoretical results that introduce new physical concepts, symmetries, or exact solutions with applicability across contexts.
- Quantum information and quantum technology results when the physics significance is broadly articulable (for narrower QIS focus, `prx-quantum` may be more appropriate).
- Cross-disciplinary physics — novel applications of physical methods or principles to biology, chemistry, or complex systems — when the physics insight is primary.

## Method & evidence bar

- The result must be complete and self-contained within the Letter; PRL does not accept work-in-progress or preliminary reports that will be followed by a longer paper at the same journal.
- Experimental papers require full statistical rigor: error bars, systematic-uncertainty budgets, and confidence in the quoted precision; single-event claims need extraordinary evidence.
- Theoretical papers must present either exact results or clearly bounded approximations with explicit validity conditions; numerical computation alone rarely clears the cross-subfield-significance bar.
- Supplemental Material is permitted for technical details that do not alter the completeness of the main text, but the main Letter must stand independently.
- Data and code availability expectations are increasing; re-check current APS data-sharing and reproducibility policies.

## Structure & house style

- The manuscript must fit within the current APS length limit — re-check the exact current limit (in Physical Review units) on the official PRL author guidelines page before drafting.
- The opening paragraph must immediately state the physical question, why it matters broadly, and what the main result is; PRL readers scan opening paragraphs to decide relevance outside their specialty.
- No subfield jargon in the abstract or opening paragraph; the significance must be articulable to a physicist working in a different APS division.
- A single focused Supplemental Material file carries derivations and extended data; it is peer reviewed but not part of the main text.
- Display items (figures, tables) must be minimal and maximally informative; PRL is not a venue for exhaustive parameter sweeps — show the key result cleanly.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Physical Review Letters author guidelines" and follow the current APS version; pay particular attention to the current length limit in manuscript units.
- Re-check article-type options (Letter vs. Rapid Communication legacy conventions), abstract format (single paragraph, no display equations), figure count and resolution requirements.
- Re-check the Supplemental Material policy: what is permitted there vs. what must appear in the main text.
- Re-check APS data/code availability and sharing policies, copyright transfer or open-access licensing options, and the preprint policy (APS generally supports arXiv posting).
- Confirm the cover letter explains cross-subfield significance explicitly — editors use it to assess the PRL significance bar before assigning referees.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] Can the main result be explained in one sentence to a physicist from a different APS division? If not, this is likely a subfield journal paper.
- [ ] The manuscript fits within the current official length limit — verify the number on the APS site, not from memory or a colleague's previous submission.
- [ ] The opening paragraph states the broad physics question and significance without subfield jargon.
- [ ] All error bars, uncertainty budgets, and statistical claims meet current precision standards for the measurement type.
- [ ] The Supplemental Material contains only supporting detail; the main Letter is fully self-contained.
- [ ] The cover letter explicitly argues cross-subfield importance.

## Common desk-reject triggers

- A technically correct but subfield-specific result that would interest only specialists in one APS division; editors desk-reject these routinely regardless of quality.
- Manuscript length exceeding the current limit — this is a hard gate and editors return papers over-length without review.
- An abstract or introduction written in subfield notation that non-specialists cannot parse; signals the broad-significance criterion cannot be met.
- Work presented as preliminary, with a companion full article promised elsewhere; PRL requires self-contained completeness.
- A result that is an incremental extension of prior work rather than a qualitatively new physical insight.

## Re-routing decision

If the result is excellent but primarily of subfield interest: condensed matter / materials → `physical-review-b`; particles / gravitation / cosmology → `physical-review-d`; quantum information / quantum technology (high impact, cross-subfield) → `prx-quantum`. For high-impact results that need more space to develop than PRL allows and span subfields, `physical-review-x` (open access, longer format, high significance bar) is the natural alternative. For results with a broad non-specialist physics narrative, `nature-physics` targets the same cross-subfield breadth with a different editorial culture.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Physical Review Letters
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result clear PRL's cross-subfield importance + completeness bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <current length limit / Supplemental Material policy / abstract format / data sharing / cover letter>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
