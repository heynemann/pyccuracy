# -*- coding: utf-8 -*-

from nose.tools import raises, set_trace
from pyccuracy import PageRegistry, Page

class GoogleMainPage(Page):
    url = 'http://google.com'

class GoogleSearchPage(Page):
    url = 'http://google.com'

def test_get_by_name():
    page = PageRegistry.get_by_name(u'Google Main Page')
    assert issubclass(page, Page)

def test_get_all_by_url():
    pages = PageRegistry.all_by_url('http://google.com')
    for page in pages:
        assert issubclass(page, Page)
