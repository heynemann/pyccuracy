import re
from selenium_browser_driver import *
from errors import *

class ElementIsVisibleHelper(object):
	def __init__(self, browser_driver, language):
		self.browser_driver = browser_driver
		self.language = language
	
	def get_selector(self, element_name):
		return element_name
	
	def execute_is_visible(self, element_name, not_visible_message):
		selector = self.get_selector(element_name)
		is_visible = self.browser_driver.is_element_visible(selector)
		if not is_visible:
			raise ActionFailedError(not_visible_message % (element_name))