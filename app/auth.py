# app/auth.py
from .models import query_user_by_username

# hardcoded secret (intentional)
HARDCODED_API_KEY = 'TOPSECRET_API_KEY_12345'

def check_credentials(username, password):
    # insecure: uses query_user_by_username which formats SQL directly
    row = query_user_by_username(username)
    if not row:
        return False
    stored_username, stored_password = row
    # plaintext comparison (intentional)
    return stored_password == password

def get_api_key():
    return HARDCODED_API_KEY
