import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.errors import ActionFailedError

class ActionBase(object):
    def __init__(self, browser_driver, language):
        self.browser_driver = browser_driver
        self.language = language

    def raise_action_failed_error(self, message):
        raise ActionFailedError(message)

    def is_element_visible(self, selector):
        is_visible = self.browser_driver.is_element_visible(selector)
        return is_visible

    def assert_element_is_visible(self, selector, message):
        if not self.is_element_visible(selector):
            self.raise_action_failed_error(message)

    def assert_element_is_not_visible(self, selector, message):
        if self.is_element_visible(selector):
            self.raise_action_failed_error(message)
    
    def resolve_element_key(self, context, element_type, element_key):
        if context.current_page == None: return self.browser_driver.resolve_element_key(context, element_type, element_key)
        return context.current_page.get_registered_element(element_type, element_key)
        
    def is_element_empty(self, selector):
        is_empty = self.browser_driver.is_element_empty(selector)
        return is_empty 

    def assert_element_is_empty(self, selector, message):
        if not self.is_element_empty(selector):
            self.raise_action_failed_error(message)
            
    def assert_element_is_not_empty(self, selector, message):
        if self.is_element_empty(selector):
            self.raise_action_failed_error(message) 
            
