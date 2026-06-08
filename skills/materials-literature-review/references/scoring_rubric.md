# Scoring Rubric

Score every paper on two axes.

## RelevanceScore

Use 1 to 5:

- `5`: Directly supports the target chain: microstructure or texture input, physics model or surrogate, calibration, and target mechanical-property prediction.
- `4`: Strongly adjacent. Covers the same target output or method but with another material, or covers the target material with a less direct method.
- `3`: Methodologically useful but indirect, such as general microstructure-property ML, generic surrogate modeling, or broad parameter identification.
- `2`: Background or transferable concept only.
- `1`: Peripheral; keep only if it helps historical framing or terminology.

Boost relevance when a paper includes any of:

- the target material family or close analogues,
- microscopy maps, ODF, pole figures, texture components, or microtexture,
- tensile, compression, forming, or direction-dependent mechanical tests,
- anisotropy metrics, stress-strain curves, yield surfaces, or forming limits,
- CPFE, CP-FFT, VPSC, or other constitutive laws,
- Bayesian optimization/calibration or uncertainty quantification,
- ML surrogate, CNN/GNN/transformer/neural operator, image-to-property model.

## AuthorityScore

Use 1 to 5:

- `5`: High-authority journal, canonical review, widely cited foundation, or direct field-defining paper.
- `4`: Strong peer-reviewed journal or high-quality specialized venue.
- `3`: Solid but narrower journal/conference, recent preprint with useful method, or reputable report.
- `2`: Weakly documented source, thesis-only source, or unverified proceedings.
- `1`: Unreliable, duplicate, inaccessible, or insufficient bibliographic detail.

## OverallScore and Tier

Use:

```text
OverallScore = 0.6 * RelevanceScore + 0.4 * AuthorityScore
```

Tier thresholds:

- `Core`: `OverallScore >= 4.4`
- `Important`: `3.6 <= OverallScore < 4.4`
- `Useful`: `2.8 <= OverallScore < 3.6`
- `Peripheral`: `OverallScore < 2.8`
