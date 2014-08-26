# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import six

if six.PY3:
    from unittest.mock import patch, call, MagicMock
else:
    from mock import patch, call, MagicMock

from jinja2_stl.loader import FilestorageTemplateLoader


class TestFilestorageTemplateLoader(object):
    def test_storage_saved_on_init(self):
        storage = MagicMock()
        loader = FilestorageTemplateLoader(storage=storage)

        assert loader._storage == storage
