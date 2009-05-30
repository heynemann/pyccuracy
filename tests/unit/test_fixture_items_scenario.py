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

def test_creating_a_scenario_returns_a_scenario():
    scenario = Scenario(index=None, title=None, story=None)
    assert isinstance(scenario, Scenario)

def test_creating_a_scenario_keeps_index():
    expected = "1"
    scenario = Scenario(index=expected, title=None, story=None)
    assert scenario.index == expected, "Index should be %s but was %s" % (expected, scenario.index)

def test_creating_a_scenario_keeps_title():
    expected = "some title"
    scenario = Scenario(index=None, title=expected, story=None)
    assert scenario.title == expected, "title should be %s but was %s" % (expected, scenario.title)

def test_creating_a_scenario_keeps_the_story():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index=None, title=None, story=story)
    assert str(story) == str(scenario.story), "story should be %s but was %s" % (str(story), str(scenario.story))

def test_creating_a_scenario_starts_with_empty_times():
    scenario = Scenario(index="1", title="Something", story=None)
    assert scenario.start_time == None, "Scenario should start with no start time but was %s" % scenario.start_time
    assert scenario.end_time == None, "Scenario should start with no end time but was %s" % scenario.end_time

def test_creating_a_scenario_starts_with_empty_givens():
    scenario = Scenario(index="1", title="Something", story=None)
    assert scenario.givens == [], "Scenario should start with no givens but was %s" % scenario.givens

def test_creating_a_scenario_starts_with_empty_whens():
    scenario = Scenario(index="1", title="Something", story=None)
    assert scenario.whens == [], "Scenario should start with no whens but was %s" % scenario.whens

def test_creating_a_scenario_starts_with_empty_thens():
    scenario = Scenario(index="1", title="Something", story=None)
    assert scenario.thens == [], "Scenario should start with no thens but was %s" % scenario.thens
    
def test_creating_a_scenario_starts_with_unknown_status():
    scenario = Scenario(index="1", title="Something", story=None)
    assert scenario.status == Status.Unknown, "Scenario should start with Unknown status but was %s" % scenario.status

def test_story_returns_right_repr():
    scenario = Scenario(index="1", title="Do Something", story=None)
    expected = u"Scenario 1 - Do Something (0 givens, 0 whens, 0 thens) - UNKNOWN"
    assert unicode(scenario) == expected, "Unicode Expected: %s Actual: %s" % (expected, unicode(scenario))
    assert str(scenario) == expected, "Str Expected: %s Actual: %s" % (expected, str(scenario))

def test_mark_scenario_as_failed():
    scenario = Scenario(index="1", title="Something", story=None)
    scenario.mark_as_failed()
    assert scenario.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, scenario.status)

def test_mark_scenario_as_successful():
    scenario = Scenario(index="1", title="Something", story=None)
    scenario.mark_as_successful()
    assert scenario.status == Status.Successful, "The status should be %s but was %s" % (Status.Successful, scenario.status)

def test_mark_scenario_as_successful_after_failed_has_no_effect():
    scenario = Scenario(index="1", title="Something", story=None)
    scenario.mark_as_failed()
    scenario.mark_as_successful()
    assert scenario.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, scenario.status)

def test_marking_scenario_as_failed_also_marks_story_as_failed_if_story_exists():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    scenario.mark_as_failed()
    assert story.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, story.status)

def test_marking_scenario_as_successful_also_marks_story_as_failed_if_story_exists():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    scenario.mark_as_successful()
    assert story.status == Status.Successful, "The status should be %s but was %s" % (Status.Successful, story.status)

def test_scenario_start_run_marks_time():
    scenario = Scenario(index="1", title="Something", story=None)
    scenario.start_run()
    assert scenario.start_time is not None, "There should be some start time after start_run"

def test_scenario_end_run_marks_time():
    scenario = Scenario(index="1", title="Something", story=None)
    scenario.end_run()
    assert scenario.end_time is not None, "There should be some end time after end_run"

def test_scenario_ellapsed_returns_zero_for_non_started_scenarios():
    scenario = Scenario(index="1", title="Something", story=None)

    expected = 0
    ellapsed = int(scenario.ellapsed())
    assert ellapsed == expected, "The ellapsed time should be %d but was %d" % (expected, ellapsed)

def test_story_ellapsed_returns_zero_for_non_finished_stories():
    scenario = Scenario(index="1", title="Something", story=None)
    scenario.start_run()
    expected = 0
    ellapsed = int(scenario.ellapsed())
    assert ellapsed == expected, "The ellapsed time should be %d but was %d" % (expected, ellapsed)

def test_scenario_ellapsed_returns_seconds():
    scenario = Scenario(index="1", title="Something", story=None)
    scenario.start_run()
    time.sleep(0.1)
    scenario.end_run()

    expected = "0.1"
    ellapsed = "%.1f" % scenario.ellapsed()
    assert ellapsed == expected, "The ellapsed time should be %s but was %s" % (expected, ellapsed)

def test_append_given_adds_to_givens_in_scenario():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    args = ["a"]
    kwargs = {"extra_args":"something"}
    scenario.add_given("some action", lambda: None, args, kwargs)
    assert len(scenario.givens) == 1, "There should be one given in the scenario but there was %d" % len(scenario.givens)

def test_append_given_adds_right_class_to_givens_in_scenario():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    args = ["a"]
    kwargs = {"extra_args":"something"}
    scenario.add_given("some action", lambda: None, args, kwargs)
    assert isinstance(scenario.givens[0], Action), "There should be one given of type Action in the scenario but there was %s" % scenario.givens[0].__class__

def test_append_when_adds_to_whens_in_scenario():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    args = ["a"]
    kwargs = {"extra_args":"something"}
    scenario.add_when("some action", lambda: None, args, kwargs)
    assert len(scenario.whens) == 1, "There should be one when in the scenario but there was %d" % len(scenario.whens)

def test_append_when_adds_right_class_to_whens_in_scenario():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    args = ["a"]
    kwargs = {"extra_args":"something"}
    scenario.add_when("some action", lambda: None, args, kwargs)
    assert isinstance(scenario.whens[0], Action), "There should be one when of type Action in the scenario but there was %s" % scenario.whens[0].__class__

def test_append_then_adds_to_thens_in_scenario():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    args = ["a"]
    kwargs = {"extra_args":"something"}
    scenario.add_then("some action", lambda: None, args, kwargs)
    assert len(scenario.thens) == 1, "There should be one then in the scenario but there was %d" % len(scenario.thens)

def test_append_then_adds_right_class_to_thens_in_scenario():
    story = Story(as_a="Someone", i_want_to="do something", so_that="something", identity="Some File")
    scenario = Scenario(index="1", title="Something", story=story)
    args = ["a"]
    kwargs = {"extra_args":"something"}
    scenario.add_then("some action", lambda: None, args, kwargs)
    assert isinstance(scenario.thens[0], Action), "There should be one then of type Action in the scenario but there was %s" % scenario.thens[0].__class__

