$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$gh = "C:\Program Files\GitHub CLI\gh.exe"

if (-not (Test-Path $gh)) {
  throw "GitHub CLI not found at $gh"
}

Push-Location $repoRoot
try {
  Write-Host "This script logs in to GitHub with a token you paste locally." -ForegroundColor Cyan
  Write-Host "Do not paste the token into chat. Paste it only into this PowerShell window." -ForegroundColor Yellow
  Write-Host "For a public repo, a classic PAT with public_repo is enough. For private, use repo." -ForegroundColor Yellow

  $secureToken = Read-Host "Paste GitHub token" -AsSecureString
  $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureToken)
  try {
    $token = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
    if ([string]::IsNullOrWhiteSpace($token)) {
      throw "Token was empty."
    }

    $token | & $gh auth login --hostname github.com --git-protocol https --with-token
    if ($LASTEXITCODE -ne 0) {
      throw "GitHub CLI login failed."
    }
  }
  finally {
    if ($bstr -ne [IntPtr]::Zero) {
      [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
    }
    $token = $null
  }

  & "$repoRoot\PUBLISH_TO_GITHUB.ps1"
  if ($LASTEXITCODE -ne 0) {
    throw "Publish script failed."
  }
}
finally {
  Pop-Location
}
