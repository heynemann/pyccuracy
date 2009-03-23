# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium_browser_driver import *
from webdriver_browser_driver import *
from story_runner import *
from test_fixture_parser import *
from language import *
from errors import *
from pyoc.ioc import IoC
from pyoc.config import InPlaceConfig
from page import Page
from actions.action_base import ActionBase
import report_parser as report
from os.path import join

class PyccuracyCore(object):
    def run_tests(self,
                  tests_dir=os.curdir,
                  actions_dir=os.path.join(os.path.dirname(__file__), "actions"),
                  custom_actions_dir=None,
                  pages_dir = None,
                  file_pattern="to_be_defined_by_language",
                  default_culture="en-us",
                  languages_dir=os.path.join(os.path.dirname(__file__), "languages"),
                  base_url= None,
                  should_throw = False,
                  context = None,
                  write_report = True,
                  report_file_dir = None,
                  report_file_name="report.html",
                  browser_to_run="firefox",
                  browser_driver="selenium"):

        IoC.reset()

        if not pages_dir:
            pages_dir = tests_dir

        if not custom_actions_dir:
            custom_actions_dir = tests_dir

        if not report_file_dir:
            report_file_dir = tests_dir

        lang = self.load_language(languages_dir, default_culture)

        self.configure_ioc(languages_dir,
                           default_culture,
                           tests_dir,
                           file_pattern,
                           actions_dir,
                           pages_dir,
                           base_url,
                           custom_actions_dir,
                           lang,
                           browser_to_run,
                           browser_driver)

        if context == None:
            self.context = IoC.resolve(PyccuracyContext)

        self.context.browser_driver.start()

        #running the tests
        try:
            results = self.context.story_runner.run_stories(self.context)
        finally:
            self.context.browser_driver.stop()

        results = self.context.test_fixture.get_results()

        self.__print_results(results)

        if write_report:
            report.generate_report(join(report_file_dir, report_file_name), results, lang)

        if should_throw and self.context.test_fixture.get_results().status == "FAILED":
            raise TestFailedError("The test failed!")

        return results

    def __select_browser_driver(self, driver_name):
        available_drivers = {
            "selenium": SeleniumBrowserDriver,
            "webdriver": WebdriverBrowserDriver,
            }

        selected_driver = available_drivers.get(driver_name, None)
        
        if selected_driver is None:
            raise LookupError('The requested Webdriver was not found. Available drivers are: \n%s' % available_drivers.keys())

        return selected_driver


    def configure_ioc(self, languages_dir, culture, tests_dir, file_pattern, actions_dir, pages_dir, base_url, custom_actions_dir, lang, browser_to_run, browser_driver):

        config = InPlaceConfig()
        config.register("selenium_server", SeleniumServer)

        config.register("browser_driver", self.__select_browser_driver(browser_driver))

        config.register_instance("language", lang)

        if (file_pattern == "to_be_defined_by_language"): file_pattern = lang["default_pattern"]
        config.register("file_pattern", file_pattern)

        config.register("test_fixture_parser", FileTestFixtureParser)
        config.register("tests_dir", tests_dir)

        config.register_files("all_actions", actions_dir, "*_action.py", lifestyle_type = "singleton")

        config.register_inheritors("all_pages", pages_dir, Page)
        config.register_inheritors("all_custom_actions", custom_actions_dir, ActionBase)

        config.register("story_runner", StoryRunner)

        config.register("browser_to_run", "*%s" % browser_to_run)        

        config.register("scripts_path", os.path.abspath(__file__))
        config.register("base_url", base_url)

        IoC.configure(config)

    def load_language(self, languages_dir, culture):
        lang = Language(languages_dir)
        lang.load(culture)

        return lang

    def __print_results(self, results):
        print unicode(results)
        print "\n"

class PyccuracyContext:
    def __init__(self, browser_driver, language, test_fixture_parser, tests_dir, file_pattern, story_runner, all_actions, all_pages, all_custom_actions, base_url):
        self.browser_driver = browser_driver
        self.language = language
        self.test_fixture_parser = test_fixture_parser
        self.test_fixture = self.test_fixture_parser.get_fixture([file_path for file_path in list(locate(file_pattern, tests_dir))])
        self.tests_dir = tests_dir
        self.all_pages = dict(zip([klass.__class__.__name__ for klass in all_pages], [klass for klass in all_pages]))
        self.current_page = None
        self.file_pattern = file_pattern
        self.story_runner = story_runner
        self.base_url = base_url
        self.all_custom_actions = all_custom_actions
        self.all_actions = all_actions

