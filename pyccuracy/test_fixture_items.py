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

from errors import *
import time

class Story(object):
    def __init__(self, as_a, i_want_to, so_that):
        self.as_a = as_a
        self.i_want_to = i_want_to
        self.so_that = so_that
        self.scenarios = []
        self.status = "UNKNOWN"

    def start_scenario(self, scenario_index, scenario_title):
        scenario = Scenario(self, scenario_index, scenario_title)
        self.scenarios.append(scenario)
        return scenario

    def mark_as_failed(self):
        self.status = "FAILED"

    def mark_as_successful(self):
        self.status = "SUCCESSFUL"
        
    def start_run(self):
        self.start_time = time.time()
        
    def end_run(self):
        self.end_time = time.time()

class Scenario(object):
    def __init__(self, story, index, title):
        self.story = story
        self.index = index
        self.title = title
        self.givens = []
        self.whens = []
        self.thens = []
        self.status = "UNKNOWN"

    def add_given(self, action_description, execute_function, arguments):
        action = Action(self, action_description, execute_function, arguments)
        self.givens.append(action)
        return action

    def add_when(self, action_description, execute_function, arguments):
        action = Action(self, action_description, execute_function, arguments)
        self.whens.append(action)
        return action

    def add_then(self, action_description, execute_function, arguments):
        action = Action(self, action_description, execute_function, arguments)
        self.thens.append(action)
        return action

    def mark_as_failed(self):
        self.status = "FAILED"
        self.story.mark_as_failed()

    def mark_as_successful(self):
        self.status = "SUCCESSFUL"
        self.story.mark_as_successful()

    def start_run(self):
        self.start_time = time.time()
        
    def end_run(self):
        self.end_time = time.time()

class Action(object):
    def __init__(self, scenario, description, execute_function, arguments):
        self.scenario = scenario
        self.description = description
        self.execute_function = execute_function
        self.arguments = arguments
        self.status = "UNKNOWN"

    def execute(self, context):
        try:
            if (self.arguments):
                self.execute_function(self.arguments, context)
            else:
                self.execute_function([], context)
        except Exception, error:
            if error.__class__.__name__ != "ActionFailedError": raise
            self.mark_as_failed(error)
            return 0

        self.mark_as_successful()
        return 1

    def mark_as_failed(self, error):
        self.status = "FAILED"
        self.error = error
        self.scenario.mark_as_failed()

    def mark_as_successful(self):
        self.status = "SUCCESSFUL"
        self.scenario.mark_as_successful()

    def start_run(self):
        self.start_time = time.time()
        
    def end_run(self):
        self.end_time = time.time()
