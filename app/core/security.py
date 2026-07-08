from passlib.context import CryptContext


pwd = CryptContext(
    schemes=[
        "bcrypt",
    ],
    deprecated="auto",
)


def hash_password(
    password: str,
) -> str:

    password_bytes = len(
        password.encode("utf-8")
    )

    print(
        "HASH PASSWORD DEBUG:",
        password,
        "BYTES:",
        password_bytes,
    )

    if password_bytes > 72:
        raise ValueError(
            "Password cannot be longer than 72 bytes."
        )

    return pwd.hash(
        password,
    )


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:

    return pwd.verify(
        plain_password,
        hashed_password,
    )