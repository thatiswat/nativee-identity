from fastapi import (
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.core.jwt import decode_token

from app.dependencies.auth import security
from app.dependencies.database import get_db

from app.repositories.user import UserRepository


def get_current_user(
    credentials=Depends(
        security,
    ),
    db: Session = Depends(
        get_db,
    ),
):

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
        )

    payload = decode_token(
        credentials.credentials,
    )

    if payload.get("type") != "access":
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    try:
        user_id = int(
            payload["sub"],
        )
    except (
        KeyError,
        TypeError,
        ValueError,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    user = UserRepository(
        db,
    ).get_by_id(
        user_id,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user