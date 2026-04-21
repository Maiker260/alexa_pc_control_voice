from src.utils.run_ps import run_ps

def remove_user_config():
    run_ps(
        'if (Test-Path $env:USERPROFILE\\.cloudflared) { Remove-Item -Recurse -Force $env:USERPROFILE\\.cloudflared }'
    )