from cryptography.fernet import Fernet

def generate_key():
    """Generate and save a key"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the key from the current directory named `secret.key`"""
    return open("secret.key", "rb").read()


