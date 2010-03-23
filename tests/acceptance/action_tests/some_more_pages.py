#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyccuracy import Page

class YetAnotherPage(Page):
    url = "page_tests.htm"

    def register(self):
        self.quick_register(u"text2", "#divText2")
