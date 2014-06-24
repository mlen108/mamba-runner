from unittest import runner

from .result import BlackMambaTestResult


class BlackMambaTestRunner(runner.TextTestRunner):
    resultclass = BlackMambaTestResult
