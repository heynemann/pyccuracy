import re
from selenium_browser_driver import *

class textbox_type_action:
	def __init__(self, browser_driver, language):
		self.browser_driver = browser_driver
		self.language = language
	
	def matches(self, line):
		reg = self.language["type_regex"]
		self.last_match = reg.search(line)
		return self.last_match
	
	def values_for(self, line):
		return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple([])
		
	def execute(self, values):
		textbox = values[0]
		text = values[1]
		self.browser_driver.type(textbox, text)
		
	def __call__(browser_driver):
		return textbox_type_action(browser_driver)