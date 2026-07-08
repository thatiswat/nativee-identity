import secrets


def generate_id(
    prefix: str,
) -> str:
    """
    Example:

    usr_8GkPz7X...
    org_Ld92...
    ses_ab82...
    """

    return (
        f"{prefix}_"
        f"{secrets.token_urlsafe(16)}"
    )