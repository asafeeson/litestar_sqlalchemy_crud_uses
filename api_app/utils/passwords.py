import os
import hashlib
import base64
import hmac
from core.logging import get_logger


log = get_logger('authentication')

SALT_SIZE = 16
HASH_ALGO = 'sha256'

def hash_password(password: str, iterations: int = 100_000) -> str:
    salt = os.urandom(SALT_SIZE)
    key = hashlib.pbkdf2_hmac(HASH_ALGO, password.encode('utf-8'), salt, iterations)
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    key_b64 = base64.b64encode(key).decode('utf-8')
    
    return f"{iterations}${salt_b64}${key_b64}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        iterations_str, salt_b64, key_b64 = stored_hash.split('$')
        iterations = int(iterations_str)
        salt = base64.b64decode(salt_b64)
        stored_key = base64.b64decode(key_b64)
        new_key = hashlib.pbkdf2_hmac(HASH_ALGO, password.encode('utf-8'), salt, iterations)
        return hmac.compare_digest(stored_key, new_key)
        
    except Exception as e:
        log.error(e)
        return False