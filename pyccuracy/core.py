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

import os
import sys
from os.path import join, split, splitext

from pyccuracy.airspeed import Template

from pyccuracy import Page, ActionBase
from pyccuracy.common import Settings, Context, locate
from pyccuracy.story_runner import *
from pyccuracy.parsers import FileParser, ActionNotFoundError
from pyccuracy.errors import *
from pyccuracy.languages.templates import *
from pyccuracy.drivers import DriverError
from pyccuracy.result import Result
from pyccuracy.colored_terminal import TerminalController

class FSO(object):
    def add_to_import(self, path):
        sys.path.insert(0, path)

    def remove_from_import(self, path):
        sys.path.pop()

    def locate(self, path, pattern):
        return locate(root=path, pattern=pattern, recursive=False)

    def import_file(self, filename):
        __import__(filename)

class PyccuracyCore(object):
    def __init__(self, parser=None, runner=None):
        self.parser = parser or FileParser()
        self.runner = runner

    def run_tests(self, context=None, fso=None, **kwargs):
        settings = Settings(kwargs)

        if not context:
            context = Context(settings)

        if not self.runner:
            self.runner = settings.worker_threads == 1 and StoryRunner() or ParallelStoryRunner(settings.worker_threads)

        self.import_extra_content(settings.pages_dir, fso=fso)

        if settings.custom_actions_dir != settings.pages_dir:
            self.import_extra_content(settings.custom_actions_dir, fso=fso)

        try:
            fixture = self.parser.get_stories(settings)

        except ActionNotFoundError, err:
            self.print_invalid_action(settings.default_culture, err)
            if settings.should_throw:
                raise TestFailedError("The test failed!")

            else:
                return None

        if not fixture.stories:
            results = Result(fixture)
            self.print_results(settings.default_culture, results)
            return results

        #running the tests
        results = self.runner.run_stories(settings=settings, fixture=fixture, context=context)

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
        ctrl = TerminalController()
        print ctrl.render(results.summary_for(language))
        print "\n"

    def print_invalid_action(self, language, err):
        ctrl = TerminalController()
        template_text = TemplateLoader(language).load("invalid_scenario")
        template = Template(template_text)

        values = {
                    "action_text":err.line,
                    "scenario":err.scenario,
                    "filename":err.filename
                 }

        print ctrl.render(template.merge(values))

    def import_extra_content(self, path, fso=None):
        '''Imports all the extra .py files in the tests dir so that pages, actions and other things get imported.'''
        pattern = "*.py"

        if not fso:
            fso = FSO()

        fso.add_to_import(path)
        files = fso.locate(path, pattern)

        for f in files:
            try:
                filename = splitext(split(f)[1])[0]
                fso.import_file(filename)
            except ImportError, err:
                raise ExtraContentError("An error occurred while trying to import %s. Error: %s" % (f, err))

        fso.remove_from_import()

class ExtraContentError(Exception):
    pass
