from datetime import (
    datetime,
    timedelta,
    timezone,
)

from app.core.jwt import create_access_token

from app.models.auth_session import AuthSession

from app.repositories.auth_session import AuthSessionRepository


class AuthSessionService:

    def __init__(
        self,
        db,
    ):
        self.sessions = AuthSessionRepository(
            db,
        )

    # ----------------------------------
    # Create Session
    # ----------------------------------

    def create(
        self,
        id: str,
        user_id: int,
        refresh_token: str,
        device_name: str | None = None,
        ip_address: str | None = None,
        user_agent: str | None = None,
    ):

        session = AuthSession(
            id=id,
            user_id=user_id,
            refresh_token=refresh_token,
            device_name=device_name,
            ip_address=ip_address,
            user_agent=user_agent,
            is_active=True,
            expires_at=(
                datetime.now(timezone.utc)
                + timedelta(days=30)
            ),
        )

        return self.sessions.create(
            session,
        )

    # ----------------------------------
    # Refresh Access Token
    # ----------------------------------

    def refresh(
        self,
        refresh_token: str,
    ):

        session = self.sessions.get_by_refresh_token(
            refresh_token,
        )

        if session is None:
            raise ValueError(
                "Invalid refresh token."
            )

        if session.expires_at < datetime.now(timezone.utc):
            raise ValueError(
                "Session expired."
            )

        access_token = create_access_token(
            user=session.user,
            session_id=session.id,
        )

        return {
            "access_token": access_token,
        }

    # ----------------------------------
    # Logout
    # ----------------------------------

    def logout(
        self,
        refresh_token: str,
    ):

        session = self.sessions.get_by_refresh_token(
            refresh_token,
        )

        if session is None:
            raise ValueError(
                "Session not found."
            )

        self.sessions.revoke(
            session,
        )

    # ----------------------------------
    # Logout All Devices
    # ----------------------------------

    def logout_all(
        self,
        user_id: int,
    ):

        self.sessions.revoke_all(
            user_id,
        )