from .runner import BlackMambaTestRunner


class BlackMambaRunnerMixin(object):
    test_runner = BlackMambaTestRunner

    def run_suite(self, suite, **kwargs):
        """This is the version from Django 1.7."""
        return self.test_runner(
            verbosity=self.verbosity,
            failfast=self.failfast,
        ).run(suite)
