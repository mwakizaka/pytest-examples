# content of test_module.py
import pytest


def test_func_fast():
    pass


@pytest.mark.slow
@pytest.mark.fast
def test_func_so_fast():
    pass