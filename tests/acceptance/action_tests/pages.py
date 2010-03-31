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
