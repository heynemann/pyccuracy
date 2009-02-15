from scenario import *

class Story(object):
	def __init__(self, as_a, i_want_to, so_that):
		self.as_a = as_a
		self.i_want_to = i_want_to
		self.so_that = so_that
		self.scenarios = []
		self.status = "UNKNOWN"
		
	def start_scenario(self, scenario_index, scenario_title):
		scenario = Scenario(self, scenario_index, scenario_title)
		self.scenarios.append(scenario)
		return scenario
		
	def mark_as_failed(self):
		self.status = "FAILED"
	
	def mark_as_successful(self):
		self.status = "SUCCESSFUL"