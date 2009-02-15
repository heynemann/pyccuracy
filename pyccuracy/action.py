from errors import *

class Action(object):
	def __init__(self, scenario, description, execute_function, arguments):
		self.scenario = scenario
		self.description = description
		self.execute_function = execute_function
		self.arguments = arguments
		self.status = "UNKNOWN"
	
	def execute(self):
		try:
			if (self.arguments):
				self.execute_function(self.arguments)
			else:
				self.execute_function()
		except ActionFailedError, error:
			self.mark_as_failed(error)
			return 0
		
		self.mark_as_successful()
		return 1
		
	def mark_as_failed(self, error):
		self.status = "FAILED"
		self.error = error
		self.scenario.mark_as_failed()
	
	def mark_as_successful(self):
		self.status = "SUCCESSFUL"
		self.scenario.mark_as_successful()