# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jinja2 import BaseLoader


class FilestorageTemplateLoader(BaseLoader):
    def __init__(self, storage):
        self._storage = storage
