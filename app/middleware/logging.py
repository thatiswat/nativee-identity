import logging

from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

logger = logging.getLogger(
    "identity",
)


class LoggingMiddleware(
    BaseHTTPMiddleware,
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        logger.info(
            "%s %s",
            request.method,
            request.url.path,
        )

        return await call_next(
            request,
        )