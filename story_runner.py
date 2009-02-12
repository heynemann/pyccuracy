from test_fixture import *

class StoryRunner(object):
	def __init__(self, browser_driver, test_fixture):
		self.browser_driver = browser_driver
		self.test_fixture = test_fixture
	
	def run_stories(self):
		self.browser_driver.start_test("http://www.google.com")
		try:
			for current_story in self.test_fixture.stories:
				self.__run_scenarios(current_story)
		finally:
			self.browser_driver.stop_test()
			
	def __run_scenarios(self, current_story):
		for current_scenario in current_story.scenarios:
			for current_action in (current_scenario.givens + current_scenario.whens + current_scenario.thens):
				result = current_action.execute()
				if not result: return 0