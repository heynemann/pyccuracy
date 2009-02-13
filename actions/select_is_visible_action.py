import re
from element_is_visible_helper import *

class SelectIsVisibleAction(ElementIsVisibleHelper):
	def __init__(self, browser_driver, language):
		ElementIsVisibleHelper.__init__(self, browser_driver, language)
		
	def get_selector(self, element_name):
		return r"//select[@name='%s' or @id='%s']" % (element_name, element_name)		
	
	def matches(self, line):
		reg = self.language["select_is_visible_regex"]
		self.last_match = reg.search(line)
		return self.last_match
	
	def values_for(self, line):
		return self.last_match and (self.last_match.groups()[1],) or tuple([])
		
	def execute(self, values):
		select_name = values[0]
		error_message = self.language["select_is_visible_failure"]
		self.execute_is_visible(select_name, error_message)

	def __call__(browser_driver):
		return SelectIsVisibleAction(browser_driver)