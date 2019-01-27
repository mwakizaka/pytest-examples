import time
import pytest


def test_ax(new_fixture):
    time.sleep(0.1)
    print("\n new_fixture:" + str(new_fixture))
    assert 0


@pytest.mark.remove
def test_ay():
    time.sleep(0.2)
    assert 1


@pytest.mark.slow
def test_az():
    time.sleep(0.3)
    assert 0
