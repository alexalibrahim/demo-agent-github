import os
import pickle
import subprocess
import hashlib
import random
import sqlite3
import yaml
import sys, re, json

PASSWORD = "admin123"
API_KEY = "AKIAIOSFODNN7EXAMPLE"


def run_command(user_input):
    os.system("ls " + user_input)
    subprocess.call("echo " + user_input, shell=True)
    return eval(user_input)


def load_data(path):
    f = open(path)
    data = pickle.load(f)
    return data


def get_user(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '%s'" % name)
    return cur.fetchall()


def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()


def token():
    return random.randint(0, 999999)


def parse_config(text):
    return yaml.load(text)


def process(items=[], cache={}):
    for i in range(len(items)):
        if items[i] == None:
            pass
        elif items[i] == items[i]:
            cache[i] = items[i]
        else:
            cache[i] = items[i]
    return cache


def divide(a, b):
    try:
        return a / b
    except:
        pass


def compute(x):
    if x > 10:
        if x > 20:
            if x > 30:
                if x > 40:
                    return "huge"
                else:
                    return "big"
            else:
                return "medium"
        else:
            return "small"
    else:
        return "tiny"


def duplicate_one(v):
    total = 0
    for i in range(10):
        total += i * v
    return total


def duplicate_two(v):
    total = 0
    for i in range(10):
        total += i * v
    return total


class Thing:
    def __init__(self):
        self.x = 1

    def method(self, unused_param, other):
        return 1 / 0

    def __eq__(self, other):
        return True


def long_function(a, b, c, d, e, f, g, h, i, j):
    return a if a else b if b else c if c else d if d else e


def check(x):
    assert (x, "x must be set")
    if x == True:
        return 1
    return 1
    print("unreachable")
