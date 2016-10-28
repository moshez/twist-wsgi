Twisted as a WSGI Container
===========================

This has some proofs of concept for using Twisted
as a WSGI container, using :code:`twist`.

The "XX_manage.py" are runnable examples that showcase
using "twist", even in the face of non-installed-packages.

There is also a twist plugin to show a Frankenstenian
monster of three WSGI applications, written in different
frameworks, a static file server and a cron-like task
executing every second. This illustrates the flexibility
of using Twisted as a WSGI container -- though, possibly,
not an ideal coding pattern.
