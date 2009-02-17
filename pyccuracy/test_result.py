import time

class TestResult(object):
    def __init__(self, language, stories, invalid_test_files, no_story_definition, start_time, end_time):
        self.language = language
        self.stories = stories
        self.invalid_test_files = invalid_test_files
        self.no_story_definition = no_story_definition
        self.start_time = start_time
        self.end_time = end_time

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

        messages.append("=" * 80)
        messages.append(self.language["test_run_summary"])
        messages.append("=" * 80)
        messages.append(self.language["stories_ran_successfully"] % (self.successful_stories, percentage_successful_stories * 100))
        messages.append(self.language["stories_that_failed"] % (self.failed_stories, percentage_failed_stories * 100))
        messages.append(self.language["scenarios_ran_successfully"] % (self.successful_scenarios, percentage_successful_scenarios * 100))
        messages.append(self.language["scenarios_that_failed"] % (self.failed_scenarios, percentage_failed_scenarios * 100))
        messages.append("")
        messages.append("Test Run Status: %s" % (self.failed_stories > 0 and "FAILED" or "SUCCESSFUL"))
        period = (self.end_time - self.start_time)
        threshold = total_scenarios / period
        messages.append("Ran all %d scenarios in %0.2f s" % (total_scenarios, period))
        messages.append("Test run threshold: %0.2f scenarios/second" % threshold)
        if (self.failed_stories > 0):
            messages.append("")
            messages.append("=" * 80)
            messages.append("Failures")
            messages.append("=" * 80)
            for story in [story for story in self.stories if story.status == "FAILED"]:
                messages.append("%s %s %s %s %s %s" % (self.language["as_a"], self.language["i_want_to"], self.language["so_that"],
                                                       story.as_a, story.i_want_to, story.so_that))
                messages.append("-" * 80)
                for scenario in [scenario for scenario in story.scenarios if scenario.status == "FAILED"]:
                    messages.append("Scenario %s - %s" % (scenario.index, scenario.title))
                    messages.append("-" * 80)

                    messages.append("%s: " % self.language["given"])
                    self.render_actions(messages, scenario.givens)

                    messages.append("%s: " % self.language["when"])
                    self.render_actions(messages, scenario.whens)

                    messages.append("%s: " % self.language["then"])
                    self.render_actions(messages, scenario.thens)

        return "\n".join(messages)

    def render_actions(self, messages, action_collection):
        for action in action_collection:
            messages.append("	%s - %s" % (action.description, action.status))
            if (action.status == "FAILED"):
                if (action.error):
                    messages[-1] += (" - %s" % action.error)