import secrets

def generate_local_secret():
    return secrets.token_hex(32)