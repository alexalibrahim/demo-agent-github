"""
SonarQube Python — three intentional issues for demonstration.
"""


def wrong_none_check(value):
    """Compare to None should use `is`, not `==`."""
    if value == None:
        return "empty"
    return str(value)


def bare_except_swallows_errors():
    """Bare except hides bugs and system exits."""
    try:
        return 1 / 0
    except:
        return None


def return_in_finally_overrides_try():
    """Return in finally suppresses the try/except return values."""
    result = "from_finally"
    try:
        result = "from_try"
    except ZeroDivisionError:
        result = "from_except"
    return result
