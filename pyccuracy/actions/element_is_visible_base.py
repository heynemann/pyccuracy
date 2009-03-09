from pyccuracy.errors import *
from pyccuracy.actions.element_selector import *
from pyccuracy.actions.action_base import *
from pyccuracy.actions.element_is_visible_base import *

class ElementIsVisibleBase(ActionBase):
    def __init__(self, browser_driver, language):
        super(ElementIsVisibleBase, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return element_name

    def execute_is_visible(self, element_name, not_visible_message):
        element = self.get_selector(element_name)
        self.assert_element_is_visible(element, not_visible_message % (element_name))

    def execute_is_not_visible(self, element_name, visible_message):
        element = self.get_selector(element_name)
        self.assert_element_is_not_visible(element, visible_message % (element_name))
