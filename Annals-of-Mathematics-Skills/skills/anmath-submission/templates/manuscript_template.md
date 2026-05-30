# Annals of Mathematics Manuscript Skeleton (AMS-LaTeX)

A structural skeleton for a theorem-and-proof manuscript. Adapt to your area; confirm the
journal's current style requirements on the official page.

## Preamble (illustrative)

```latex
\documentclass[12pt]{amsart}
\usepackage{amsmath, amsthm, amssymb, amsfonts, mathtools}
\usepackage{tikz-cd}          % only if commutative diagrams are needed
\usepackage[colorlinks=false]{hyperref}
\usepackage{cleveref}

% One consistent numbering scheme (here: numbered within section)
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
```

## Front matter

```latex
\title{[Precise, informative title]}
\author{[Author name]}
\address{[Institution, department, city, country]}
\email{[email]}
\subjclass[2020]{Primary [xxXxx]; Secondary [xxXxx]}   % MSC, match the main result
\keywords{[keyword]; [keyword]; [keyword]}
\date{\today}
\begin{abstract}
[Self-contained. State the Main Theorem in plain terms, the advance over prior work,
and the key idea in one or two sentences. No undefined notation.]
\end{abstract}
```

## Body structure

### 1. Introduction

- Problem and history: what the question is and what was known.
- **Main Theorem**, stated precisely and early:

```latex
\begin{theorem}[Main Theorem]\label{thm:main}
Let [hypotheses, all explicit]. Then [precise conclusion].
\end{theorem}
```

- What is new vs. prior work: name the closest prior results and what they proved.
- Consequences / corollaries (state separately from the Main Theorem).
- **Proof strategy** in one paragraph: the main steps, the key lemma(s), the crux.
- Organization of the paper.

### 2. Preliminaries and Notation

- Conventions and definitions, each introduced before use.
- Precise statements (with citation) of external results invoked.

### 3. Constructions / Setup

- The objects the proof manipulates, defined carefully.

### 4. Key Lemmas

```latex
\begin{lemma}\label{lem:key}
[Statement with its own explicit hypotheses.]
\end{lemma}
\begin{proof}
[Full argument. No "clearly"/"it is easy to see" guarding a real step.]
\end{proof}
```

### 5. Proof of the Main Theorem

```latex
\begin{proof}[Proof of \Cref{thm:main}]
[Assemble the lemmas into the headline result; the crux fully visible.]
\end{proof}
```

### 6. Consequences

- Corollaries and remarks; relate back to the problem in the introduction.

### Appendices (length relief only — no hidden essentials)

```latex
\appendix
\section{Proof of the estimate in \Cref{lem:key}}
[Long but routine computation; the main text states what this establishes.]
```

## References (BibTeX)

```latex
\bibliographystyle{amsplain}   % or alpha; use MathSciNet abbreviations / \MR{}
\bibliography{refs}
```

- Every in-text citation appears in `refs.bib` and vice versa.
- Prefer versions of record; label preprints (with arXiv id) explicitly.

## Rigor reminders (do not ship without these)

- The Main Theorem statement matches exactly what the proof delivers.
- Quantifier order explicit; constant dependence stated.
- No essential step rests on an unpublished/unverifiable claim.
- Any computer-assisted step: software, version, exact claim checked, archived code/data.
