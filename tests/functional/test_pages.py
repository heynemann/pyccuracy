# -*- coding: utf-8 -*-
from pyccuracy import PageRegistry, Page
from pyccuracy.page import ElementAlreadyRegisteredError

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

def test_quick_register_registers_element_within_dict():
    class GloboPortal(Page):
        url = 'http://globo.com'
        def register(self):
            self.quick_register('logo', u"div.marca-globo > a")


    p = GloboPortal()
    expected_xpath = "//div[contains(concat(' ', normalize-space(@class), ' '), ' marca-globo ')]/a"
    assert p.registered_elements.has_key('logo')
    assert p.registered_elements['logo'] == expected_xpath

def test_should_not_allow_registering_two_elements_with_same_name():
    class GloboPortal(Page):
        url = 'http://globo.com'
        def register(self):
            self.register_element('my div', u"//div[1]")
            self.register_element('my div', u"//div[2]")

    try:
        p = GloboPortal()
        assert False, "Should not get here."
    except ElementAlreadyRegisteredError, e:
        pass

def test_should_allow_registering_two_elements_with_same_name_in_different_pages():
    class GloboPortal(Page):
        url = 'http://globo.com'
        def register(self):
            self.register_element('my div', u"//div[1]")

    class YahooPortal(Page):
        url = 'http://yahoo.com'
        def register(self):
            self.register_element('my div', u"//div[1]")

    try:
        g = GloboPortal()
        y = YahooPortal()
    except ElementAlreadyRegisteredError, e:
        assert False, "Should not get here."
