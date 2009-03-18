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

        self.browser_driver.start_test("http://www.pyccuracy.org")
        try:
            test_fixture.start_run()
            for current_story in test_fixture.stories:
                self.raise_pre_story(context, current_story)
                self.__run_scenarios(current_story, context)
                self.raise_post_story(context, current_story, current_story.status)
        finally:
            test_fixture.end_run()
            self.browser_driver.stop_test()

    def __run_scenarios(self, current_story, context):
        for current_scenario in current_story.scenarios:
            self.raise_pre_scenario(context, current_story, current_scenario)
            current_scenario.start_run()
            for current_action in (current_scenario.givens + current_scenario.whens + current_scenario.thens):
                current_action.start_run()
                result = current_action.execute(context)
                current_action.end_run()
                if not result: return 0
            current_scenario.end_run()
            self.raise_post_scenario(context, current_story, current_scenario, current_scenario.status)

    def raise_pre_story(self, context, story):
        conditions = story.conditions_module
        if conditions and hasattr(conditions, "pre_story"):
            conditions.pre_story(context, story)

    def raise_post_story(self, context, story, result):
        conditions = story.conditions_module
        if conditions and hasattr(conditions, "post_story"):
            conditions.post_story(context, story, result)

    def raise_pre_scenario(self, context, story, scenario):
        conditions = story.conditions_module
        if conditions and hasattr(conditions, "pre_scenario"):
            conditions.pre_scenario(context, story, scenario)

    def raise_post_scenario(self, context, story, scenario, result):
        conditions = story.conditions_module
        if conditions and hasattr(conditions, "pre_scenario"):
            conditions.post_scenario(context, story, scenario, result)
