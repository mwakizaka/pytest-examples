import pytest


@pytest.fixture(scope='function', autouse=True)
def scope_function():
    print("setup before function")
    yield
    print("teardown after function")


@pytest.fixture()
def fixture_a():
    print("    setup before fixture_a")
    yield("        I am fixture_a!")
    print("    teardown after fixture_a")


@pytest.fixture()
def fixture_b():
    print("    setup before fixture_b")
    yield("        I am fixture_b!")
    print("    teardown after fixture_b")


@pytest.fixture()
def fixture_c(fixture_b):
    print("        setup before fixture_c")
    print(fixture_b)
    yield("            I am fixture_c!")
    print("        teardown after fixture_c")
