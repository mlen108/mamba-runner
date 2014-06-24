## pymamba

How fast are your unittest tests? Time it and make it faster!

### Why?

This functionality [is missing](http://bugs.python.org/issue4080) from Python's
[unittest](https://docs.python.org/3/library/unittest.html) module.

### What?

`pymamba` is derived from [black mamba](http://en.wikipedia.org/wiki/Black_mamba) snake
(don't click if you suffer to [ophidiophobia](http://en.wikipedia.org/wiki/Ophidiophobia)!).

The purpose of this module is to make your tests as fast as the black mamba snake!

### See?

Before:

After:

### Try?

    pip install pymamba

#### Django?

Add the black mamba to your test runner:

    from django.test.runner import DiscoverRunner  # Django1.6's default
    from pymamba.django_runner import BlackMambaRunnerMixin

    class MyTestRunner(BlackMambaRunnerMixin, DiscoverRunner):
       pass

#### Other snake?

Use `runner.BlackMambaTestRunner` instead of `unittest.TextTestRunner`.
