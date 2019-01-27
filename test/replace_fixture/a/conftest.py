import pytest
from test.sandbox.replace_fixture.singletonobj.operator import Operator


@pytest.fixture
def new_fixture():
    operator = Operator()
    return operator
