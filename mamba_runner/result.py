from unittest import result
from unittest.util import strclass
import time

from blessings import Terminal
try:
    text_type = unicode
except NameError:
    # Python3
    text_type = str


class BlackMambaTestResult(result.TestResult):
    """
    A test result class that adds time execution for every unittest test run.
    """
    startTime = 0
    indent = ' ' * 4
    _test_class = None
    _terminal = Terminal()
    # all results are buffered as a string & being output after all tests
    # are executed
    _results = ''

    def __init__(self, stream, descriptions, verbosity):
        super(BlackMambaTestResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions

    def getShortDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return self.indent + doc_first_line
        return self.indent + test._testMethodName

    def startTest(self, test):
        super(BlackMambaTestResult, self).startTest(test)
        self.startTime = time.time()

    def stopTestRun(self):
        """Output time results after all tests are executed."""
        if self._results:
            self.stream.write(self._results)
            self.stream.flush()

    def collectResult(self, tp, test):
        if not self.showAll:
            return

        # for more real timings the run time has to be calculated here
        # and not in `stopTest` method
        run_time = time.time() - self.startTime
        color = None
        if run_time >= 0.001 and run_time < 0.5:
            color = self._terminal.yellow
        elif run_time >= 0.5 and run_time < 1:
            color = self._terminal.magenta
        elif run_time >= 1:
            color = self._terminal.bold_red

        if color:
            title = "\n\nBelow tests seem to be slow:\n\n"
            self._results = self._terminal.bold_red(title)

            klass = strclass(test.__class__)
            self._results += "{}\n".format(self._terminal.blue(klass))
            self._results += (self.indent + test._testMethodName)
            self._results += " ... "
            self._results += color("[{0:.6f}s] {1}\n".format(run_time, tp))
        color = None

    def addSuccess(self, test):
        super(BlackMambaTestResult, self).addSuccess(test)
        self.collectResult('ok', test)

    def addError(self, test, err):
        super(BlackMambaTestResult, self).addError(test, err)
        self.collectResult('ERROR', test)

    def addFailure(self, test, err):
        super(BlackMambaTestResult, self).addFailure(test, err)
        self.collectResult('FAIL', test)

    def addSkip(self, test, reason):
        super(BlackMambaTestResult, self).addSkip(test, reason)
        self.collectResult('skipped', test)

    def addExpectedFailure(self, test, err):
        super(BlackMambaTestResult, self).addExpectedFailure(test, err)
        self.collectResult('expected failure', test)

    def addUnexpectedSuccess(self, test):
        super(BlackMambaTestResult, self).addUnexpectedSuccess(test)
        self.collectResult('unexpected success', test)
