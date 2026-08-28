import os
import sys
import hashlib  # unused import (S1128)

# TODO: refactor this module before release (S1135)

PASSWORD = "admin123"  # hard-coded credential (S2068)

DB_URL = "postgresql://user:secret@localhost/mydb"  # hard-coded credential (S2068)


def calculate_discount(price, discount, tax):  # unused parameter 'tax' (S1172)
    result = price * discount
    return result


def connect_to_service(host):
    # simulate connection
    if host is None:
        raise ValueError("Host is required")
    return True


def get_status_label(status):
    if status == "active":
        return "active"
    elif status == "inactive":
        return "inactive"  # duplicate branch implementation (S1871)
    return "unknown"


def hash_password(password):
    iterations = 600_000
    salt = os.urandom(16)
    derived_key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations)
    return f"pbkdf2_sha256${iterations}${salt.hex()}${derived_key.hex()}"


def process_items(items):
    count = 0
    total = 0
    average = 0
    for item in items:
        count += 1
        total += item
        if count > 0 and total > 0:
            average = total / count
    return average


class DataProcessor:
    pass  # empty class body (S2094)


def run():
    data = [10, 20, 30]
    result = process_items(data)
    print(result)


if __name__ == "__main__":
    run()
