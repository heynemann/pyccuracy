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

