import time
import pytest


def test_cx():
    time.sleep(0.1)
    assert 0


def test_cy():
    time.sleep(0.2)
    assert 1


@pytest.mark.slow
def test_cz():
    time.sleep(0.3)
    assert 0
