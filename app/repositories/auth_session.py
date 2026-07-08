from sqlalchemy.orm import Session

from app.models.auth_session import (
    AuthSession,
)


class AuthSessionRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    # ----------------------------------
    # Create
    # ----------------------------------

    def create(
        self,
        session: AuthSession,
    ):

        self.db.add(
            session,
        )

        self.db.commit()

        self.db.refresh(
            session,
        )

        return session

    # ----------------------------------
    # Read
    # ----------------------------------

    def get_by_refresh_token_hash(
        self,
        refresh_token_hash: str,
    ):

        return (
            self.db.query(
                AuthSession,
            )
            .filter(
                AuthSession.refresh_token_hash
                == refresh_token_hash,
                AuthSession.is_active == True,
            )
            .first()
        )

    # ----------------------------------
    # Update
    # ----------------------------------

    def update(
        self,
        session: AuthSession,
    ):

        self.db.commit()

        self.db.refresh(
            session,
        )

        return session

    # ----------------------------------
    # Revoke Session
    # ----------------------------------

    def revoke(
        self,
        session: AuthSession,
    ):

        session.is_active = False

        self.db.commit()

        self.db.refresh(
            session,
        )

        return session

    # ----------------------------------
    # Revoke All Sessions
    # ----------------------------------

    def revoke_all(
        self,
        user_id: int,
    ):

        (
            self.db.query(
                AuthSession,
            )
            .filter(
                AuthSession.user_id == user_id,
                AuthSession.is_active == True,
            )
            .update(
                {
                    "is_active": False,
                }
            )
        )

        self.db.commit()