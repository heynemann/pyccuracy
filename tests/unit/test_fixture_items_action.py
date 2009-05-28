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

from pyccuracy.fixture_items import Status, Story, Action, Action

def test_creating_an_action_returns_an_action():
    action = Action(scenario=None, description=None, execute_function=None, args=None, kwargs=None)
    assert isinstance(action, Action)

def test_creating_an_action_keeps_description():
    expected = "1"
    action = Action(scenario=None, description=expected, execute_function=None, args=None, kwargs=None)
    assert action.description == expected, "Description should be %s but was %s" % (expected, action.description)

def test_creating_an_action_keeps_execute_function():
    func = lambda: None
    action = Action(scenario=None, description=None, execute_function=func, args=None, kwargs=None)
    assert action.execute_function == func, "Execute function should be %s but was %s" % (func, action.execute_function)

def test_creating_an_action_keeps_args_and_kwargs():
    expected = ["a","b"]
    kwargs = {"a":"b"}
    action = Action(scenario=None, description=None, execute_function=None, args=expected, kwargs=kwargs)
    assert action.args == expected, "Args should be %s but was %s" % (expected, action.args)
    assert action.kwargs == kwargs, "KWArgs should be %s but was %s" % (kwargs, action.kwargs)

#def test_creating_an_action_starts_with_empty_times():
#    action = Action(index="1", title="Something", story=None)
#    assert action.start_time == None, "Action should start with no start time but was %s" % action.start_time
#    assert action.end_time == None, "Action should start with no end time but was %s" % action.end_time

#def test_creating_an_action_starts_with_empty_givens():
#    action = Action(index="1", title="Something", story=None)
#    assert action.givens == [], "Action should start with no givens but was %s" % action.givens

#def test_creating_an_action_starts_with_empty_whens():
#    action = Action(index="1", title="Something", story=None)
#    assert action.whens == [], "Action should start with no whens but was %s" % action.whens

#def test_creating_an_action_starts_with_empty_thens():
#    action = Action(index="1", title="Something", story=None)
#    assert action.thens == [], "Action should start with no thens but was %s" % action.thens
#    
#def test_creating_an_action_starts_with_unknown_status():
#    action = Action(index="1", title="Something", story=None)
#    assert action.status == Status.Unknown, "Action should start with Unknown status but was %s" % action.status

#def test_story_returns_right_repr():
#    action = Action(index="1", title="Do Something", story=None)
#    expected = u"Action 1 - Do Something (0 givens, 0 whens, 0 thens) - UNKNOWN"
#    assert unicode(action) == expected, "Unicode Expected: %s Actual: %s" % (expected, unicode(action))
#    assert str(action) == expected, "Str Expected: %s Actual: %s" % (expected, str(action))

#def test_mark_action_as_failed():
#    action = Action(index="1", title="Something", story=None)
#    action.mark_as_failed()
#    assert action.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, action.status)

#def test_mark_action_as_successful():
#    action = Action(index="1", title="Something", story=None)
#    action.mark_as_successful()
#    assert action.status == Status.Successful, "The status should be %s but was %s" % (Status.Successful, action.status)

#def test_mark_action_as_successful_after_failed_has_no_effect():
#    action = Action(index="1", title="Something", story=None)
#    action.mark_as_failed()
#    action.mark_as_successful()
#    assert action.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, action.status)

#def test_marking_action_as_failed_also_marks_story_as_failed_if_story_exists():
#    story = Story(as_a="Someone", i_want_to="do something", so_that="something")
#    action = Action(index="1", title="Something", story=story)
#    action.mark_as_failed()
#    assert story.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, story.status)

#def test_marking_action_as_successful_also_marks_story_as_failed_if_story_exists():
#    story = Story(as_a="Someone", i_want_to="do something", so_that="something")
#    action = Action(index="1", title="Something", story=story)
#    action.mark_as_successful()
#    assert story.status == Status.Successful, "The status should be %s but was %s" % (Status.Successful, story.status)

