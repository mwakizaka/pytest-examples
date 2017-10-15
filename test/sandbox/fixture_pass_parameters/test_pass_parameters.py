def test_always_succeeds(scope_class):
    print(scope_class)
    print("            test_always_succeeds")
    assert True


def test_always_fails():
    print("            test_always_fails")
    assert False


class TestFaafaaClass():
    def test_always_succeeds_under_class(self, scope_module):
        print(scope_module)
        print("            test_always_succeeds_under_class")
        assert True

    def test_always_fails_under_class(self, scope_function):
        print(scope_function)
        print("            test_always_fails_under_class")
        assert False
