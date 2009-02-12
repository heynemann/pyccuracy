from action import *

class Scenario(object):
	def __init__(self, story, index, title):
		self.story = story
		self.index = index
		self.title = title
		self.givens = []
		self.whens = []
		self.thens = []
		self.status = "UNKNOWN"
	
	def add_given(self, action_description, execute_function, arguments):
		action = Action(self, action_description, execute_function, arguments)
		self.givens.append(action)
		return action
		
	def add_when(self, action_description, execute_function, arguments):
		action = Action(self, action_description, execute_function, arguments)
		self.whens.append(action)
		return action
	
	def add_then(self, action_description, execute_function, arguments):
		action = Action(self, action_description, execute_function, arguments)
		self.thens.append(action)
		return action
		
	def mark_as_failed(self):
		self.status = "FAILED"
		self.story.mark_as_failed()
	
	def mark_as_successful(self):
		self.status = "SUCCESSFUL"
		self.story.mark_as_successful()