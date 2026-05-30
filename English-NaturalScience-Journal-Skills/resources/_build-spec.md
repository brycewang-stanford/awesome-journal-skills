# Build Spec — English-NaturalScience-Journal-Skills (per-journal profile skills)

This file is the **single source of truth** for the format, voice, and factual
discipline of every per-journal profile skill in this bundle. It mirrors the
proven design of the sibling `English-SocialScience-Journal-Skills` bundle, but
tuned for top English-language **natural-science, clinical/medical, physical, and
formal-science** venues (general science, life sciences, medicine, physics,
chemistry, materials/energy, earth/environment, CS/AI, mathematics).

Each journal ships **one self-contained "fit-and-house-style" profile skill**.
A profile answers four questions for an author:

1. Is my manuscript on-target for this venue?
2. How should it be framed to fit the venue's editorial culture?
3. What method-and-evidence bar does this venue expect?
4. What official submission details must I re-check before submitting?

A profile is a **positioning / venue-selection / re-framing** tool. It is **not**
a substitute for the journal's current official author instructions, and it must
say so.

The canonical 100-venue roster (slugs + editorial-DNA seeds) lives in
`journal-roster.md`. Folder name == frontmatter `name`.

---

## Canonical template (follow section order and headings exactly)

```markdown
---
name: <slug>
description: Use when targeting <Full Journal Name> (<ABBR>) or deciding whether a <field> manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# <Full Journal Name> (<slug>)

## Journal positioning

<2–4 sentences: discipline, tier, what kind of paper wins here, who the readership is. Then one boundary sentence:>
This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the publisher's own site or submission system.

## When to trigger

- The author names <Full Journal Name> / <ABBR> as the target venue.
- A manuscript is near this venue's scope but the author is unsure about significance level, method bar, or audience fit.
- A general <field> manuscript needs re-framing into the narrative this venue rewards.
- The author needs this venue's high-frequency desk-reject risks and a credible alternative-venue list before submitting.

## Scope & topic fit

- <3–6 bullets of the SPECIFIC topics / questions / paradigms this venue publishes — make it venue-distinctive, not generic.>

## Method & evidence bar

- <3–6 bullets on what this venue demands methodologically: significance/novelty bar, mechanism vs. description, validation/replication, statistics & reporting standards, data/code/materials availability, reporting guidelines (CONSORT/PRISMA/ARRIVE), registration/registered-reports, etc. Be venue-specific.>

## Structure & house style

- <3–6 bullets on framing, the significance/contribution statement, abstract conventions (structured vs. unstructured), length and format (Letter vs. Article), exhibits, and any venue-specific submission artifacts (STAR Methods, significance statement, extended data, supplementary/SI, reporting summary, data/code availability statement).>

## Official-submission checklist

- Search the live site for "<Full Journal Name> author instructions / information for authors / submission guidelines" and follow the current version, not a third-party broker's copy.
- Re-check <venue-specific items: article-type and length limits, abstract format, figure/display limits, reporting guideline + checklist, data/code/materials availability and deposition, registration/ethics/consent, competing-interests & funding disclosure, AI-use disclosure, preprint policy, open-access/APC and licensing>.
- <1–2 more venue-specific official items.>
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this paper belongs to <ABBR>'s core readership / fits its significance bar.
- [ ] The contribution is stated as <conceptual advance / mechanism / new method / definitive evidence>, not as "first to report" or a p-value.
- [ ] The framing positions the paper against <2–3 recent advances in this venue or its tier>.
- [ ] Methods, statistics, reporting checklist, data/code/materials, and exhibits already match the current official guide.
- [ ] <1–2 venue-specific self-checks.>

## Common desk-reject triggers

- <3–5 venue-specific failure modes that get papers desk-rejected or quickly rejected here.>

## Re-routing decision

<2–4 sentences or bullets: if the paper does not fit, name the more appropriate sibling venue(s) and why — use real journal names, ideally other slugs in this bundle.>

## Output format

` ``text
[Fit] High / Medium / Low (one-line reason)
[Target] <Full Journal Name>
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the current method/evidence clear this venue's significance bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / abstract / reporting checklist / data-code / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
` ``
```

(The triple-backtick fence above is shown escaped; in the real file use a normal
```text fenced block.)

---

## Voice & quality rules

1. **English, opinionated, venue-specific.** Every section must contain content
   that could only be true of *this* venue. If a paragraph would read identically
   for ten journals, it is wrong. The whole value of the bundle is differentiation.
2. **Capture editorial DNA.** State the venue's actual culture, e.g.: Nature/Science
   want a single broadly-significant advance and triage most papers before review;
   Cell wants a complete mechanistic molecular story with STAR Methods; PRL is a
   strict-length Letter judged on immediacy + breadth; NEJM/Lancet/JAMA want
   practice-changing, registered, reporting-guideline-compliant clinical evidence;
   eLife uses the Reviewed-Preprint (no accept/reject) model with public
   assessments; Chemical Reviews / RMP / Accounts / Trends are largely invited
   review venues; Nature Methods wants a generalizable, benchmarked new method;
   Annals of Mathematics wants the most significant results with full proofs.
3. **Length:** ~90–150 lines. Dense, scannable, no filler.

## Factual discipline (hard rules — do not break)

- **Do NOT invent volatile facts.** No impact factors, acceptance rates, ISSNs,
  exact word/figure limits, APC amounts, editor names, or "ranked #N" claims unless
  they are stable and widely known. When tempted, defer to the official-check
  section ("re-check current length/figure limit") instead of stating a number.
- **Stable, well-known facts are fine:** discipline; publisher/society (APS, ACS,
  RSC, AAAS, NAS, Cell Press, Springer Nature, Wiley, AHA, ACC, ESC, ASCO, ASH,
  AGA, AMS, IEEE, OUP); permanent structural features (PRL length limit exists;
  Cell STAR Methods; Nature reporting summary / extended data; eLife
  Reviewed-Preprint model; PNAS Direct Submission; CA/RMP/Chem Rev mostly invited;
  CONSORT/registration expectations at major medical journals).
- **No fabricated citations.** Do not cite specific articles by title/author/year.
  Refer to literatures and paradigms generically.
- **Defer, don't guess.** Anything that changes year to year goes in the
  official-submission checklist as "re-check," never asserted as current fact.

## Slug / naming

- Slug = kebab-case of the full journal name (frontmatter `name` == folder name),
  exactly as listed in `journal-roster.md`.
- Slugs are unique within this bundle's `skills/` directory. (No cross-bundle
  `-en`/`-cn` suffixing is required here, since this bundle has its own namespace;
  the flagship venues that also ship as repo-root depth packs — Science, Cell,
  PNAS, NEJM, The Lancet, Nature — use plain slugs here, mirroring how AER is
  covered both ways.)
