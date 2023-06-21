import hashlib
import decimal


def hash_password(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()


def normalise_number(num):
    # return str(decimal.Decimal(num or 0).normalize())
    return "{:.2f}".format(float(num or 0))
