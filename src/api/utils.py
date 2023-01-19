import base64

from cryptography.fernet import Fernet

from password_manager.settings import ENCRYPT_KEY


def encrypt(password):
    f = Fernet(ENCRYPT_KEY)
    encrypted_password = f.encrypt(password.encode('ascii'))
    encrypted_password = (
        base64
        .urlsafe_b64encode(encrypted_password)
        .decode("ascii")
    )
    return encrypted_password


def decrypt(password):
    password = base64.urlsafe_b64decode(password)
    f = Fernet(ENCRYPT_KEY)
    decrypted_password = f.decrypt(password).decode("ascii")
    return decrypted_password
