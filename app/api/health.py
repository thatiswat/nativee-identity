from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
def health():

    return {
        "success": True,
        "data": {
            "service": "identity",
            "status": "healthy",
        },
    }