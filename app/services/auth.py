from sqlalchemy.orm import Session

from app.core.id import generate_id

from app.core.jwt import (
    create_access_token,
    create_refresh_token,
)

from app.core.security import (
    hash_password,
    verify_password,
)

from app.models.user import User

from app.repositories.user import UserRepository

from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
)

from app.services.auth_session import AuthSessionService


class AuthService:

    def __init__(
        self,
        db: Session,
    ):
        self.users = UserRepository(
            db,
        )

        self.session_service = AuthSessionService(
            db,
        )


    # ----------------------------------
    # Register
    # ----------------------------------

    def register(
        self,
        request: RegisterRequest,
    ) -> User:

        existing = self.users.get_by_email(
            request.email,
        )

        if existing:
            raise ValueError(
                "Email already exists."
            )


        user = User(
            public_id=generate_id("usr"),
            email=request.email,
            password_hash=hash_password(
                request.password,
            ),
            display_name=request.display_name,
        )


        return self.users.create(
            user,
        )


    # ----------------------------------
    # Login
    # ----------------------------------

    def login(
        self,
        request: LoginRequest,
    ) -> TokenResponse:

        user = self.users.get_by_email(
            request.email,
        )


        if user is None:
            raise ValueError(
                "Invalid credentials."
            )


        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid credentials."
            )


        # ----------------------------------
        # Create Session ID first
        # ----------------------------------

        session_id = generate_id(
            "ses",
        )


        # ----------------------------------
        # Create Refresh Token
        # ----------------------------------

        refresh_token = create_refresh_token(
            user_id=user.id,
            session_id=session_id,
        )


        # ----------------------------------
        # Save Session
        # ----------------------------------

        session = self.session_service.create(
            id=session_id,
            user_id=user.id,
            refresh_token=refresh_token,
        )


        # ----------------------------------
        # Create Access Token
        # ----------------------------------

        access_token = create_access_token(
            user=user,
            session_id=session.id,
        )


        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )


    # ----------------------------------
    # Current User
    # ----------------------------------

    def me(
        self,
        user_id: int,
    ):

        user = self.users.get_by_id(
            user_id,
        )


        if user is None:
            raise ValueError(
                "User not found."
            )


        return {
            "id": user.public_id,
            "email": user.email,
            "display_name": user.display_name,
            "email_verified": user.email_verified,
            "phone_verified": user.phone_verified,
        }