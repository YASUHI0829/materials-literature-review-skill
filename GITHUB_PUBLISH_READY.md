# GitHub Publish Ready

This folder is a standalone project for the generic `materials-literature-review` Codex skill.

It is intentionally separate from any literature RAG project and contains no project-specific paper matrix, private review draft, or unpublished research content.

## Proposed Repository

Suggested GitHub repository name:

```text
materials-literature-review-skill
```

Suggested remote URL after repository creation:

```text
https://github.com/YASUHI0829/materials-literature-review-skill.git
```

## What Will Be Uploaded

- `README.md`
- `.gitignore`
- `skills/materials-literature-review/SKILL.md`
- `skills/materials-literature-review/agents/openai.yaml`
- `skills/materials-literature-review/references/search_taxonomy.md`
- `skills/materials-literature-review/references/scoring_rubric.md`
- `skills/materials-literature-review/references/synthesis_protocol.md`
- `skills/materials-literature-review/assets/templates/papers_matrix_template.csv`
- `skills/materials-literature-review/assets/templates/paper_extraction_note.md`
- `skills/materials-literature-review/assets/templates/review_outline.md`
- `skills/materials-literature-review/scripts/score_literature_matrix.py`

## What Must Not Be Uploaded

Keep these in local/private research folders only:

- Project-specific paper matrices.
- Project-specific review drafts.
- Experiment notes.
- Simulation case files.
- Files from unrelated RAG projects.
- Any unpublished or laboratory-specific data.

## Current Local Status

Local repository:

```text
D:\Research\materials-literature-review-skill
```

Current local commit:

```text
9d92032 Create standalone materials literature review skill
```

The repository currently has no GitHub remote configured.

## Publish Commands

After logging in to GitHub CLI:

```powershell
& "C:\Program Files\GitHub CLI\gh.exe" auth login
cd D:\Research\materials-literature-review-skill
& "C:\Program Files\GitHub CLI\gh.exe" repo create materials-literature-review-skill --public --source . --remote origin --push
```

If the repository already exists on GitHub:

```powershell
cd D:\Research\materials-literature-review-skill
git remote add origin https://github.com/YASUHI0829/materials-literature-review-skill.git
git push -u origin main
```

## Verification Before Publishing

Run:

```powershell
python C:\Users\FUJIYOSHI\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\Research\materials-literature-review-skill\skills\materials-literature-review
.\PUBLISH_TO_GITHUB.ps1
```

Expected result:

- Validator says `Skill is valid!`
- The publish script refuses to continue if project-specific terms are found.
