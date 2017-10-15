import pytest
import os


def pytest_configure(config):
    if is_master(config):
        config.shared_directory = os.makedirs('/tests/runs/')


def pytest_configure_node(self, node):
    """xdist hook"""
    node.slaveinput['shared_dir'] = node.config.shared_directory


@pytest.fixture
def shared_directory(request):
    if is_master(request.config):
        return request.config.shared_directory
    else:
        return request.config.slaveinput['shared_dir']


def is_master(config):
    """True if the code running the given pytest.config object is running in a xdist master
    node or not running xdist at all.
    """
    return not hasattr(config, 'slaveinput')