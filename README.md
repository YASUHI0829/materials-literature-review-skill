# Materials Literature Review Skill

Standalone Codex skill package for building evidence-tracked materials-science literature reviews.

This project is intentionally separate from other literature/RAG repositories. It contains only generic workflow instructions, templates, and a scoring helper. Project-specific paper matrices, private review drafts, and unpublished research notes should stay in their own local research folders.

## Contents

- `skills/materials-literature-review/SKILL.md`: Codex skill entrypoint.
- `skills/materials-literature-review/references/`: search taxonomy, scoring rubric, and synthesis protocol.
- `skills/materials-literature-review/assets/templates/`: CSV and Markdown templates.
- `skills/materials-literature-review/scripts/score_literature_matrix.py`: helper to fill relevance, authority, overall score, and tier fields.

## Use

Copy or symlink `skills/materials-literature-review` into `C:\Users\FUJIYOSHI\.codex\skills\materials-literature-review`, or keep this folder as the source copy and sync when the skill changes.
