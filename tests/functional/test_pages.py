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

def test_register_element_registers_element_within_dict():
    class GloboPortal(Page):
        url = 'http://globo.com'
        def register(self):
            self.register_element('logo', u"div[contains(@class, 'marca-globo')]/a")


    p = GloboPortal()

    assert p.registered_elements.has_key('logo')
    assert p.registered_elements['logo'] == u"div[contains(@class, 'marca-globo')]/a"

def test_register_css_element_registers_element_within_dict():
    class GloboPortal(Page):
        url = 'http://globo.com'
        def register(self):
            self.register_css_element('logo', u"div.marca-globo > a")


    p = GloboPortal()
    expected_xpath = u"descendant-or-self::div[contains(concat" \
                     "(' ', normalize-space(@class), ' '), ' marca-globo ')]/a"
    assert p.registered_elements.has_key('logo')
    assert p.registered_elements['logo'] == expected_xpath