#def test_action_start_run_marks_time():
#    action = Action(index="1", title="Something", story=None)
#    action.start_run()
#    assert action.start_time is not None, "There should be some start time after start_run"

#def test_action_end_run_marks_time():
#    action = Action(index="1", title="Something", story=None)
#    action.end_run()
#    assert action.end_time is not None, "There should be some end time after end_run"

#def test_action_ellapsed_returns_zero_for_non_started_actions():
#    action = Action(index="1", title="Something", story=None)

#    expected = 0
#    ellapsed = int(action.ellapsed())
#    assert ellapsed == expected, "The ellapsed time should be %d but was %d" % (expected, ellapsed)

#def test_story_ellapsed_returns_zero_for_non_finished_stories():
#    action = Action(index="1", title="Something", story=None)
#    action.start_run()
#    expected = 0
#    ellapsed = int(action.ellapsed())
#    assert ellapsed == expected, "The ellapsed time should be %d but was %d" % (expected, ellapsed)

#def test_action_ellapsed_returns_seconds():
#    action = Action(index="1", title="Something", story=None)
#    action.start_run()
#    time.sleep(0.1)
#    action.end_run()

#    expected = "0.10"
#    ellapsed = "%.2f" % action.ellapsed()
#    assert ellapsed == expected, "The ellapsed time should be %s but was %s" % (expected, ellapsed)

#def test_append_given_adds_to_givens_in_action():
#    story = Story(as_a="Someone", i_want_to="do something", so_that="something")
#    action = Action(index="1", title="Something", story=story)
#    kwargs = {"extra_args":"something"}
#    action.add_given("some action", lambda: None, "some arg", **kwargs)
#    assert len(action.givens) == 1, "There should be one given in the action but there was %d" % len(action.givens)

#def test_append_given_adds_right_class_to_givens_in_action():
#    story = Story(as_a="Someone", i_want_to="do something", so_that="something")
#    action = Action(index="1", title="Something", story=story)
#    kwargs = {"extra_args":"something"}
#    action.add_given("some action", lambda: None, "some arg", **kwargs)
#    assert isinstance(action.givens[0], Action), "There should be one given of type Action in the action but there was %s" % action.givens[0].__class__

#def test_append_when_adds_to_whens_in_action():
#    story = Story(as_a="Someone", i_want_to="do something", so_that="something")
#    action = Action(index="1", title="Something", story=story)
#    kwargs = {"extra_args":"something"}
#    action.add_when("some action", lambda: None, "some arg", **kwargs)
#    assert len(action.whens) == 1, "There should be one when in the action but there was %d" % len(action.whens)

#def test_append_when_adds_right_class_to_whens_in_action():
#    story = Story(as_a="Someone", i_want_to="do something", so_that="something")
#    action = Action(index="1", title="Something", story=story)
#    kwargs = {"extra_args":"something"}
#    action.add_when("some action", lambda: None, "some arg", **kwargs)
#    assert isinstance(action.whens[0], Action), "There should be one when of type Action in the action but there was %s" % action.whens[0].__class__

#def test_append_then_adds_to_thens_in_action():
#    story = Story(as_a="Someone", i_want_to="do something", so_that="something")
#    action = Action(index="1", title="Something", story=story)
#    kwargs = {"extra_args":"something"}
#    action.add_then("some action", lambda: None, "some arg", **kwargs)
#    assert len(action.thens) == 1, "There should be one then in the action but there was %d" % len(action.thens)

#def test_append_then_adds_right_class_to_thens_in_action():
#    story = Story(as_a="Someone", i_want_to="do something", so_that="something")
#    action = Action(index="1", title="Something", story=story)
#    kwargs = {"extra_args":"something"}
#    action.add_then("some action", lambda: None, "some arg", **kwargs)
#    assert isinstance(action.thens[0], Action), "There should be one then of type Action in the action but there was %s" % action.thens[0].__class__

