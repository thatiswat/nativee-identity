from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.dependencies.auth import (
    get_current_user,
)
from app.dependencies.database import get_db

from app.models.user import User

from app.schemas.auth import (
    LoginRequest,
    RefreshRequest,
    RegisterRequest,
)

from app.services.auth import AuthService
from app.services.auth_session import AuthSessionService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    try:
        user = service.register(request)

        return {
            "success": True,
            "data": {
                "user": {
                    "id": user.public_id,
                    "email": user.email,
                    "display_name": user.display_name,
                }
            },
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    try:
        return {
            "success": True,
            "data": service.login(
                request,
            ).model_dump(),
        }

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


@router.post("/refresh")
def refresh(
    request: RefreshRequest,
    db: Session = Depends(get_db),
):
    service = AuthSessionService(
        db,
    )

    try:
        token = service.refresh(
            request.refresh_token,
        )

        return {
            "success": True,
            "data": token,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


@router.post("/logout")
def logout(
    request: RefreshRequest,
    db: Session = Depends(get_db),
):
    service = AuthSessionService(
        db,
    )

    try:
        service.logout(
            request.refresh_token,
        )

        return {
            "success": True,
            "data": {
                "message": "Logged out successfully.",
            },
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/logout-all")
def logout_all(
    user: User = Depends(
        get_current_user,
    ),
    db: Session = Depends(
        get_db,
    ),
):
    AuthSessionService(
        db,
    ).logout_all(
        user.id,
    )

    return {
        "success": True,
        "data": {
            "message": "Logged out from all devices.",
        },
    }


@router.get("/me")
def me(
    user: User = Depends(
        get_current_user,
    ),
):

    return {
        "success": True,
        "data": {
            "id": user.public_id,
            "email": user.email,
            "display_name": user.display_name,
            "email_verified": user.email_verified,
            "phone_verified": user.phone_verified,
        },
    }