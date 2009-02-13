import re
from selenium_browser_driver import *
from errors import *
from action_base import *

class ElementIsVisibleBase(ActionBase):
	def __init__(self, browser_driver, language):
		ActionBase.__init__(self, browser_driver, language)
	
	def get_selector(self, element_name):
		return element_name
	
	def execute_is_visible(self, element_name, not_visible_message):
		self.assert_element_is_visible(element_name, not_visible_message % (element_name))
		