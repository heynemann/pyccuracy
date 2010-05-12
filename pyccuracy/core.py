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
from pyccuracy.actions import MetaActionBase
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
        self.used_elements = {}

    def got_element(self, page, element_key, resolved_key):
        if page not in self.used_elements:
            self.used_elements[page] = []
        self.used_elements[page] = element_key

    def run_tests(self, context=None, fso=None, **kwargs):
        settings = Settings(kwargs)

        if not context:
            context = Context(settings)

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

        if len(self.parser.used_actions) != len(ActionBase.all()):
            unused_actions = []
            for action in ActionBase.all():
                if hasattr(action, '__builtin__') and action.__builtin__:
                    continue
                if action not in self.parser.used_actions:
                    unused_actions.append(action.__name__)
            if unused_actions:
                self.print_unused_actions_warning(unused_actions)

        if not fixture.stories:
            results = Result(fixture)
            self.print_results(context.settings.default_culture, results)
            return results

        try:
            Page.subscribe_to_got_element(self.got_element)

            #running the tests
            results = self.runner.run_stories(settings=context.settings,
                                               fixture=fixture,
                                               context=context)

            self.print_unused_elements_warning()
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

    def print_unused_elements_warning(self):
        unused_elements = []
        
        for page_class in Page.all():
            page = page_class()
            if hasattr(page, "register"):
                page.register()
            if not page in self.used_elements:
                unused_elements.extend(page.registered_elements.keys())
            else:
                for element in page.registered_elements.keys():
                    element_key = '[%s] %s' % \
                                (page.__class__.__name__, element)
                                
                    if element not in self.used_elements.values() and \
                                element_key not in unused_elements:
                        unused_elements.append(element_key)

        if unused_elements:
            template = """${YELLOW}WARNING!
    ------------
    The following elements are registered but are never used: 

      *%s
    ------------
    ${NORMAL}
    """
            ctrl = TerminalController()
            print ctrl.render(template % "\n  *".join(unused_elements))

    def print_unused_actions_warning(self, unused_actions):
        template = """${YELLOW}WARNING!
------------
The following actions are never used: 

  *%s
------------
${NORMAL}
"""
        ctrl = TerminalController()
        print ctrl.render(template % "\n  *".join(unused_actions))

    def print_lxml_import_error(self):
        template = """${RED}REPORT ERROR
------------
Sorry, but you need to install lxml (python-lxml in aptitude or easy_install lxml)
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
