import pytest


@pytest.fixture(scope='session', autouse=True)
def scope_session():
    print("setup before session")
    yield("    I am session fixture!")
    print("teardown after session")


@pytest.fixture(scope='module', autouse=True)
def scope_module(scope_session):
    print("    setup before module")
    print(scope_session)
    yield("        I am module fixture!")
    print("    teardown after module")


@pytest.fixture(scope='class', autouse=True)
def scope_class(scope_module):
    print("        setup before class")
    print(scope_module)
    yield("            I am class fixture!")
    print("        teardown after class")


@pytest.fixture(scope='function', autouse=True)
def scope_function(scope_class):
    print("            setup before function")
    print(scope_class)
    yield("                I am function fixture!")
    print("            teardown after function")

