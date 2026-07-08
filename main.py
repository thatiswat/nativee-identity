from fastapi import FastAPI

from app.api.auth import (
    router as auth_router,
)
from app.api.jwt import (
    router as jwt_router,
)
from app.api.well_known import (
    router as discovery_router,
)

from app.core.exceptions import (
    register_exception_handlers,
)

from app.database.base import Base
from app.database.session import engine

# Import models
from app.models.user import User
from app.models.auth_session import AuthSession

from app.middleware.logging import (
    LoggingMiddleware,
)
from app.middleware.request import (
    RequestMiddleware,
)
from app.middleware.security import (
    SecurityMiddleware,
)


# ----------------------------------
# Database
# ----------------------------------

Base.metadata.create_all(
    bind=engine,
)


# ----------------------------------
# Application
# ----------------------------------

app = FastAPI(
    title="Nativee Identity",
    version="1.0.0",
)


# ----------------------------------
# Exception Handlers
# ----------------------------------

register_exception_handlers(
    app,
)


# ----------------------------------
# Middleware
# ----------------------------------

app.add_middleware(
    RequestMiddleware,
)

app.add_middleware(
    LoggingMiddleware,
)

app.add_middleware(
    SecurityMiddleware,
)


# ----------------------------------
# Routers
# ----------------------------------

app.include_router(
    auth_router,
)

app.include_router(
    jwt_router,
)

app.include_router(
    discovery_router,
)


# ----------------------------------
# Health Check
# ----------------------------------

@app.get("/")
def root():
    return {
        "service": "identity",
        "status": "running",
    }