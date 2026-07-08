from fastapi import APIRouter

from jose.utils import (
    base64url_encode,
)

from cryptography.hazmat.primitives import (
    serialization,
)

from app.core.keys import (
    PUBLIC_KEY,
)


router = APIRouter(
    tags=["Discovery"],
)


# ----------------------------------
# OpenID Configuration
# ----------------------------------

@router.get(
    "/.well-known/openid-configuration",
)
def configuration():

    issuer = "http://localhost:8000"

    return {
        "issuer": issuer,
        "jwks_uri": f"{issuer}/.well-known/jwks.json",
        "authorization_endpoint": f"{issuer}/auth/login",
        "token_endpoint": f"{issuer}/auth/refresh",
        "userinfo_endpoint": f"{issuer}/auth/me",
    }


# ----------------------------------
# JSON Web Key Set (JWKS)
# ----------------------------------

@router.get(
    "/.well-known/jwks.json",
)
def jwks():

    with open(
        PUBLIC_KEY,
        "rb",
    ) as f:

        key = serialization.load_pem_public_key(
            f.read(),
        )

    numbers = key.public_numbers()

    e = base64url_encode(
        numbers.e.to_bytes(
            3,
            "big",
        ),
    ).decode()

    n = base64url_encode(
        numbers.n.to_bytes(
            (numbers.n.bit_length() + 7) // 8,
            "big",
        ),
    ).decode()

    return {
        "keys": [
            {
                "kty": "RSA",
                "alg": "RS256",
                "use": "sig",
                "kid": "nativee-main",
                "n": n,
                "e": e,
            }
        ]
    }