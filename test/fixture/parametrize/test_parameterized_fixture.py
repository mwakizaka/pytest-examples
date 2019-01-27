import pytest


@pytest.fixture
def fixture_a():
    yield 1


@pytest.fixture
def fixture_b():
    yield 2


@pytest.fixture
def fixture_c():
    yield 3


@pytest.fixture(params=['a', 'b', 'c'])
def context(request):
    if request.param == 'a':
        return (1, request.getfixturevalue('fixture_a'))
    elif request.param == 'b':
        return (2, request.getfixturevalue('fixture_b'))
    elif request.param == 'c':
        return (4, request.getfixturevalue('fixture_c'))


def test_fixture_parameterize(context):
    expected, generated = context
    assert expected == generated