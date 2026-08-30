# v2.13 Submission Package

**Version:** Draft v2.12.1 frozen (2026-08-30)

## Contents

```
v2.13/
 ├── manuscript.pdf        (frozen — compiled from manuscript.tex)
 ├── manuscript.tex        (frozen — same as papers/rh-discriminator-v29.tex)
 ├── figures/              (none)
 ├── bibliography.bib      (Weil 1952, Barner 1981, Schwartz, Hörmander)
 ├── README.txt            (this file)
 ├── cover_letter.md       (Cover Letter draft)
 └── referee_response.md   (Referee Response Appendix C1-C5)
```

## Compilation

```
pdflatex manuscript.tex        # twice for references
```

LaTeX environment: pdfTeX (TeX Live), amsmath/amssymb/amsthm/mathtools,
geometry. Compile log: 4 pages, no errors (2026-08-30 21:43).

## Freeze status

- Mathematical structure: frozen (no new mechanisms).
- Wording: "criterion equivalent to RH under the stated framework" —
  never "proof of RH".
- Frozen conventions: see papers/rh-discriminator-frozen-conventions.md.
- Red flag scan: prove/proved/proof of RH/solution of RH/resolves RH
  appear only in negative statements (not claims).

## External verification reminder

The manuscript does not claim a proof of RH. Final validity depends on
independent verification of the key lemmas and the applicability of the
invoked explicit formula.
