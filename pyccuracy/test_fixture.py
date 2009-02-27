from errors import *
import time
from test_result import *
from test_fixture_items import *

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
        return TestResult(self.language, self.stories, self.invalid_test_files, self.no_story_definition, self.start_time, self.end_time)

    def start_run(self):
        self.start_time = time.time()
        
    def end_run(self):
        self.end_time = time.time()

    def __str__(self):
        return self.get_results()