import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *
from urllib import basejoin
import urllib2

import re

class PageGoToAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(PageGoToAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["page_go_to_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        if not self.last_match: return tuple([])

        groups = self.last_match.groups()

        if groups[1] != None:
            return (groups[1].replace("\"", ""),)
        else:
            return (groups[2],)

    def execute(self, values, context):
        url = values[0]
        base_url = context.base_url

        if url.replace(" ", "") in context.all_pages:
            context.current_page = context.all_pages[url.replace(" ", "")]
            url = context.current_page.url

        if base_url:
            url = basejoin(base_url + "/", url)
        
        protocol, page_name, file_name, complement, querystring, anchor = urllib2.urlparse.urlparse(url)
        
        if not protocol and not base_url:
        	url = "file://" + os.path.abspath(os.path.join(context.tests_dir, url))
        elif not protocol:
        	url = "file://" + os.path.abspath(url)
        
        self.browser_driver.page_open(url)
        self.browser_driver.wait_for_page()
