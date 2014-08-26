# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

import pytest

if six.PY3:
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


@pytest.fixture
def storage():
    return MagicMock()


@pytest.fixture
def environment():
    return MagicMock()
