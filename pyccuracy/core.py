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
from pyccuracy.common import Settings, Context, locate, Status
from pyccuracy.story_runner import *
from pyccuracy.parsers import FileParser, ActionNotFoundError
from pyccuracy.errors import *
from pyccuracy.languages.templates import *
from pyccuracy.drivers import DriverError
from pyccuracy.result import Result
from pyccuracy.colored_terminal import TerminalController

class FSO(object):
    def add_to_import(self, path):
        sys.path.append(path)

    def remove_from_import(self, path):
        sys.path.remove(path)

    def locate(self, path, pattern):
        return locate(root=path, pattern=pattern, recursive=False)

    def import_file(self, filename):
        __import__(filename)

class PyccuracyCore(object):
    def __init__(self, parser=None, runner=None):
        self.parser = parser or FileParser()
        self.runner = runner
        sys.path.insert(0, os.getcwd())

    def run_tests(self, context=None, fso=None, **kwargs):
        settings = Settings(kwargs)

        if not context:
            context = Context(settings)

        context.on_before_action = kwargs.get('on_before_action', None)
        context.on_action_successful = kwargs.get('on_action_successful', None)
        context.on_action_error = kwargs.get('on_action_error', None)

        if not self.runner:
            self.runner = context.settings.worker_threads == 1 and StoryRunner() or ParallelStoryRunner(settings.worker_threads)

        for directory in context.settings.pages_dir:
            self.import_extra_content(directory, fso=fso)

        if context.settings.custom_actions_dir != context.settings.pages_dir:
            for directory in context.settings.custom_actions_dir:
                self.import_extra_content(directory, fso=fso)

        try:
            fixture = self.parser.get_stories(settings)

        except ActionNotFoundError, err:
            self.print_invalid_action(context.settings.default_culture, err)
            if settings.should_throw:
                raise TestFailedError("The test failed!")

            else:
                return None

        if not fixture.stories:
            results = Result(fixture)
            self.print_results(context.settings.default_culture, results)
            return results

        try:
            #running the tests
            results = self.runner.run_stories(settings=context.settings,
                                               fixture=fixture,
                                               context=context)

            self.print_results(context.settings.default_culture, results)

            if context.settings.write_report and results:
                try:
                    import lxml
                except ImportError:
                    self.print_lxml_import_error()
                else:
                    import report_parser as report
                    path = join(context.settings.report_file_dir, context.settings.report_file_name)
                    report.generate_report(path, results, context.language)

            if settings.should_throw and results and results.get_status() == Status.Failed:
                raise TestFailedError("The test failed!")

            return results
        except KeyboardInterrupt:
            results = Result(fixture)
            self.print_results(context.settings.default_culture, results)
            return results

    def print_lxml_import_error(self):
        template = """${RED}REPORT ERROR
------------
Sorry, but you need to install lxml (python-lxml in aptitude)
before using the report feature in pyccuracy.
If you do not need a report use the -R=false parameter.
${NORMAL}
"""
        ctrl = TerminalController()
        print ctrl.render(template)

    def print_results(self, language, results):
        if not results:
            return
        ctrl = TerminalController()
        print ctrl.render("${NORMAL}")
        print ctrl.render(results.summary_for(language))
        print "\n"

    def print_invalid_action(self, language, err):
        ctrl = TerminalController()
        print ctrl.render("${NORMAL}")
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
            except ImportError, e:
                import traceback
                err = traceback.format_exc(e)
                raise ExtraContentError("An error occurred while trying to import %s. Error: %s" % (f, err))

        fso.remove_from_import(path)

class ExtraContentError(Exception):
    pass
