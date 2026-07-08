from datetime import (
    datetime,
    timedelta,
    timezone,
)

from pathlib import Path
import os

from jose import (
    jwt,
    JWTError,
)


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


PRIVATE_KEY_PATH = (
    BASE_DIR
    / "keys"
    / "private.pem"
)


PUBLIC_KEY_PATH = (
    BASE_DIR
    / "keys"
    / "public.pem"
)



# --------------------------------------------------
# Load RSA Keys
# --------------------------------------------------

PRIVATE_KEY = os.getenv(
    "JWT_PRIVATE_KEY",
)

PUBLIC_KEY = os.getenv(
    "JWT_PUBLIC_KEY",
)


# Local development fallback

if not PRIVATE_KEY:

    with open(
        PRIVATE_KEY_PATH,
        "r",
    ) as file:
        PRIVATE_KEY = file.read()


if not PUBLIC_KEY:

    with open(
        PUBLIC_KEY_PATH,
        "r",
    ) as file:
        PUBLIC_KEY = file.read()


# --------------------------------------------------
# Identity JWT Configuration
# --------------------------------------------------

IDENTITY_ALGORITHM = os.getenv(
    "IDENTITY_ALGORITHM",
    "RS256",
)


IDENTITY_ISSUER = os.getenv(
    "IDENTITY_ISSUER",
    "http://127.0.0.1:8000",
)


IDENTITY_AUDIENCE = os.getenv(
    "IDENTITY_AUDIENCE",
    "nativeee",
)


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



# --------------------------------------------------
# Create Access Token
# --------------------------------------------------

def create_access_token(
    *,
    user,
    session_id: str,
):

    now = datetime.now(
        timezone.utc,
    )


    payload = {

        # ------------------------------
        # Identity
        # ------------------------------

        "sub": str(
            user.id,
        ),

        "pid": user.public_id,

        "email": user.email,

        "name": user.display_name,

        "role": getattr(
            user,
            "role",
            "user",
        ),

        "is_active": getattr(
            user,
            "is_active",
            True,
        ),


        # Session identity

        "sid": session_id,


        # ------------------------------
        # JWT Metadata
        # ------------------------------

        "type": "access",

        "iss": IDENTITY_ISSUER,

        "aud": IDENTITY_AUDIENCE,

        "iat": now,

        "exp": (
            now
            + timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
            )
        ),
    }


    return jwt.encode(
        payload,
        PRIVATE_KEY,
        algorithm=IDENTITY_ALGORITHM,
    )



# --------------------------------------------------
# Create Refresh Token
# --------------------------------------------------

def create_refresh_token(
    user_id: int,
    session_id: str,
):

    now = datetime.now(
        timezone.utc,
    )


    payload = {

        "sub": str(
            user_id,
        ),

        "sid": session_id,


        "type": "refresh",

        "iss": IDENTITY_ISSUER,

        "aud": IDENTITY_AUDIENCE,

        "iat": now,

        "exp": (
            now
            + timedelta(
                days=REFRESH_TOKEN_EXPIRE_DAYS,
            )
        ),
    }


    return jwt.encode(
        payload,
        PRIVATE_KEY,
        algorithm=IDENTITY_ALGORITHM,
    )



# --------------------------------------------------
# Decode Token
# --------------------------------------------------

def decode_token(
    token: str,
):

    try:

        return jwt.decode(
            token,
            PUBLIC_KEY,
            algorithms=[
                IDENTITY_ALGORITHM,
            ],
            audience=IDENTITY_AUDIENCE,
            issuer=IDENTITY_ISSUER,
        )


    except JWTError:

        return None



# --------------------------------------------------
# Decode Access Token
# --------------------------------------------------

def decode_access_token(
    token: str,
):

    payload = decode_token(
        token,
    )


    if payload is None:
        return None


    if payload.get(
        "type"
    ) != "access":

        return None


    return payload



# --------------------------------------------------
# Decode Refresh Token
# --------------------------------------------------

def decode_refresh_token(
    token: str,
):

    payload = decode_token(
        token,
    )


    if payload is None:
        return None


    if payload.get(
        "type"
    ) != "refresh":

        return None


    return payload