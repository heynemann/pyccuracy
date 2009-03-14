import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class LinkHasTextOfAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(LinkHasTextOfAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["link_has_text_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple([])

    def execute(self, values, context):
        link_name = values[0]		
        text = values[1]
        link = self.resolve_element_key(context, Page.Link, link_name)
        self.assert_element_is_visible(link, self.language["link_is_visible_failure"] % link_name)        
        
        error_message = self.language["link_has_text_failure"]
        current_text = self.browser_driver.get_link_text(link)
        if text.lower() != current_text.lower():
            self.raise_action_failed_error(error_message % (link_name, text, current_text))

