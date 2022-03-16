# -*- coding: utf-8 -*-
# This is a test file intended to be used with pytest
# pytest automatically runs all the function starting with "test_"
# see https://docs.pytest.org for more information

from remote_library import my_function


def test_dummy_function():
    dummy_results = my_function.do_something()
    assert dummy_results == 5