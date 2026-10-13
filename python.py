def calculate_discount(price, rate):
    tax = price * 0.2   # unused
    discount = price * rate
    return price - discount

import os
import hashlib


# Hard-coded credentials (Security Hotspot / vulnerability)
PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"


# SQL injection risk
def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query


# Unused import and unused local variable
def process_data():
    result = hashlib.md5(b"data").hexdigest()
    unused_var = 42
    return result


# Empty function
def do_nothing():
    pass


# Duplicate code block
def calculate_area_circle(r):
    pi = 3.14159
    area = pi * r * r
    return area


def calculate_area_circle2(r):
    pi = 3.14159
    area = pi * r * r
    return area


# UNBLOCKED: python:S1763 — all branches of ternary are identical (agent CAN fix)
def redundant_ternary(x):
    return True
