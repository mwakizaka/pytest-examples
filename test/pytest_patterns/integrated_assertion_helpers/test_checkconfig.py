# content of test_checkconfig.py
import pytest
def checkconfig(x):
    __tracebackhide__ = True
    if not hasattr(x, "config"):
        pytest.fail("not configured: %s" %(x,))


def test_something():
    checkconfig(42)