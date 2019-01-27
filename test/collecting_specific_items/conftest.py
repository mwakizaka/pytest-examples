# content of conftest.py

import pytest
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


# def pytest_collection_modifyitems(config, items):
#     selected_items = []
#     deselected_items = []
#     for item in items:
#         if 'new_fixture' in getattr(item, 'fixturenames', ()):
#             selected_items.append(item)
#         else:
#             deselected_items.append(item)
#     config.hook.pytest_deselected(items=deselected_items)
#     items[:] = selected_items


# def pytest_collection_modifyitems(config, items):
#     if config.getoption("--runslow"):
#         # --runslow given in cli: do not skip slow tests
#         return
#     skip_slow = pytest.mark.skip(reason="need --runslow option to run")
#     for item in items:
#         if "slow" in item.keywords:
#             item.add_marker(skip_slow)
#         # elif "remove" in item.keywords:
#         #     items.remove(item)


# def pytest_deselected(items):
#     """ called for test items deselected by keyword. """
#     for item in items:
#         if "remove" in item.keywords:
#             items.remove(item)
#     print("items: " + str(items))