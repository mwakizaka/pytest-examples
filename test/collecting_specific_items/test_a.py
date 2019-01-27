import time
import pytest


@pytest.fixture
def new_fixture():
    return 'foobar'


def test_ax():
    time.sleep(0.1)
    assert 0


@pytest.mark.remove
def test_ay(new_fixture):
    time.sleep(0.2)
    assert 1


@pytest.mark.slow
def test_az():
    time.sleep(0.3)
    assert 0
