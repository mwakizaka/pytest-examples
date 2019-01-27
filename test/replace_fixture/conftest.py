import pytest
from _pytest._pluggy import HookspecMarker
from test.sandbox.replace_fixture.singletonobj.operator import Operator

hookspec = HookspecMarker("pytest")


# @hookspec(firstresult=True)
# def pytest_fixture_setup(fixturedef, request):
#     """ performs fixture setup execution.
#
#     Stops at first non-None result, see :ref:`firstresult` """
#     print("pytest_fixture_setup")
#     fixturedef = new_new_fixture


@hookspec(firstresult=True)
def pytest_runtestloop(session):
    """ called for performing the main runtest loop
    (after collection finished).
    
    Stops at first non-None result, see :ref:`firstresult` """
    operator = Operator()
    print("Operator" + str(operator))
    print("==================")
    print("pytest_runtestloop")
    print("==================")


def pytest_runtest_setup(item):
    """ called before ``pytest_runtest_call(item)``. """
    # print("pytest_runtest_setup")


def pytest_runtest_call(item):
    """ called to execute the test ``item``. """
    # print("pytest_runtest_call")


def pytest_runtest_teardown(item, nextitem):
    """ called after ``pytest_runtest_call``.

    :arg nextitem: the scheduled-to-be-next test item (None if no further
                   test item is scheduled).  This argument can be used to
                   perform exact teardowns, i.e. calling just enough finalizers
                   so that nextitem only needs to call setup-functions.
    """
    # print("pytest_runtest_teardown")


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true",
                     default=False, help="run slow tests")


def pytest_collection_modifyitems(config, items):
    selected_items = []
    deselected_items = []
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
            selected_items.append(item)
        elif "remove" in item.keywords:
            deselected_items.append(item)
        else:
            selected_items.append(item)

    config.hook.pytest_deselected(items=deselected_items)
    items[:] = selected_items
