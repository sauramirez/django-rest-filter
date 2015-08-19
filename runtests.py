#! /usr/bin/env python
from __future__ import print_function

import sys

import pytest

PYTEST_ARGS = {
    'default': ['tests', '--tb=short', '-s'],
    'fast': ['tests', '--tb=short', '-q', '-s'],
}


def exit_on_failure(ret, message=None):
    if ret:
        sys.exit(ret)


if __name__ == "__main__" or __name__ == 'runtests':
    run_tests = True

    pytest_args = PYTEST_ARGS['default']
    if run_tests:
        exit_on_failure(pytest.main(pytest_args))
