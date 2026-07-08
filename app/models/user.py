from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
)

from sqlalchemy.sql import func

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    public_id = Column(
        String,
        unique=True,
        index=True,
        nullable=False,
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=True,
    )

    phone = Column(
        String,
        unique=True,
        index=True,
        nullable=True,
    )

    password_hash = Column(
        String,
        nullable=False,
    )

    display_name = Column(
        String,
        nullable=True,
    )

    avatar = Column(
        String,
        nullable=True,
    )

    email_verified = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    phone_verified = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )