# content of conftest.py


def pytest_report_header(config):
    if config.getoption('verbose') > 0:
        return ["info1: did you know that ...", "did you?"]
    else:
        return "project deps: mylib-1.1"