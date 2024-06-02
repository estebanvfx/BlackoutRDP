import secrets
import string

def generate_user_id(length=30):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(length))