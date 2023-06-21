import hashlib


def hash_password(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()
