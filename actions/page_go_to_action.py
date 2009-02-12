import re
from selenium_browser_driver import *

class PageGoToAction:
	def __init__(self, browser_driver, language):
		self.browser_driver = browser_driver
		self.language = language
	
	def matches(self, line):
		reg = self.language["page_go_to_regex"]
		self.last_match = reg.search(line)
		return self.last_match
	
	def values_for(self, line):
		return self.last_match and (self.last_match.groups()[1],) or tuple([])
		
	def execute(self, values):
		url = values[0]
		self.browser_driver.page_open(url)
		self.browser_driver.wait_for_page()
		
	def __call__(browser_driver):
		return PageGoToAction(browser_driver)