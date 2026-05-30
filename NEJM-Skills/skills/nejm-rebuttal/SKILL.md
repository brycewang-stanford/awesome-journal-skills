---
name: nejm-rebuttal
description: Use after NEJM reviews arrive — often including a dedicated statistical reviewer and an editor letter — to triage the decision, answer statistical comments rigorously, and draft a point-by-point response that quotes each comment, the response, and the revised manuscript text. Do not run before the main text is actually revised.
---

# Response to Reviewers (nejm-rebuttal)

## When to trigger

- A decision letter arrives (reject / reject-but-resubmit / major or minor revision).
- You have reviewer comments — frequently including a **statistical reviewer** — and need a strategy.
- A revision is drafted and you need the point-by-point response letter.

## Step 0: read the editor's letter first

The **editor's** framing outranks individual reviewers. Identify:

- The decision type and whether a new review round is implied.
- Which concerns the editor **emphasizes** (these are load-bearing — address fully).
- Any **deal-breaker** the editor names (e.g., "the primary analysis must be ITT", "registration discrepancy must be resolved").

> A "reject but would consider a new submission" is an invitation gated on the deal-breaker. Do not treat it as a flat reject, and do not under-deliver.

## The statistical reviewer is special

NEJM commonly assigns a **statistician** whose comments carry decisive weight and require **rigorous statistical responses**, not prose:

- Re-run analyses exactly as requested (ITT vs per-protocol, multiplicity adjustment, alternative models, sensitivity analyses) and **show the numbers** with CIs.
- If asked about subgroup over-interpretation, report the **interaction test** and reframe the subgroup as exploratory.
- For missing data, demonstrate robustness (e.g., results under multiple imputation vs complete case).
- Concede a methodological point with the corrected analysis rather than defending a weaker one.
- Loop in `nejm-statistics` to make sure every re-analysis is reported to NEJM's standard.

## Triage every comment into 4 buckets

| Bucket             | Action                                                            |
|--------------------|------------------------------------------------------------------|
| **Do** (fair, feasible) | Make the change; show it; quote the new text/table/figure.  |
| **Do-partial**     | Do what's feasible; explain the boundary with evidence.          |
| **Defend** (wrong/out of scope) | Push back respectfully, with data/citations — not assertion. |
| **Defer** (future work) | Acknowledge; add a sentence to the text; don't over-promise. |

Most rejections-on-revision come from **silently skipping** a load-bearing comment or **defending** when a re-analysis was actually needed.

## Response-letter format

For each comment:

```
Reviewer N, Comment k: <verbatim quote of the reviewer>

Response: <what we did / our reasoning>. <Evidence: re-analysis with effect + 95% CI,
new Table/Fig., updated CONSORT numbers.>
Changes: "<quoted new manuscript text>" (p. X, lines Y–Z; Table/Fig. update).
```

- Open with a short thank-you and a 3–4 line summary of the **major changes** across the revision.
- Quote each comment verbatim; never paraphrase in a way that softens the reviewer's point.
- **Quote the new manuscript text** so the editor and statistician can verify without hunting.
- Use a consistent visual convention (reviewer text plain, response indented, manuscript quotes in italics).

## Over-claiming and causation watch (NEJM-specific)

If a reviewer says the conclusion outruns the data — or that causal language is used on observational data — this is the **most dangerous** comment for a clinical paper. Either add the evidence or **narrow the claim** in the abstract Conclusions, title, and Discussion, and **soften causal verbs to associations** where appropriate. Be honest about limitations; a candid limitations paragraph builds credibility. Re-run `nejm-fit` if the narrowed claim weakens the practice-changing case.

## Output format

```
【Decision type】 reject / reject-resubmit / major / minor
【Editor's load-bearing concerns】 [...]
【Deal-breaker】 ... → plan to resolve
【Statistical reviewer comments】 [...] → re-analyses planned (with CIs)
【Comment triage】 Do [...] / Do-partial [...] / Defend [...] / Defer [...]
【Claim integrity】 over-claiming / causal-language narrowing needed? (re-check nejm-fit)
【Response letter】 drafted point-by-point with quoted changes
```

## Anti-patterns

- **Do not** silently skip a comment the editor emphasized.
- **Do not** answer a statistical reviewer with prose where a re-analysis with CIs is required.
- **Do not** defend causal language on observational data — narrow it to association.
- **Do not** over-promise future work to dodge a needed re-analysis.
- **Do not** draft the response before the manuscript is actually revised.
