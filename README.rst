Markdown No Lazy Code Extension
--------------------------------

.. image:: https://pypip.in/download/Markdown-No-Lazy-Code-Extension/badge.png
    :target: https://pypi.python.org/pypi/Markdown-No-Lazy-Code-Extension/
    :alt: Downloads


This is Markdown extension which disables lazy code blocks. By default if you have
code block separated by a newline Markdown will render them as one. This extension
allows code blocks separated by newline to be rendered separately.

To see this in action checkout:
http://atodorov.org/blog/2013/02/13/secure-vnc-installation-red-hat-enterprise-linux/

To make use of this extension:

    md = Markdown(extensions=['nlcx.nlcx'])


Contributing
============

Source code and issue tracker are at https://github.com/atodorov/Markdown-No-Lazy-Code-Extension
