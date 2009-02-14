import re
from selenium_browser_driver import *
from errors import *

class PageWaitForPageToLoadAction(object):
	def __init__(self, browser_driver, language):
		self.browser_driver = browser_driver
		self.language = language
	
	def matches(self, line):
		reg = self.language["page_wait_for_page_to_load_regex"]
		self.last_match = reg.search(line)
		return self.last_match
	
	def values_for(self, line):
		if not self.last_match return ()
		
		timeout = float(self.last_match.groups()[2])
		return (timeout,)
		
	def execute(self, values):
		if (values):
			timeout = values[0]
			self.browser_driver.wait_for_page(timeout * 1000)
		else:
			self.browser_driver.wait_for_page()