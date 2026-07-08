from starlette.middleware.base import BaseHTTPMiddleware


class SecurityMiddleware(
    BaseHTTPMiddleware,
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        response = await call_next(
            request,
        )

        response.headers[
            "X-Frame-Options"
        ] = "DENY"

        response.headers[
            "X-Content-Type-Options"
        ] = "nosniff"

        response.headers[
            "Referrer-Policy"
        ] = "same-origin"

        response.headers[
            "Permissions-Policy"
        ] = "camera=(), microphone=(), geolocation=()"

        return response