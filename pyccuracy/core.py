#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Bernardo Heynemann <heynemann@gmail.com>
# Copyright (C) 2009 Gabriel Falcão <gabriel@nacaolivre.org>
#
# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.opensource.org/licenses/osl-3.0.php
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import join, abspath, dirname

from pyccuracy import Page, ActionBase
from pyccuracy.story_runner import *
from pyccuracy.parsers import *
from pyccuracy.errors import *

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

    def __print_results(self, results):
        print unicode(results)
        print "\n"

