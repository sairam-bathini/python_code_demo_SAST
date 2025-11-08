# vuln_scripts/hardcoded_secrets.py
# hardcoded secrets and weak hashing demo

API_KEY = 'THIS_IS_A_DEMO_HARDCODED_API_KEY'

import hashlib

def hash_password(password):
    # insecure: sha1 without salt (intentional)
    return hashlib.sha1(password.encode()).hexdigest()

if __name__ == '__main__':
    print('Hardcoded key:', API_KEY)
    print('Hash of "password":', hash_password('password'))
