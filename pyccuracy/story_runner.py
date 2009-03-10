from test_fixture import *

class StoryRunner(object):
    def __init__(self, browser_driver):
        self.browser_driver = browser_driver

    def run_stories(self, context):
        self.context = context
        test_fixture = context.test_fixture

        #No tests to run
        if len(test_fixture.stories) == 0:
            test_fixture.did_not_run() 
            return
            
        self.browser_driver.start_test("http://www.google.com")
        try:
            test_fixture.start_run()
            for current_story in test_fixture.stories:
                self.__run_scenarios(current_story, context)
        finally:
            test_fixture.end_run()
            self.browser_driver.stop_test()

    def __run_scenarios(self, current_story, context):
        for current_scenario in current_story.scenarios:
            current_scenario.start_run()
            for current_action in (current_scenario.givens + current_scenario.whens + current_scenario.thens):
                current_action.start_run()
                result = current_action.execute(context)
                current_action.end_run()
                if not result: return 0
            current_scenario.end_run()
