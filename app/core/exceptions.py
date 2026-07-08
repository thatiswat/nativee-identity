from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


def register_exception_handlers(
    app: FastAPI,
):

    @app.exception_handler(
        HTTPException,
    )
    async def http_exception(
        request,
        exc,
    ):

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": {
                    "code": str(exc.status_code),
                    "message": exc.detail,
                },
            },
        )

    @app.exception_handler(
        Exception,
    )
    async def internal_exception(
        request,
        exc,
    ):

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": "Unexpected server error.",
                },
            },
        )