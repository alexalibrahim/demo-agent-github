"""
Bugs - Contains various bug patterns that Sonar detects
"""

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


# Mutable default argument
def append_to_list(item, lst=None):
    """Mutable default argument bug"""
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# Unreachable code
def unreachable_code():
    """Contains unreachable code"""
    return "early return"
    print("This will never execute")
    x = 5
    return x


# Division by zero risk
def risky_division(a, b):
    """No check for division by zero"""
    return a / b


# Unused variables
def unused_variables():
    """Contains unused variables"""
    x = 10
    y = 20
    return x + y


# Missing exception handling
def no_exception_handling(filename):
    """No exception handling for file operations"""
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content


# Bare except clause
def bare_except():
    """Using bare except clause"""
    try:
        result = 10 / 0
    except:
        pass


# Ignoring return value
def ignoring_return_value():
    """Ignoring return values"""
    list1 = [1, 2, 3]
    list1.sort()  # sort() returns None but modifies in place
    return list1.append(4)  # append returns None


# Comparing to None with ==
def wrong_none_comparison(value):
    """Wrong way to compare to None"""
    if value == None:
        return True
    return False


# Using assert for validation
def using_assert_for_validation(age):
    """Assert should not be used for validation"""
    assert age > 0, "Age must be positive"
    return age * 2


# Lost exception
def lost_exception():
    """Exception is caught but not logged or handled"""
    try:
        result = risky_operation()
    except Exception:
        result = None
    return result


def risky_operation():
    return 1 / 0


# Race condition
import threading

counter = 0

def increment_counter():
    """Race condition - no synchronization"""
    global counter
    for _ in range(1000):
        counter += 1


# Infinite loop potential
def potential_infinite_loop(x):
    """Potential infinite loop"""
    while x > 0:
        print(x)
        if x == 5:
            x -= 1


# String concatenation in loop
def inefficient_string_concat(items):
    """Inefficient string concatenation"""
    result = ""
    for item in items:
        result = result + str(item) + ","
    return result


# Modifying list while iterating
def modifying_during_iteration(items):
    """Modifying list while iterating"""
    for item in items:
        if item > 5:
            items.remove(item)
    return items


# Return in finally
def return_in_finally():
    """Return in finally block"""
    try:
        return "try"
    except:
        return "except"
    finally:
        return "finally"


# Boolean parameter
def boolean_parameter(flag):
    """Using boolean parameter instead of two functions"""
    if flag:
        return "option A"
    else:
        return "option B"


# Class with only static methods
class UtilityClass:
    """Class with only static methods should be a module"""
    
    @staticmethod
    def method1():
        return 1
    
    @staticmethod
    def method2():
        return 2


# Empty except block
def empty_except_block():
    """Empty except block"""
    try:
        dangerous_operation()
    except ValueError:
        pass
    except TypeError:
        pass


def dangerous_operation():
    raise ValueError("Error")


# Assignment in conditional
def assignment_in_conditional():
    """Assignment in conditional"""
    x = 10
    if y := x + 5:
        return y
    return x
