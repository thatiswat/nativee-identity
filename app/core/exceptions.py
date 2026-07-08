"""
Nativee Identity Exceptions

Every exception raised by the application should inherit from
IdentityException.

Routers are responsible for converting these exceptions into HTTP responses.
"""


class IdentityException(Exception):
    """Base exception for Nativee Identity."""

    code = "IDENTITY_ERROR"
    message = "Identity error."

    def __init__(self, message: str | None = None):
        self.message = message or self.message
        super().__init__(self.message)


# ==========================================================
# Authentication
# ==========================================================


class AuthenticationException(IdentityException):
    code = "AUTHENTICATION_ERROR"
    message = "Authentication failed."


class InvalidCredentialsException(AuthenticationException):
    code = "INVALID_CREDENTIALS"
    message = "Invalid email or password."


class UserNotFoundException(AuthenticationException):
    code = "USER_NOT_FOUND"
    message = "User not found."


class UserInactiveException(AuthenticationException):
    code = "USER_INACTIVE"
    message = "User account is inactive."


class EmailAlreadyExistsException(AuthenticationException):
    code = "EMAIL_ALREADY_EXISTS"
    message = "Email already exists."


# ==========================================================
# Sessions
# ==========================================================


class SessionException(IdentityException):
    code = "SESSION_ERROR"
    message = "Session error."


class InvalidSessionException(SessionException):
    code = "INVALID_SESSION"
    message = "Session not found."


class SessionExpiredException(SessionException):
    code = "SESSION_EXPIRED"
    message = "Session expired."


class InvalidRefreshTokenException(SessionException):
    code = "INVALID_REFRESH_TOKEN"
    message = "Invalid refresh token."


# ==========================================================
# Authorization
# ==========================================================


class AuthorizationException(IdentityException):
    code = "UNAUTHORIZED"
    message = "Unauthorized."


# ==========================================================
# Tokens
# ==========================================================


class TokenException(IdentityException):
    code = "TOKEN_ERROR"
    message = "Token error."


class InvalidTokenException(TokenException):
    code = "INVALID_TOKEN"
    message = "Invalid token."


class ExpiredTokenException(TokenException):
    code = "TOKEN_EXPIRED"
    message = "Token expired."