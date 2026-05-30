---
name: anmath-length-management
description: Use when controlling the length of a pure-mathematics manuscript for Annals of Mathematics — math papers may be long, but every section must be necessary; this skill cuts bloat and padding while keeping the proof complete and gap-free. Late-stage; run after the proof and architecture are fixed.
---

# Length Discipline (anmath-length-management)

## When to trigger

- The paper has grown long and you cannot defend every section's necessity
- Background or preliminaries dwarf the actual new mathematics
- The same idea is explained several times in different words
- You feel pressure to "say it is easy to see" to shorten a hard step — stop

## The principle: long is fine, bloated is not

Annals papers can be long — a deep result may require many pages. Length is **not** a defect.
**Bloat** is: material that does not advance the proof, padding, repetition, or restating
known background at textbook length. The test for every paragraph is necessity, not size.

| Question | If "no" → |
|----------|-----------|
| Does this paragraph advance the proof or its understanding? | Cut or compress it |
| Is this background needed to read *this* paper specifically? | Replace with a precise citation |
| Have I already said this elsewhere? | Delete the repetition |
| Could this routine computation be summarized + appendixed? | Move to appendix (anmath-supplementary) |
| Is this section's job stated in one line at its top? | If not, the section may be unfocused |

## What to compress vs. what to keep

**Compress / cut**
- Textbook-level background that a citation handles
- Repeated re-statements of the strategy in slightly different words
- Over-long motivational prose that delays the mathematics
- Routine multi-page computations (summarize result in text, push detail to appendix)

**Never cut for length**
- The crux / new idea — it stays in full
- Any step a referee must check to believe the theorem
- Hypotheses, quantifiers, and constant dependence
- Precise statements of external results you invoke

> Shortening must never create a gap. If a step is long *because it is hard*, that length
> is earned — keep it. The forbidden shortcut is replacing a hard step with "it is easy to
> see" (see anmath-writing-style).

## Section-necessity pass

- For each section, write one sentence stating why it is necessary. If you cannot, the
  section is a candidate for merging, compressing, or appendixing.
- Check that preliminaries are proportionate to their use — recall only what the paper uses.
- Confirm appendices carry length relief, not hidden essentials.

## Checklist

- [ ] Every section has a one-line justification of necessity
- [ ] Textbook background is replaced by precise citations
- [ ] No idea or strategy statement is repeated unnecessarily
- [ ] Routine long computations are summarized in text and detailed in an appendix
- [ ] No step was shortened in a way that introduces a gap
- [ ] The crux and all referee-checkable steps remain in full
- [ ] Overall length is defensible: every page earns its place

## Anti-patterns

- Padding preliminaries with background the paper never uses
- Restating the proof strategy three times to fill space
- Cutting a hard step to "it is easy to see" to hit a length target (a fatal gap)
- A 90-page paper where 30 pages are recycled background
- Burying the new contribution under disproportionate motivational prose
- Trimming hypotheses or constant-dependence statements to save lines

## Output format

```
【Total length】~N pages
【Sections without necessity justification】... → compress / merge / appendix
【Background to replace with citation】...
【Repetition removed】...
【Computations moved to appendix】... → anmath-supplementary
【Gap introduced by cutting?】no / FIX (return to anmath-writing-style)
【Next step】anmath-cover-letter
```
