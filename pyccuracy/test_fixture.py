from errors import *
from test_result import *
from story import *

class TestFixture(object):
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
		
	def get_results(self):
		return TestResult(self.language, self.stories, self.invalid_test_files, self.no_story_definition)
		
	def __str__(self):
		return self.get_results()
		
	def get_stories_string():
		messages = []
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
		return messages

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