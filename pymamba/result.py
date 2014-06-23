from unittest import result
from unittest.util import strclass

from blessings import Terminal
try:
    text_type = unicode
except NameError:
    # Python3
    text_type = str


class BlackMambaTestResult(result.TestResult):
    """
    A test result class that adds time execution for every unittest test run.

    Based on https://github.com/python/cpython/blob/3.3/Lib/unittest/runner.py
    """

    def __init__(self, stream, descriptions, verbosity):
        super(BlackMambaTestResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions
