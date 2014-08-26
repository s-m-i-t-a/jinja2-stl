# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six
import pytest

if six.PY3:
    from unittest.mock import patch, call, MagicMock
else:
    from mock import patch, call, MagicMock

from jinja2 import BaseLoader

from jinja2_stl.loader import FilestorageTemplateLoader


class TestFilestorageTemplateLoader(object):
    def test_template_loader_is_subclass_of_base_loader(self):
        assert issubclass(FilestorageTemplateLoader, BaseLoader)

    def test_storage_saved_on_init(self):
        storage = MagicMock()
        loader = FilestorageTemplateLoader(storage=storage)

        assert loader._storage == storage

    def test_get_source_return_tuple(self, storage):
        environment = MagicMock()
        loader = FilestorageTemplateLoader(storage=storage)

        result = loader.get_source(environment, 'index.html')

        assert type(result) == tuple
