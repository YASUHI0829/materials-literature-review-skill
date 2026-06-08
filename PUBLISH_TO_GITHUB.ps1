$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$gh = "C:\Program Files\GitHub CLI\gh.exe"
$repoName = "materials-literature-review-skill"

if (-not (Test-Path $gh)) {
  throw "GitHub CLI not found at $gh"
}

Push-Location $repoRoot
try {
  & $gh auth status
  if ($LASTEXITCODE -ne 0) {
    throw "GitHub CLI is not logged in. Run: & `"$gh`" auth login"
  }

  python C:\Users\FUJIYOSHI\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\skills\materials-literature-review
  if ($LASTEXITCODE -ne 0) {
    throw "Skill validation failed."
  }

  $pattern = @(
    ("SUS" + "430"),
    ("AISI " + "430"),
    ("type " + "430"),
    ("paper" + "-lattice"),
    ("sus" + "430" + "_ebsd"),
    ("RD/" + "TD/" + "DD"),
    ("EBSD" + "-to-property")
  ) -join "|"
  $privateTerms = rg -n $pattern . --glob "!GITHUB_PUBLISH_READY.md" --glob "!PUBLISH_TO_GITHUB.ps1"
  if ($LASTEXITCODE -eq 0) {
    Write-Host $privateTerms
    throw "Private or project-specific terms found. Refusing to publish."
  }

  $remote = git remote get-url origin 2>$null
  if (-not $remote) {
    & $gh repo create $repoName --public --source . --remote origin --push
  } else {
    git push -u origin main
  }
}
finally {
  Pop-Location
}
