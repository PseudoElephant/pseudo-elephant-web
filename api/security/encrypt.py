from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"], default="pbkdf2_sha256", pbkdf2_sha256__rounds=50000,
)


def encrypt_password(password: str) -> str:
    """
    Encrypts the password
    """
    return pwd_context.hash(password)


def check_encrypted_password(password: str, hashed: str) -> bool:
    """
    If password matches its hashed form, returns true
    """
    return pwd_context.verify(password, hashed)
