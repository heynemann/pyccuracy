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

import sys
import time
import traceback

from Queue import Queue
from threading import Thread

from pyccuracy.result import Result
from pyccuracy.common import Context
from pyccuracy.actions import ActionNotFoundError
from pyccuracy.errors import ActionFailedError
from pyccuracy.drivers import DriverError
from pyccuracy.languages.templates import TemplateLoader
from pyccuracy.airspeed import Template
from pyccuracy.colored_terminal import TerminalController

class StoryRunner(object):
    def run_stories(self, settings, fixture, context=None):
        if not context:
            context = self.create_context_for(settings)

        fixture.start_run()
        if settings.base_url:
            base_url = settings.base_url
        else:
            base_url = "http://localhost"

        try:
            context.browser_driver.start_test(base_url)
        except DriverError, err:
            ctrl = TerminalController()
            template_text = TemplateLoader(settings.default_culture).load("driver_error")
            template = Template(template_text)
            values = {"error": err, "browser_driver": context.browser_driver}
            print ctrl.render(template.merge(values))

            if settings.should_throw:
                raise TestFailedError("The test failed!")
            else:
                return None

        try:
            scenario_index = 0
            for story in fixture.stories:
                for scenario in story.scenarios:
                    if settings.on_scenario_started and callable(settings.on_scenario_started):
                        settings.on_scenario_started(fixture, scenario, scenario_index)
                    scenario_index += 1
                    if not context:
                        context = self.create_context_for(settings)
                    for action in scenario.givens + scenario.whens + scenario.thens:
                        try:
                            result = self.execute_action(context, action)
                            if not result:
                                break
                        except ActionNotFoundError, error:
                            action.mark_as_failed(ActionNotFoundError(error.line, scenario, scenario.story.identity))
                            break
                    if settings.on_scenario_completed and callable(settings.on_scenario_completed):
                        settings.on_scenario_completed(fixture, scenario, scenario_index)

            fixture.end_run()
            return Result(fixture=fixture)
        finally:
            context.browser_driver.stop_test()

    def execute_action(self, context, action):
        try:
            action.execute_function(context, *action.args, **action.kwargs)
        except ActionNotFoundError:
            raise
        except ActionFailedError, err:
            action.mark_as_failed(err)
            return False
        except Exception, err:
            action.mark_as_failed(ValueError("Error executing action %s - %s" % (action.execute_function, traceback.format_exc(err))))
            return False

        action.mark_as_successful()
        return True

    def create_context_for(self, settings):
        return Context(settings)

class ParallelStoryRunner(StoryRunner):
    def __init__(self, number_of_threads):
        self.number_of_threads = number_of_threads
        self.test_queue = Queue()

    def run_stories(self, settings, fixture, context=None):
        if len(fixture.stories) == 0:
            return

        self.fill_queue(fixture, settings)

        fixture.start_run()

        self.start_processes()

        try:
            time.sleep(2)
            while self.test_queue.unfinished_tasks:
                time.sleep(1)
        except KeyboardInterrupt:
            sys.stderr.write("Parallel tests interrupted by user\n")

        fixture.end_run()

        return Result(fixture=fixture)

    def start_processes(self):
        for i in range(self.number_of_threads):
            t = Thread(target=self.worker)
            t.setDaemon(True)
            t.start()

    def fill_queue(self, fixture, settings):
        scenario_index = 0
        for story in fixture.stories:
            for scenario in story.scenarios:
                scenario_index += 1
                context = self.create_context_for(settings)
                self.test_queue.put((fixture, scenario, context))

    def worker(self):
        while True:
            fixture, scenario, context = self.test_queue.get()

            scenario_index = fixture.count_successful_scenarios() + fixture.count_failed_scenarios() + 1

            if context.settings.on_scenario_started and callable(context.settings.on_scenario_started):
                context.settings.on_scenario_started(fixture, scenario, scenario_index)

            current_story = scenario.story
            if context.settings.base_url:
                base_url = context.settings.base_url
            else:
                base_url = "http://localhost"

            context.browser_driver.start_test(base_url)
            try:
                scenario.start_run()
                for action in scenario.givens + scenario.whens + scenario.thens:
                    result = self.execute_action(context, action)
                    if not result:
                        break
                scenario.end_run()
            except Exception, err:
                traceback.print_exc(err)
            finally:
                context.browser_driver.stop_test()
                self.test_queue.task_done()
                if context.settings.on_scenario_completed and callable(context.settings.on_scenario_completed):
                    context.settings.on_scenario_completed(fixture, scenario, scenario_index)

