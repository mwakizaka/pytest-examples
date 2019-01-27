import time
import pytest


def test_bx():
    time.sleep(0.1)
    assert 0


def test_by():
    time.sleep(0.2)
    assert 1


@pytest.mark.slow
def test_bz():
    time.sleep(0.3)
    assert 0
