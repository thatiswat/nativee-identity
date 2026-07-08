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
# JWT
# --------------------------------------------------

JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "",
).strip()

JWT_ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256",
).strip()

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

if not JWT_SECRET_KEY:
    raise RuntimeError(
        "JWT_SECRET_KEY is missing."
    )