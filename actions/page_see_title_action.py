import re
from selenium_browser_driver import *
from errors import *

class PageSeeTitleAction(object):
	def __init__(self, browser_driver, language):
		self.browser_driver = browser_driver
		self.language = language
	
	def matches(self, line):
		reg = self.language["see_title_regex"]
		self.last_match = reg.search(line)
		return self.last_match
	
	def values_for(self, line):
		return self.last_match and (self.last_match.groups()[1],) or tuple([])
		
	def execute(self, values):
		expected_title = values[0]
		title = self.browser_driver.get_title()
		if (title != expected_title):
			raise ActionFailedError("The expected title (%s) does not match the specified title (%s)" % (title, expected_title))
	
	def __call__(browser_driver):
		return PageSeeTitleAction(browser_driver)