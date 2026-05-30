---
name: pnas-track
description: Use to choose the PNAS submission track — Direct Submission (standard, editor-assigned, peer reviewed) vs Contributed Submission (an NAS member communicates their own paper). Covers eligibility, the editor/member role, the discontinued and legacy tracks, and how to pick. Unique to PNAS.
---

# Submission Track Selection (pnas-track)

## Why this skill exists

The **submission track** is PNAS's signature feature and has **no equivalent at Science or Nature**. The track determines who handles the paper, who picks reviewers, and how the published article is labeled. Pick it early — it shapes the entire handling path. Do this right after `pnas-fit`.

## When to trigger

- You are about to start a PNAS submission and must choose a track.
- A co-author or collaborator who is a **member of the U.S. National Academy of Sciences (NAS)** offers to "communicate" or "contribute" the paper.
- You read "Contributed by …" or "Edited by …" on a PNAS paper and need to know what it means for yours.
- You are unsure whether the legacy "Communicated" or "Prearranged Editor" options still apply.

## The tracks

### (a) Direct Submission — the default for most authors

- **Standard route.** Anyone may submit. The manuscript is **assigned to an editorial board member / editor by PNAS**, who oversees independent peer review.
- No NAS member required. This is what most authors use and what `pnas-submission` defaults to.
- You may suggest editors and reviewers in the cover letter (`pnas-submission`), but the journal assigns the handling editor.

### (b) Contributed Submission — only via an NAS member

- An **NAS member** may **"contribute"** a paper they are an author on. The member acts as the communicating editor: they **arrange the review themselves**, typically securing **at least two qualified, independent reviewers**, and submit the reviews and the authors' responses along with the paper.
- **Strict limit:** an NAS member may contribute only a **small number of papers per year** (historically about **2 per member per year** — confirm the current cap in PNAS author guidelines).
- The member must be an author and is responsible for the integrity of the review they arrange; reviewers must be genuinely independent (no recent collaborators, no conflicts).
- Published articles are labeled **"Contributed by [Member]."**

### (c) Legacy / discontinued options

- **Prearranged Editor (PE):** historically, a non-member author could ask an NAS member to agree in advance to be the editor before submission, after which the paper went through PNAS's standard review. Availability has changed over time — **confirm whether this option currently exists** before relying on it.
- **"Communicated" submissions (third-party member relays a non-member's paper):** this older track was **discontinued** — do not plan around it.

## How to pick

| Situation | Track |
|-----------|-------|
| No NAS member among the authors | **Direct Submission** |
| An NAS-member author wants standard PNAS-run review | **Direct Submission** (member is just an author) |
| An NAS-member author wants to communicate and has not used up their annual quota, and can secure ≥2 independent reviewers | **Contributed Submission** (eligible) |
| You want the fastest/most controlled handling but have no eligible member | **Direct Submission** (Contributed is not available to you) |
| You are tempted by a legacy track | confirm it still exists; default to **Direct** |

> Contributed is a privilege of the member, bounded by the annual quota and by the independence requirement. It is **not** a way to dodge peer review — the reviews still happen and are submitted with the paper. If reviewer independence is in any doubt, use Direct Submission.

## What the label means to readers

The published article carries its track in the header — "Edited by …" for a Direct Submission handled by the assigned editor, or "Contributed by [Member]" for a Contributed paper. Reviewers, journalists, and downstream readers can see the route. A Contributed paper with weak member-arranged review attracts scrutiny; Direct Submission with PNAS-run review is the conservative default and carries no such overhead.

## Timing implications

- **Direct:** PNAS assigns the editor and manages review; timeline is standard for the journal and outside your control.
- **Contributed:** the member front-loads the work (securing reviewers, collecting reviews, bundling responses) *before* the paper reaches PNAS, which can shorten the journal-side timeline — but only if the member actually has time to manage it. Do not choose Contributed for speed if the member cannot commit the effort.

## Eligibility & integrity checklist

- [ ] Is any author a current NAS member? (If no → Direct.)
- [ ] If Contributed: has the member used their annual contribution quota? (Confirm current cap.)
- [ ] If Contributed: can the member secure **≥2 independent** reviewers (no conflicts/recent collaboration)?
- [ ] If Contributed: are the reviews and author responses ready to submit **with** the paper?
- [ ] Cover letter states the chosen track and, for Direct, suggested editors/reviewers (`pnas-submission`).

## Output format

```
【NAS member among authors?】 yes/no (who)
【Track chosen】 Direct / Contributed / (legacy — confirm)
【If Contributed】 member: ___ | within annual quota? yes/no | ≥2 independent reviewers secured? yes/no
【Reviewer-independence check】 ok / risk → if risk, switch to Direct
【Why this track】 one line
【Next】 pnas-writing
```

## Anti-patterns

- **Do not** use Contributed Submission to avoid genuine independent review — reviews are still required and submitted.
- **Do not** assume a member can contribute unlimited papers — the annual quota is real (≈2/year; confirm).
- **Do not** plan around the discontinued "Communicated" track.
- **Do not** let a member contribute when reviewers are recent collaborators — use Direct instead.
- **Do not** leave the track decision to the final submission step; it shapes editor handling.
