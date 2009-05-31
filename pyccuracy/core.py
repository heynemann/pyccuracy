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

from pyccuracy.airspeed import Template

from pyccuracy import Page, ActionBase
from pyccuracy.common import Settings, Context
from pyccuracy.story_runner import *
from pyccuracy.parsers import FileParser, ActionNotFoundError
from pyccuracy.errors import *
from pyccuracy.languages.templates import *
from pyccuracy.drivers import DriverError

class PyccuracyCore(object):
    def __init__(self, parser=None, runner=None):
        self.parser = parser or FileParser()
        self.runner = runner or StoryRunner()

    def run_tests(self, **kwargs):
        settings = Settings(kwargs)
        context = Context(settings)

        try:
            fixture = self.parser.get_stories(settings)
        except ActionNotFoundError, err:
            self.print_invalid_action(settings.default_culture, err)
            if settings.should_throw:
                raise TestFailedError("The test failed!")
            else:
                return None

        try:
            context.browser_driver.start()
        except DriverError, err:
            template_text = TemplateLoader(language).load("driver_error")
            template = Template(template_text)
            values = {"error" : err, browser_driver:context.browser_driver}
            print template.merge(values)

        #running the tests
        try:
            results = self.runner.run_stories(settings=settings, fixture=fixture)
        finally:
            context.browser_driver.stop()

        self.print_results(settings.default_culture, results)

#        if self.context.write_report:
#            import report_parser as report
#            report.generate_report(
#                        join(self.context.report_file_dir, self.context.report_file_name),
#                        results,
#                        self.context.language)

        if settings.should_throw and result.get_status() == Status.Failed:
            raise TestFailedError("The test failed!")

        return results

    def print_results(self, language, results):
        print results.summary_for(language)
        print "\n"

    def print_invalid_action(self, language, err):
        template_text = TemplateLoader(language).load("invalid_scenario")
        template = Template(template_text)
        
        values = {
                    "action_text":err.line,
                    "scenario":err.scenario,
                    "filename":err.filename
                 }

        print template.merge(values)

