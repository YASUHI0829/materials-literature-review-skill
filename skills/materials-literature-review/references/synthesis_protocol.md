# Synthesis Protocol

## Evidence Classes

Tag each claim as one of:

- `Direct`: target material and target product-form evidence.
- `Transferable`: another material system with the same target variable.
- `Method`: general modeling, calibration, or ML method evidence.
- `Inference`: a project-specific conclusion obtained by connecting multiple sources.

Only Direct and Transferable evidence should support material behavior claims. Method evidence can support workflow choices. Inference should be labeled clearly.

## Review Structure

Use this order for a microstructure-to-property materials review:

1. Problem definition: why the selected mechanical-property targets matter.
2. Target-material microstructure, texture, property, and formability literature.
3. Physics-based constitutive modeling for the selected material family.
4. Calibration and parameter identification.
5. Virtual material testing and synthetic labels.
6. ML from texture, microstructure, or simulations to properties.
7. Research gap and proposed workflow.

## Gap Statement Template

```text
Existing work separately demonstrates material-specific microstructure-property
analysis, physics-based virtual material testing, calibration of constitutive
parameters, and ML prediction from texture or microstructure. However, few studies
close the full loop from measured microstructure to experimentally validated
property prediction with uncertainty-aware calibration and an ML surrogate.
```

Customize the material names and target properties after checking the matrix.

## Quality Checks

Before calling the review comprehensive, confirm:

- Each search lane has at least one Core or Important paper.
- Direct target-material evidence is separated from transferable evidence.
- Core papers have DOI/publisher/source URLs.
- ML papers are not used to claim target-material behavior unless they include direct or clearly transferable evidence.
- The write-up distinguishes prediction, inverse design, and parameter calibration.
