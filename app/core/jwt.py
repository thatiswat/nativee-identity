from datetime import (
    datetime,
    timedelta,
    timezone,
)

from pathlib import Path

import os
import uuid

from jose import (
    jwt,
    JWTError,
)


# ==================================================
# Paths
# ==================================================

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



# ==================================================
# RSA Key Loading
# ==================================================

PRIVATE_KEY = os.getenv(
    "JWT_PRIVATE_KEY",
)


PUBLIC_KEY = os.getenv(
    "JWT_PUBLIC_KEY",
)



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



# ==================================================
# JWT Configuration
# ==================================================

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
    "nativee",
)


JWT_KEY_ID = os.getenv(
    "JWT_KEY_ID",
    "kid_2026_01",
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



# ==================================================
# Helpers
# ==================================================

def _now():

    return datetime.now(
        timezone.utc,
    )



def _generate_jti(
    prefix: str,
):

    return (
        f"{prefix}_"
        f"{uuid.uuid4().hex}"
    )



def _jwt_headers():

    return {
        "kid": JWT_KEY_ID,
    }



# ==================================================
# Create Access Token
# ==================================================

def create_access_token(
    *,
    user,
    session_id: str,
):

    now = _now()


    payload = {

        # ------------------------------
        # Public Identity
        # ------------------------------

        "sub": user.public_id,


        "email": user.email,


        "email_verified": getattr(
            user,
            "email_verified",
            False,
        ),


        "phone_verified": getattr(
            user,
            "phone_verified",
            False,
        ),


        "is_active": getattr(
            user,
            "is_active",
            True,
        ),



        # ------------------------------
        # Session
        # ------------------------------

        "sid": session_id,



        # ------------------------------
        # Token Identity
        # ------------------------------

        "jti": _generate_jti(
            "atk",
        ),



        # ------------------------------
        # Token Type
        # ------------------------------

        "type": "access",



        # ------------------------------
        # JWT Claims
        # ------------------------------

        "iss": IDENTITY_ISSUER,

        "aud": IDENTITY_AUDIENCE,

        "iat": now,

        "nbf": now,

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
        headers=_jwt_headers(),
    )



# ==================================================
# Create Refresh Token
# ==================================================

def create_refresh_token(
    *,
    user_public_id: str,
    session_id: str,
):

    now = _now()


    payload = {

        # ------------------------------
        # Public Identity
        # ------------------------------

        "sub": user_public_id,



        # ------------------------------
        # Session
        # ------------------------------

        "sid": session_id,



        # ------------------------------
        # Token Identity
        # ------------------------------

        "jti": _generate_jti(
            "rtk",
        ),



        # ------------------------------
        # Token Type
        # ------------------------------

        "type": "refresh",



        # ------------------------------
        # JWT Claims
        # ------------------------------

        "iss": IDENTITY_ISSUER,

        "aud": IDENTITY_AUDIENCE,

        "iat": now,

        "nbf": now,

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
        headers=_jwt_headers(),
    )



# ==================================================
# Decode Token
# ==================================================

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



# ==================================================
# Decode Access Token
# ==================================================

def decode_access_token(
    token: str,
):

    payload = decode_token(
        token,
    )


    if not payload:

        return None



    if payload.get(
        "type"
    ) != "access":

        return None



    return payload



# ==================================================
# Decode Refresh Token
# ==================================================

def decode_refresh_token(
    token: str,
):

    payload = decode_token(
        token,
    )


    if not payload:

        return None



    if payload.get(
        "type"
    ) != "refresh":

        return None



    return payload