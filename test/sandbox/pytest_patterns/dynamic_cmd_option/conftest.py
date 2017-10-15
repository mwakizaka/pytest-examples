# content of conftest.py
import sys
import pytest


def pytest_cmdline_preparse(args):
    if 'xdist' in sys.modules: # pytest-xdist plugin
        import multiprocessing
        num = int(max(multiprocessing.cpu_count() / 2, 1))
        # print("num: " + str(num))
        args[:] = ["-n", str(num)] + args
        # args[:] = ["-n", str(num)] + ["--tx", f"{str(num)}*popen//python=python3.6.1"] + args
        print("after args: " + str(args))


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="type1",
                     help="my option: type1 or type2")


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
