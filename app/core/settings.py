from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# --------------------------------------------------
# Database
# --------------------------------------------------

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "",
).strip()

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is missing."
    )


# --------------------------------------------------
# Identity JWT
# --------------------------------------------------

IDENTITY_ISSUER = os.getenv(
    "IDENTITY_ISSUER",
    "http://127.0.0.1:8000",
).strip()


IDENTITY_AUDIENCE = os.getenv(
    "IDENTITY_AUDIENCE",
    "nativeee",
).strip()


IDENTITY_ALGORITHM = os.getenv(
    "IDENTITY_ALGORITHM",
    "RS256",
).strip()


# --------------------------------------------------
# Token Expiry
# --------------------------------------------------

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "15",
    )
)


REFRESH_TOKEN_EXPIRE_DAYS = int(
    os.getenv(
        "REFRESH_TOKEN_EXPIRE_DAYS",
        "30",
    )
)