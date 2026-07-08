from fastapi import (
    Depends,
    HTTPException,
)

from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)

from sqlalchemy.orm import Session

from app.core.jwt import decode_token

from app.dependencies.database import get_db

from app.repositories.user import UserRepository


security = HTTPBearer(
    auto_error=False,
)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(
        security,
    ),
    db: Session = Depends(
        get_db,
    ),
):

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization header",
        )

    try:

        payload = decode_token(
            credentials.credentials,
        )

        if payload.get("type") != "access":
            raise HTTPException(
                status_code=401,
                detail="Invalid token type",
            )

        user_id = int(
            payload["sub"],
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

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )