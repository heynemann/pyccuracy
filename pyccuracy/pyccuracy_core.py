from selenium_browser_driver import *
from story_runner import *
from test_fixture_parser import *
from language import *
from errors import *
from pyoc.ioc import IoC
from pyoc.config import InPlaceConfig
from page import Page

class PyccuracyCore(object):
    def run_tests(self, 
                  tests_path=os.curdir, 
                  actions_root=os.path.join(os.path.dirname(__file__), "actions"),
                  file_pattern="to_be_defined_by_language", 
                  default_culture="en-us", 
                  page_folder = None,
                  languages_dir=os.path.join(os.path.dirname(__file__), "languages"),
                  base_url= None,
                  should_throw = False,
                  context = None):

        IoC.reset()
        
        self.configure_ioc(languages_dir, default_culture, tests_path, file_pattern, actions_root, page_folder, base_url)

        if context == None:
            self.context = IoC.resolve(PyccuracyContext)
        
        self.context.browser_driver.start()

        #running the tests
        try:
            results = self.context.story_runner.run_stories(self.context)
        finally:
            self.context.browser_driver.stop()

        self.__print_results()

        if should_throw and self.context.test_fixture.get_results().status == "FAILED":
            raise TestFailedError("The test failed!")
        
    def configure_ioc(self, languages_dir, culture, tests_path, file_pattern, actions_root, page_folder, base_url):
        config = InPlaceConfig()
        config.register("selenium_server", SeleniumServer)
        config.register("browser_driver", SeleniumBrowserDriver)

        lang = self.load_language(languages_dir, culture)
        config.register_instance("language", lang)
        
        if (file_pattern == "to_be_defined_by_language"): file_pattern = lang["default_pattern"]
        config.register("file_pattern", file_pattern)
        
        config.register("test_fixture_parser", FileTestFixtureParser)
        config.register("tests_path", tests_path)
        
        config.register_files("all_actions", actions_root, "*_action.py", lifestyle_type = "singleton")
        
        if page_folder != None:
            config.register_inheritors("all_pages", page_folder, Page)
        else:
            config.register("all_pages", [])

        config.register("story_runner", StoryRunner)
        
        config.register("browser_to_run", "*firefox")
        config.register("scripts_path", os.path.abspath(__file__))
        config.register("base_url", base_url)
        
        IoC.configure(config)
        
    def load_language(self, languages_dir, culture):
        lang = Language(languages_dir)
        lang.load(culture)
        
        return lang
        
    def __print_results(self):
        print self.context.test_fixture.get_results()
        print "\n"

class PyccuracyContext:
    def __init__(self, browser_driver, language, test_fixture_parser, tests_path, file_pattern, story_runner, all_actions, all_pages, base_url):
        self.browser_driver = browser_driver
        self.language = language
        self.test_fixture_parser = test_fixture_parser
        self.test_fixture = self.test_fixture_parser.get_fixture([file_path for file_path in locate(file_pattern, tests_path)])
        self.tests_path = tests_path
        self.all_pages = dict(zip([klass.__class__.__name__ for klass in all_pages], [klass for klass in all_pages]))
        self.current_page = None
        self.file_pattern = file_pattern
        self.story_runner = story_runner
        self.base_url = base_url

