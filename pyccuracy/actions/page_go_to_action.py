import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

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
        
        if url.replace(" ", "") in context.all_pages:
            context.current_page = context.all_pages[url.replace(" ", "")]
            url = context.current_page.url
        
        if self.is_url(url):
            new_url = url
        elif context.base_url != None:
            new_url = os.path.join("file://" + os.path.abspath(context.base_url), url)
        else:            new_url = os.path.join("file://" + os.path.abspath(context.tests_path), url)
                
        self.browser_driver.page_open(new_url)
        self.browser_driver.wait_for_page()
        
    def is_url(self, url):
        url_regex = re.compile(r"^(?#Protocol)(?:(?:ht|f)tp(?:s?)\:\/\/|~/|/)?(?#Username:Password)(?:\w+:\w+@)?(?#Subdomains)(?:(?:[-\w]+\.)+(?#TopLevel Domains)(?:com|org|net|gov|mil|biz|info|mobi|name|aero|jobs|museum|travel|[a-z]{2}))(?#Port)(?::[\d]{1,5})?(?#Directories)(?:(?:(?:/(?:[-\w~!$+|.,=]|%[a-f\d]{2})+)+|/)+|\?|#)?(?#Query)(?:(?:\?(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)(?:&(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)*)*(?#Anchor)(?:#(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)?$")
        return url_regex.match(url)
