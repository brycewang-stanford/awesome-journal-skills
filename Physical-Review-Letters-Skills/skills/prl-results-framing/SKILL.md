---
name: prl-results-framing
description: Use when a Physical Review Letters result is correct but its central claim and broad significance are not yet sharp. Structures the one-claim narrative; does not run analysis or design figures.
---

# PRL Results Framing (prl-results-framing)

## When to trigger

- You have the data/derivation but the "so what" is fuzzy
- The draft reads like a chronological lab report, not a single argument
- You have several findings and have not chosen the headline one
- The opening paragraph buries the result under background
- `prl-scope-fit` returned PRL but flagged the breadth framing as weak

## The one-claim discipline

A Letter makes **one** central claim. Everything else is support. Decide the headline result first; demote the rest to corroboration or to Supplemental Material.

- **Primary claim** — the single sentence the title and abstract both encode.
- **Supporting claims** — at most two, and only if they reinforce the primary one.
- **Everything else** — context, controls, extended sweeps → Supplemental Material (see `prl-supplementary`).

If you have two equally important claims, you likely have two papers, or one belongs in a specialized PR journal.

## The opening (first paragraph carries the gate)

PRL openings are short and front-load significance. A reliable four-move pattern:

1. **The general physics context** — one or two sentences a non-specialist physicist understands.
2. **The open question / gap** — what was unknown, unresolved, or impossible before.
3. **What this Letter shows** — the central claim, stated plainly, ideally with the key number or qualitative surprise.
4. **Why it matters broadly** — the consequence for a wider community.

Do not spend the first half-column on a literature tour. The result should appear within the first paragraph or two.

## Framing decision branches

| Symptom                                              | Move                                                        |
|------------------------------------------------------|-------------------------------------------------------------|
| Two co-equal headline results                         | Split, or demote one to support / SM                        |
| Result stated only operationally ("we measured ...")  | Reframe as the physical conclusion it implies               |
| Significance asserted, not shown                      | Tie significance to a concrete prior belief it changes      |
| Background dominates the opening                      | Cut to 2–3 sentences; move detail to body or SM             |
| Abstract lists methods before findings                | Reorder: finding first, method as the enabling clause       |

## Abstract craft

The abstract is a self-contained mini-Letter: context → what you did → what you found (with the key result) → why it matters. Lead with the finding, keep it short, avoid undefined acronyms, and make it readable by a physicist outside the subfield. APS imposes an abstract length limit — verify the current value.

## Checklist

- [ ] Exactly one primary claim, expressible in one sentence
- [ ] Title encodes the central result, not just the topic
- [ ] Opening reaches the result within ~1–2 paragraphs
- [ ] Significance is tied to a belief the result changes, not asserted
- [ ] Abstract leads with the finding and is intelligible out-of-subfield
- [ ] Supporting claims (≤2) genuinely reinforce the primary one
- [ ] Demoted material has a home in the body or SM

## Anti-patterns

- A "kitchen-sink" Letter that reports everything the project produced
- Operational framing ("we observe X") with no physical interpretation
- Significance claims that overreach beyond what the data support
- An abstract that is a methods summary rather than a result statement
- Saving the punchline for the conclusion (there is barely a conclusion in a Letter)

## Output format

```
【Primary claim】one sentence
【Title】encodes the result?  yes / fix
【Opening moves】context / gap / claim / significance — all present?
【Supporting claims】≤2, each justified
【Demoted to SM】list
【Abstract leads with finding】yes / fix
【Next】prl-methods (trust) or prl-figures (lead figure)
```

> Abstract and title norms are durable; verify the current abstract length limit on the official APS / PRL author page.
