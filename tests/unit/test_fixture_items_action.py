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

import time

from pyccuracy.fixture_items import Status, Story, Scenario, Action

def some_action():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    return Action(scenario=scenario, description="Some Action", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})

def test_creating_an_action_returns_an_action():
    action = Action(scenario=None, description="bla", execute_function=None, args=None, kwargs=None)
    assert isinstance(action, Action)

def test_creating_an_action_keeps_description():
    expected = "1"
    action = Action(scenario=None, description=expected, execute_function=None, args=None, kwargs=None)
    assert action.description == expected, "Description should be %s but was %s" % (expected, action.description)

def test_creating_an_action_keeps_execute_function():
    func = lambda: None
    action = Action(scenario=None, description="bla", execute_function=func, args=None, kwargs=None)
    assert action.execute_function == func, "Execute function should be %s but was %s" % (func, action.execute_function)

def test_creating_an_action_keeps_args_and_kwargs():
    expected = ["a","b"]
    kwargs = {"a":"b"}
    action = Action(scenario=None, description="bla", execute_function=None, args=expected, kwargs=kwargs)
    assert action.args == expected, "Args should be %s but was %s" % (expected, action.args)
    assert action.kwargs == kwargs, "KWArgs should be %s but was %s" % (kwargs, action.kwargs)

def test_creating_an_action_starts_with_empty_times():
    action = some_action()
    assert action.start_time == None, "Action should start with no start time but was %s" % action.start_time
    assert action.end_time == None, "Action should start with no end time but was %s" % action.end_time

def test_creating_an_action_starts_with_unknown_status():
    action = some_action()
    assert action.status == Status.Unknown, "Action should start with Unknown status but was %s" % action.status

def test_story_returns_right_repr():
    action = some_action()
    expected = u"Action Some Action - UNKNOWN"
    assert unicode(action) == expected, "Unicode Expected: %s Actual: %s" % (expected, unicode(action))
    assert str(action) == expected, "Str Expected: %s Actual: %s" % (expected, str(action))

def test_mark_action_as_failed():
    action = some_action()
    action.mark_as_failed()
    assert action.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, action.status)

def test_mark_action_as_successful():
    action = some_action()
    action.mark_as_successful()
    assert action.status == Status.Successful, "The status should be %s but was %s" % (Status.Successful, action.status)

def test_mark_action_as_successful_after_failed_has_no_effect():
    action = some_action()
    action.mark_as_failed()
    action.mark_as_successful()
    assert action.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, action.status)

def test_marking_action_as_failed_also_marks_scenario_as_failed_if_scenario_exists():
    action = some_action()
    action.mark_as_failed()
    assert action.scenario.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, action.scenario.status)

def test_marking_action_as_successful_also_marks_scenario_as_successful_if_scenario_exists():
    action = some_action()
    action.mark_as_successful()
    assert action.scenario.status == Status.Successful, "The status should be %s but was %s" % (Status.Successful, action.scenario.status)

def test_action_start_run_marks_time():
    action = some_action()
    action.start_run()
    assert action.start_time is not None, "There should be some start time after start_run"

def test_action_end_run_marks_time():
    action = some_action()
    action.end_run()
    assert action.end_time is not None, "There should be some end time after end_run"

def test_action_ellapsed_returns_zero_for_non_started_actions():
    action = some_action()

    expected = 0
    ellapsed = int(action.ellapsed())
    assert ellapsed == expected, "The ellapsed time should be %d but was %d" % (expected, ellapsed)

def test_story_ellapsed_returns_zero_for_non_finished_stories():
    action = some_action()
    action.start_run()
    expected = 0
    ellapsed = int(action.ellapsed())
    assert ellapsed == expected, "The ellapsed time should be %d but was %d" % (expected, ellapsed)

def test_action_ellapsed_returns_seconds():
    action = some_action()
    action.start_run()
    time.sleep(0.1)
    action.end_run()

    expected = "0.1"
    ellapsed = "%.1f" % action.ellapsed()
    assert ellapsed == expected, "The ellapsed time should be %s but was %s" % (expected, ellapsed)
    
