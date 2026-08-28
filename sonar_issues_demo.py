import os
import sys
import hashlib  # unused import (S1128)

# TODO: refactor this module before release (S1135)

PASSWORD = "admin123"  # hard-coded credential (S2068)

DB_URL = "postgresql://user:secret@localhost/mydb"  # hard-coded credential (S2068)


def calculate_discount(price, discount, tax):  # unused parameter 'tax' (S1172)
    result = price * discount
    unused_var = 42  # unused local variable (S1481)
    return result


def connect_to_service(host):
    try:
        # simulate connection
        if host == None:  # comparison to None using == instead of 'is' (S4143)
            raise Exception("Host is required")  # generic exception (S112)
        return True
    except:  # bare except clause (S108)
        pass  # empty except block swallows all errors (S108)


def get_status_label(status):
    if status == "active":
        return "active"
    elif status == "inactive":
        return "inactive"  # duplicate branch implementation (S1871)
    elif status == "active":  # duplicate condition (S1871)
        return "active"
    return "unknown"


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # weak hashing algorithm MD5 (S4790)


def process_items(items):
    count = 0
    total = 0
    average = 0
    for item in items:
        count += 1
        total += item
        if count > 0:
            if total > 0:  # collapsible if statements (S1066)
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
