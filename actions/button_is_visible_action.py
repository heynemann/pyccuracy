import re
from selenium_browser_driver import *

class ButtonIsVisibleAction(object):
	def __init__(self, browser_driver, language):
		self.browser_driver = browser_driver
		self.language = language
	
	def matches(self, line):
		reg = self.language["button_is_visible_regex"]
		self.last_match = reg.search(line)
		return self.last_match
	
	def values_for(self, line):
		return self.last_match and (self.last_match.groups()[1],) or tuple([])
		
	def execute(self, values):
		button_name = values[0]
		is_visible = self.browser_driver.is_button_visible(button_name)
		if (is_visible):
			raise ActionFailedError(self.language["button_is_visible_failure"] % (button_name))

	def __call__(browser_driver):
		return ButtonClickAction(browser_driver)