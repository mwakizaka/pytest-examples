import pytest


def test_always_succeeds(scope_module):
    print(scope_module)
    print("                test_always_succeeds")
    assert True


def test_always_fails():
    print("                test_always_fails")
    assert False


class TestFaafaaClass():
    def test_always_succeeds_under_class(self, scope_module):
        print(scope_module)
        print("                test_always_succeeds_under_class")
        assert True

    def test_always_fails_under_class(self):
        print("                test_always_fails_under_class")
        assert False
