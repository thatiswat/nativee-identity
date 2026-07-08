from fastapi import APIRouter, Depends

from app.dependencies.auth import (
    get_current_user,
)

from app.models.user import User


router = APIRouter(
    prefix="/jwt",
    tags=["JWT"],
)


@router.get("/verify")
def verify(
    user: User = Depends(
        get_current_user,
    ),
):

    return {
        "success": True,
        "data": {
            "user_id": user.public_id,
            "email": user.email,
            "display_name": user.display_name,
        },
    }