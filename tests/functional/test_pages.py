# -*- coding: utf-8 -*-

from nose.tools import raises, set_trace
from pyccuracy import PageRegistry, Page

def test_get_all_by_name():
    pages = PageRegistry.all_by_name(u'Google Main Page')
    for page in pages:
        assert isinstance(page, Page)

def test_get_all_by_url():
    pages = PageRegistry.all_by_url(u'http://google.com')
    for page in pages:
        assert isinstance(page, Page)
