from errors import *

class TestFixture:
	def __init__(self, language):
		self.clear()
		self.language = language
		
	def clear(self):
		self.invalid_test_files = []
		self.no_story_definition = []
		self.stories = []
		
	def add_invalid_test_file(self, path):
		self.invalid_test_files.append(path)
	
	def add_no_story_definition(self, path):
		self.no_story_definition.append(path)
		
	def start_story(self, as_a, i_want_to, so_that):
		story = Story(as_a, i_want_to, so_that)
		self.stories.append(story)
		return story
		
	def __str__(self):
		messages = []
		messages.append("%d %s:\n%s" % (len(self.invalid_test_files), self.language["invalid_test_files"], "\n-".join(self.invalid_test_files)))
		messages.append("%d %s:\n%s" % (len(self.no_story_definition), self.language["files_without_header"], "\n-".join(self.no_story_definition)))
		
		for story in self.stories:
			messages.append("%s %s\n%s %s\n%s %s \n%s: %s" % 
												(self.language["as_a"],
												story.as_a, 
												self.language["i_want_to"],
												story.i_want_to, 
												self.language["so_that"],
												story.so_that, 
												self.language["story_status"],
												story.status))
			for scenario in story.scenarios:
				messages.append("%s %s - %s (Status: %s)" % (self.language["scenario"], scenario.index, scenario.title, scenario.status))
				str = self.language["given"]
				template = "\n\t%s (Status: %s)"
				for action in scenario.givens:
					str = str + (template % (action.description, action.status))
				str = str + "\n" + self.language["when"]
				for action in scenario.whens:
					str = str + (template % (action.description, action.status))
				str = str + "\n" + self.language["then"]
				for action in scenario.thens:
					str = str + (template % (action.description, action.status))
				messages.append(str)
			
		return "\n\n".join(messages)
		
class Story:
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
	
class Scenario:
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
		
class Action:
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
		except TestFailedError:
			self.mark_as_failed()
			return 0
		
		self.mark_as_successful()
		return 1
		
	def mark_as_failed(self):
		self.status = "FAILED"
		self.scenario.mark_as_failed()
	
	def mark_as_successful(self):
		self.status = "SUCCESSFUL"
		self.scenario.mark_as_successful()
		
if __name__ == "__main__":
	fixture = test_fixture()
	fixture.add_invalid_test_file("some invalid path")
	fixture.add_no_story_definition("some no story path")
	
	story = fixture.start_story("Some User", "Do Something", "I get something done")
	
	scenario = story.start_scenario(1, "Some Scenario")
	scenario.add_given("I did something", lambda obj: "some action", ["some arguments"])
	scenario.add_when("I do something", lambda obj: "some action", ["some arguments"])
	scenario.add_then("I see something", lambda obj: "some action", ["some arguments"])
	
	scenario = story.start_scenario(2, "Some Other Scenario")
	scenario.add_given("I did something", lambda obj: "some action", ["some arguments"])
	scenario.add_when("I do something", lambda obj: "some action", ["some arguments"])
	scenario.add_then("I see something", lambda obj: "some action", ["some arguments"])
	
	print fixture