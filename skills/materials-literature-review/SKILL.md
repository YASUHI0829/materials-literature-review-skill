---
name: materials-literature-review
description: Build large, evidence-tracked materials-science literature reviews and scored paper matrices. Use for systematic or semi-systematic reviews involving microstructure or texture inputs, crystal plasticity, constitutive modeling, calibration, machine-learning surrogates, microstructure-to-property prediction, forming anisotropy, stress-strain curves, or related structure-property literature mapping.
---

# Materials Literature Review

## Core Workflow

1. Frame the review as an input-to-output chain:
   `microstructure/texture -> model or surrogate -> calibrated parameters -> target properties`.
2. Split the search into lanes instead of one broad query: material-specific, experiment-specific, physics model, calibration/optimization, ML surrogate, and review/foundation lanes.
3. Build or update a CSV matrix before writing prose. Use `assets/templates/papers_matrix_template.csv`.
4. Verify high-priority papers by DOI, publisher page, arXiv, author page, or indexed bibliographic source. Mark unverified records clearly.
5. Score each paper on relevance and authority, then assign tiers. Use `references/scoring_rubric.md` and optionally `scripts/score_literature_matrix.py`.
6. Do citation chasing from Core papers: backward references for foundations, forward citations for newer methods.
7. Write the review from the matrix. Use `assets/templates/review_outline.md` and `assets/templates/paper_extraction_note.md`.

## Search Lanes

Load `references/search_taxonomy.md` when expanding literature. Keep lanes separate in the matrix. Typical lanes:

- `Material_texture_formability`
- `Microstructure_property_ML`
- `Texture_to_curve_or_anisotropy`
- `Physics_model_surrogate`
- `Calibration_and_optimization`
- `Virtual_material_testing`
- `Physics_informed_ML`
- `Review_methods`

For a project-specific review, prioritize papers that connect at least two of these: target material family, microstructure or texture descriptors, mechanical tests, property prediction targets, constitutive models, calibration, and ML surrogate or image-to-property learning.

## Matrix Practice

Keep every row concise but decision-useful:

- `Reference`: title plus first author when known.
- `Input`: microscopy map, ODF, pole figure, texture components, synthetic simulation data, experimental curve, etc.
- `Method`: CPFE, CP-FFT, VPSC, CNN, GNN, GP, Bayesian optimization, analytical texture model, etc.
- `Output`: stress-strain curve, anisotropy metric, yield surface, forming limit, model parameters, texture evolution, local field, etc.
- `RelevanceToProject`: state exactly why the paper matters.
- `Status`: use labels such as `verified`, `web verified`, `citation-chasing`, `needs DOI check`, or `not yet read`.

Do not claim coverage is complete. Say coverage is strong only after checking multiple lanes and citation chains.

## Scoring

Use:

```text
OverallScore = 0.6 * RelevanceScore + 0.4 * AuthorityScore
```

Then tier papers:

- `Core`: overall >= 4.4
- `Important`: overall >= 3.6
- `Useful`: overall >= 2.8
- `Peripheral`: overall < 2.8

Load `references/scoring_rubric.md` before changing scoring rules.

## Useful Commands

Score or re-score a matrix:

```powershell
python skills\materials-literature-review\scripts\score_literature_matrix.py `
  --input path\to\papers_matrix.csv `
  --output path\to\papers_matrix_scored.csv
```

Generate a quick lane summary:

```powershell
Import-Csv path\to\papers_matrix_scored.csv |
  Group-Object Bucket |
  Sort-Object Name |
  ForEach-Object { "{0},{1}" -f $_.Name,$_.Count }
```

## Synthesis Rules

Load `references/synthesis_protocol.md` before drafting a review section. Preserve the difference between:

- direct evidence for the target material,
- transferable evidence from related materials,
- methodological evidence from modeling or ML papers,
- project-specific inferences made by connecting those lines.

Make the gap statement explicit: most papers cover one or two links in the chain; the review should identify what remains missing in the full structure-property workflow.
