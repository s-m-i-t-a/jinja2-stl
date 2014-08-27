==================================
Jinja2 Filestorage Template Loader
==================================

.. image:: https://badge.fury.io/py/jinja2-stl.png
    :target: http://badge.fury.io/py/jinja2-stl

.. image:: https://travis-ci.org/s-m-i-t-a/jinja2-stl.png?branch=master
    :target: https://travis-ci.org/s-m-i-t-a/jinja2-stl

.. image:: https://coveralls.io/repos/s-m-i-t-a/jinja2-stl/badge.png
        :target: https://coveralls.io/r/s-m-i-t-a/jinja2-stl


A Filestorage template loader for Jinja2.


Features
--------

* Load templates from *Django like* storage
* Free software: MIT license


Quickstart
----------
Install jinja2_stl::

    pip install jinja2_stl

Basic usage::

    from jinja2 import Environment

    from storage import Storage

    from jinja2_stl.loader import FilestorageTemplateLoader


    loader = FilestorageTemplateLoader(storage=Storage(...))
    env = Environment(loader=loader)

    template = env.get_template('foo/bar.html')

    print(template.render(the='variables', go='here'))

``Storage`` must implements `Django Storage API <https://docs.djangoproject.com/en/1.6/ref/files/storage/#the-storage-class>`_ and is used as storage parameter in ``FilestorageTemplateLoader``. The template ``foo/bar.html`` is loaded from ``Storage`` then is used in convenience way.
