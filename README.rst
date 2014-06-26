mamba-runner
============

.. image:: https://pypip.in/version/mamba-runner/badge.png
  :target: https://pypi.python.org/pypi/mamba-runner/

.. image:: https://pypip.in/download/mamba-runner/badge.png
  :target: https://pypi.python.org/pypi/mamba-runner/

How fast are your unittest tests? Time it and make it faster!

Why?
----

This functionality `is missing <http://bugs.python.org/issue4080>`_ from Python's
`unittest <https://docs.python.org/3/library/unittest.html>`_ module.

What?
-----

``mamba-runner`` is derived from `black mamba <http://en.wikipedia.org/wiki/Black_mamba>`_ snake
(don't click if you suffer to `ophidiophobia <http://en.wikipedia.org/wiki/Ophidiophobia>`_!).

This snake runs very fast so should your tests! ;-)

See?
----

Before:

.. image:: https://github.com/mattack108/mamba-runner/raw/master/img/before_run.png

After:

.. image:: https://github.com/mattack108/mamba-runner/raw/master/img/after_run.png

Try?
----
::

    pip install mamba-runner

Django?
-------

Add the ``mamba-runner`` to your test runner: ::

    from django.test.runner import DiscoverRunner  # Django1.6's default
    from mamba_runner.django_runner import BlackMambaRunnerMixin

    class MyTestRunner(BlackMambaRunnerMixin, DiscoverRunner):
       pass

Other snake?
------------

Use ``mamba_runner.runner.BlackMambaTestRunner`` instead of ``unittest.TextTestRunner``.
