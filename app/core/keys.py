from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

KEY_DIR = BASE_DIR / "app" / "keys"

PRIVATE_KEY = KEY_DIR / "private.pem"

PUBLIC_KEY = KEY_DIR / "public.pem"