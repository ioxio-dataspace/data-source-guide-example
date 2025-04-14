from os import environ
from pathlib import Path

DEV_ENV = {"PORT": environ.get("PORT", "8000")}
REPO_ROOT = Path(__file__).parent.parent


def uvicorn_common():
    return {
        "app": "app.app:app",
        "host": "0.0.0.0",  # nosec
        "port": int(environ.get("PORT", "8000")),
    }
