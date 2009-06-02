#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyccuracy import Page

class TestCustomPage2(Page):
    url = "page_tests.htm"

    def register(self):
        self.register_element(u"custom wait for visible", "//div[@id='divWaitForVisible']")
        self.register_element(u"custom wait for invisible", "//div[@id='divWaitForInvisible']")
