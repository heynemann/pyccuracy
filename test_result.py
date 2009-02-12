class TestResult(object):
	def __init__(self, language, stories, invalid_test_files, no_story_definition):
		self.language = language
		self.stories = stories
		self.invalid_test_files = invalid_test_files
		self.no_story_definition = no_story_definition

		self.successful_stories = 0
		self.failed_stories = 0
		self.successful_scenarios = 0
		self.failed_scenarios = 0
		self.status = "SUCCESSFUL"
		self.__parse_results()
		
	def __parse_results(self):
		self.invalid_files = len(self.invalid_test_files) + len(self.no_story_definition)
		for story in self.stories:
			if story.status == "SUCCESSFUL": self.successful_stories+=1
			if story.status == "FAILED": 
			    self.failed_stories+=1
			    self.status = "FAILED"
			for scenario in story.scenarios:
				if scenario.status == "SUCCESSFUL": self.successful_scenarios+=1
				if scenario.status == "FAILED": self.failed_scenarios+=1
	
	def __str__(self):
		messages = []
		
		total_stories = float(self.successful_stories + self.failed_stories)
		total_scenarios = float(self.successful_scenarios + self.failed_scenarios)
		percentage_successful_stories = (self.successful_stories / (total_stories or 1))
		percentage_failed_stories = (self.failed_stories / (total_stories or 1))
		percentage_successful_scenarios = (self.successful_scenarios / (total_scenarios or 1))
		percentage_failed_scenarios = (self.failed_scenarios / (total_scenarios or 1))
		
		messages.append(self.language["test_run_summary"])
		messages.append("-" * 80)
		messages.append(self.language["stories_ran_successfully"] % (self.successful_stories, percentage_successful_stories * 100))
		messages.append(self.language["stories_that_failed"] % (self.failed_stories, percentage_failed_stories * 100))
		messages.append(self.language["scenarios_ran_successfully"] % (self.successful_scenarios, percentage_successful_scenarios * 100))
		messages.append(self.language["scenarios_that_failed"] % (self.failed_scenarios, percentage_failed_scenarios * 100))
		return "\n".join(messages)