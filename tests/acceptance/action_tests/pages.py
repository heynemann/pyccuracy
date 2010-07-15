#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyccuracy import Page

class TestCustomPage(Page):
    url = "page_tests.htm"

    def register(self):
        self.quick_register(u"custom wait for visible", "#divWaitForVisible")
        self.quick_register(u"custom wait for invisible", "#divWaitForInvisible")

class OtherPage(Page):
    url = "page_tests.html"

    def register(self):
        self.quick_register(u"text", "#divText3")

class GoogleSearch(Page):
    url = "http://www.google.com/"

    def register(self):
        self.register_element('query', '//input[@name="q"]')
        self.register_element('search', '//input[@name="btnG"]')

class YahooSearch(Page):
    url = "http://search.yahoo.com/search?p=<query>"

    def register(self):
        self.register_element('search', '//input[@id="yschsp"]')

class OtherYahooSearch(Page):
    url = "http://search.yahoo.com/search?p=<query>&b=<offset>"

    def register(self):
        self.register_element('search', '//input[@id="yschsp"]')
        self.register_element('page', '//div[@id="pg"]//strong')
