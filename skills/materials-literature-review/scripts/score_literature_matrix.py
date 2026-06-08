#!/usr/bin/env python
"""Score a materials literature matrix by relevance and authority."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


CORE_BUCKETS = {
    "material_texture_formability": 5,
    "texture_to_curve_or_anisotropy": 5,
    "microstructure_property_ml": 5,
    "calibration_and_optimization": 4,
    "physics_model_surrogate": 4,
    "virtual_material_testing": 4,
    "physics_informed_ml": 4,
    "review_methods": 3,
}

RELEVANCE_TERMS = [
    "target alloy",
    "target material",
    "microstructure",
    "microscopy",
    "texture",
    "odf",
    "r-value",
    "lankford",
    "stress-strain",
    "crystal plasticity",
    "cpfem",
    "cpfe",
    "bayesian",
    "machine learning",
    "deep learning",
    "surrogate",
]


def to_float(value: object) -> float | None:
    try:
        text = str(value).strip()
        if not text:
            return None
        return float(text)
    except (TypeError, ValueError):
        return None


def clamp_score(value: float) -> int:
    return max(1, min(5, int(round(value))))


def combined_text(row: dict[str, str]) -> str:
    return " ".join(str(v) for v in row.values()).lower()


def infer_relevance(row: dict[str, str]) -> int:
    existing = to_float(row.get("RelevanceScore"))
    if existing is not None:
        return clamp_score(existing)

    bucket = row.get("Bucket", "").strip().lower()
    score = CORE_BUCKETS.get(bucket, 3)
    text = combined_text(row)
    hits = sum(1 for term in RELEVANCE_TERMS if term in text)

    if hits >= 5:
        score += 1
    elif hits <= 1:
        score -= 1

    priority = row.get("Priority", "").strip().lower()
    if priority == "high":
        score += 0.5
    elif priority == "low":
        score -= 0.5

    return clamp_score(score)


def infer_authority(row: dict[str, str]) -> int:
    existing = to_float(row.get("AuthorityScore"))
    if existing is not None:
        return clamp_score(existing)

    text = combined_text(row)
    score = 3

    if "doi.org" in text or "10." in row.get("URL", ""):
        score += 1
    if "review" in text or "overview" in text:
        score += 0.5
    if "preprint" in text or "arxiv" in text:
        score -= 0.5
    if "needs verification" in text or "unverified" in text:
        score -= 1

    return clamp_score(score)


def tier(overall: float) -> str:
    if overall >= 4.4:
        return "Core"
    if overall >= 3.6:
        return "Important"
    if overall >= 2.8:
        return "Useful"
    return "Peripheral"


def score_row(row: dict[str, str], refresh: bool) -> dict[str, str]:
    if refresh:
        row["RelevanceScore"] = ""
        row["AuthorityScore"] = ""

    relevance = infer_relevance(row)
    authority = infer_authority(row)
    overall = round(0.6 * relevance + 0.4 * authority, 2)

    row["RelevanceScore"] = str(relevance)
    row["AuthorityScore"] = str(authority)
    row["OverallScore"] = f"{overall:g}"
    row["Tier"] = tier(overall)
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    for field in ["RelevanceScore", "AuthorityScore", "OverallScore", "Tier"]:
        if field not in fieldnames:
            fieldnames.append(field)

    scored = [score_row(row, args.refresh) for row in rows]
    scored.sort(
        key=lambda row: (
            -float(row.get("OverallScore", "0") or 0),
            row.get("Bucket", ""),
            row.get("Year", ""),
            row.get("Reference", ""),
        )
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scored)

    print(f"Wrote {len(scored)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
