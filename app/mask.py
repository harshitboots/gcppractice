def mask_email(email: str) -> str:
    """
    Mask email for PII protection.
    Example: john.doe@gmail.com → j***@gmail.com
    """
    try:
        name, domain = email.split("@")
        return name[0] + "***@" + domain
    except Exception:
        return "masked@example.com"