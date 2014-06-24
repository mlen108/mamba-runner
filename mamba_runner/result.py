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
    _prev_class = None
    _terminal = Terminal()
    # all results are buffered as a string & being output after all tests
    # are executed. it is string type because operations on it are faster than
    # on any other data structure.
    _results = ''

    def __init__(self, stream, descriptions, verbosity):
        super(BlackMambaTestResult, self).__init__(
            stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions

    def startTest(self, test):
        super(BlackMambaTestResult, self).startTest(test)
        self.startTime = time.time()
        if self.showAll:
            if self._prev_class != test.__class__:
                self._prev_class = test.__class__
                self._results += '${}+'.format(strclass(self._prev_class))

    def stopTestRun(self):
        """Output time results after all tests are executed."""
        if self._results:
            title = "\nBelow tests seem to be slow:\n"
            self.stream.writeln(self._terminal.bold_red(title))

            items = self._results.split('$')[1:]
            for i in items:
                klass, methods = i.split('+')
                methods = methods.split(';')[:-1]
                if methods:
                    self.stream.writeln(self._terminal.blue(klass))

                for m in methods:
                    _secs, method, status = m.split('#')
                    secs = float(_secs)
                    if secs >= 0.1 and secs < 0.5:
                        color = self._terminal.yellow
                    elif secs >= 0.5 and secs < 1:
                        color = self._terminal.magenta
                    elif secs >= 1:
                        color = self._terminal.bold_red

                    _secs = color("[{}s]".format(_secs))
                    self.stream.writeln(
                        "    {} ... {} {}".format(method, _secs, status)
                    )
            self.stream.writeln('')

    def collectResult(self, status, test):
        if not self.showAll:
            return

        # for more real timings the run-time has to be calculated here
        # and not in `stopTest` method
        run_time = time.time() - self.startTime

        is_slow = run_time >= 0.1
        if is_slow or status in ('ERROR', 'FAIL'):
            run_time = "{0:.3f}".format(run_time)
            self._results += '{}#{}#{};'.format(
                run_time, test._testMethodName, status)

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
