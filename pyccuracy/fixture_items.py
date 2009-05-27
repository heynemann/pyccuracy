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

class Status:
    '''Possible statuses of a story, scenario or action.'''
    Unknown = "UNKNOWN"
    Failed = "FAILED"
    Successful = "SUCCESSFUL"

class Story(object):
    '''Class that represents a story to be run by Pyccuracy.
    Contains zero or many scenarios to be run.'''
    def __init__(self, as_a, i_want_to, so_that):
        self.as_a = as_a
        self.i_want_to = i_want_to
        self.so_that = so_that
        self.scenarios = []
        self.status = Status.Unknown
        self.start_time = None
        self.end_time = None

    def mark_as_failed(self):
        '''Marks this story as failed.'''
        self.status = Status.Failed

    def mark_as_successful(self):
        '''Marks this story as successful only if it has not been marked failed before.'''
        if self.status != Status.Failed:
            self.status = Status.Successful

    def start_run(self):
        '''Starts a run for this story. This method just keeps track of the time this story started.'''
        self.start_time = time.time()

    def end_run(self):
        '''Finishes a run for this story. This method just keeps track of the time this story finished.'''
        self.end_time = time.time()

    def ellapsed(self):
        '''The number of milliseconds that this story took to run.'''
        if self.start_time is None:
            return 0
        if self.end_time is None:
            return 0
        return self.end_time - self.start_time

    def append_scenario(self, index, title):
        scenario = Scenario(self, index, title)
        self.scenarios.append(scenario)
        return scenario

    def __unicode__(self):
        return "Story - As a %s I want to %s So that %s (%d scenarios) - %s" % \
                (self.as_a, self.i_want_to, self.so_that, len(self.scenarios), self.status)
    def __str__(self):
        return unicode(self)


class Scenario(object):
    def __init__(self, story, index, title):
        self.story = story
        self.index = index
        self.title = title
        self.givens = []
        self.whens = []
        self.thens = []
        self.status = Status.Unknown

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
        self.status = Status.Failed
        self.story.mark_as_failed()

    def mark_as_successful(self):
        if self.status != Status.Failed:
            self.status = Status.Successful
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
        self.status = Status.Unknown

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
        self.status = Status.Failed
        self.error = error
        self.scenario.mark_as_failed()

    def mark_as_successful(self):
        if self.status != Status.Failed:
            self.status = Status.Successful
            self.scenario.mark_as_successful()

    def start_run(self):
        self.start_time = time.time()

    def end_run(self):
        self.end_time = time.time()
