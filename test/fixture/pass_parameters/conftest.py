import pytest


@pytest.fixture(scope='module', autouse=True)
def scope_module():
    print("setup before module")
    yield("    I am module fixture!")
    print("teardown after module")


@pytest.fixture(scope='class', autouse=True)
def scope_class(scope_module):
    print("    setup before class")
    print(scope_module)
    yield "        I am class fixture!"
    print("    teardown after class")


@pytest.fixture(scope='function', autouse=True)
def scope_function(scope_class):
    print("        setup before function")
    print(scope_class)
    yield("            I am function fixture!")
    print("        teardown after function")

