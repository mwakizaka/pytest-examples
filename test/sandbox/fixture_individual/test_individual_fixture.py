import pytest


def test_always_succeeds(fixture_a, fixture_b):
    print(fixture_a)
    print(fixture_b)
    print("            test_always_succeeds")
    assert True


def test_always_fails(fixture_b, fixture_a):
    print(fixture_b)
    print(fixture_a)
    print("            test_always_fails")
    assert False

class TestFaafaaClass():
    def test_always_succeeds_under_class(self, fixture_c):
        print(fixture_c)
        print("            test_always_succeeds_under_class")
        assert True

    def test_always_fails_under_class(self, fixture_c, fixture_b):
        print(fixture_c)
        print(fixture_b)
        print("            test_always_fails_under_class")
        assert False
