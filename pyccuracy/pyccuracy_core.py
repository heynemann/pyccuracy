#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import join, abspath, dirname

from selenium_browser_driver import *
from webdriver_browser_driver import *
from story_runner import *
from parsers import *
from language import *
from errors import *
from page import Page
from actions import ActionBase

class PyccuracyCore(object):
    def __init__(self, parser, runner):
        self.parser = parser
        self.runner = runner

    def run_tests(self, **kwargs):
        settings = Settings(kwargs)

        test_suite = self.parser.get_fixture(settings)

        self.context.browser_driver.start()

        #running the tests
        try:
            results = self.context.story_runner.run_stories(self.context)
        finally:
            self.context.browser_driver.stop()

        results = self.context.test_fixture.get_results()

        self.__print_results(results)

        if self.context.write_report:
            import report_parser as report
            report.generate_report(
                        join(self.context.report_file_dir, self.context.report_file_name),
                        results,
                        self.context.language)

        if should_throw and self.context.test_fixture.get_results().status == "FAILED":
            raise TestFailedError("The test failed!")

        return results

    def __select_browser_driver(self, lang, driver_name):
        available_drivers = {
            "selenium": SeleniumBrowserDriver,
            "webdriver": WebdriverBrowserDriver,
            }

        selected_driver = available_drivers.get(driver_name, None)

        if selected_driver is None:
            available_drivers_string = ",".join(available_drivers.keys())
            raise LookupError(lang["invalid_browser_driver_error"] % (driver_name, available_drivers_string))

        return selected_driver

    def load_language(self, languages_dir, culture):
        lang = Language(languages_dir)
        lang.load(culture)

        return lang

    def __print_results(self, results):
        print unicode(results)
        print "\n"

class Settings(object):
    def __init__(self, settings={}):
        cur_dir = abspath(os.curdir)
        actions_dir = abspath(join(dirname(__file__), "actions"))
        languages_dir = abspath(join(dirname(__file__), "languages"))

        self.tests_dir = settings.get("tests_dir", cur_dir)

        self.actions_dir = settings.get("actions_dir", actions_dir)
        self.languages_dir = settings.get("languages_dir", languages_dir)

        self.pages_dir = settings.get("pages_dir", cur_dir)
        self.custom_actions_dir = settings.get("custom_actions_dir", cur_dir)

        self.file_pattern = settings.get("file_pattern", "*.acc")
        self.scenarios_to_run = settings.get("scenarios_to_run", None)
        self.default_culture = settings.get("default_culture", "en-us")
        self.base_url = settings.get("base_url", None)
        self.should_throw = settings.get("should_throw", False)
        self.write_report = settings.get("write_report", True)
        self.report_file_dir = settings.get("report_file_dir", cur_dir)
        self.report_file_name = settings.get("report_file_name", "report.html")
        self.browser_to_run = settings.get("browser_to_run", "chrome")
        self.browser_driver = settings.get("browser_driver", "selenium")
        self.extra_args = settings.get("extra_args", {})

class PyccuracyContext:
    def __init__(self,
                 browser_driver,
                 language,
                 test_fixture_parser,
                 tests_dir,
                 file_pattern,
                 scenarios_to_run,
                 story_runner,
                 all_actions,
                 all_pages,
                 all_custom_actions,
                 base_url,
                 report_file_dir,
                 report_file_name,
                 write_report):
        self.browser_driver = browser_driver
        self.language = language
        self.test_fixture_parser = test_fixture_parser
        self.test_fixture = self.test_fixture_parser.get_fixture([file_path for file_path in list(locate(file_pattern, tests_dir))])
        self.tests_dir = tests_dir
        self.all_pages = dict(zip([klass.__class__.__name__ for klass in all_pages], [klass for klass in all_pages]))
        self.current_page = None
        self.file_pattern = file_pattern
        self.scenarios_to_run = scenarios_to_run
        self.story_runner = story_runner
        self.base_url = base_url
        self.all_custom_actions = all_custom_actions
        self.all_actions = all_actions
        self.report_file_dir = report_file_dir
        self.report_file_name = report_file_name
        self.write_report = write_report
