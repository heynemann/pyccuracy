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

from pyccuracy.fixture_items import Status, Story, Scenario, TimedItem, StatusItem

def test_creating_a_story_returns_a_story():
    story = Story(as_a=None, i_want_to=None, so_that=None, identity="Some File")
    assert isinstance(story, Story)

def test_story_is_a_timed_item():
    story = Story(as_a=None, i_want_to=None, so_that=None, identity="Some File")
    assert isinstance(story, TimedItem)

def test_story_is_a_status_item():
    story = Story(as_a=None, i_want_to=None, so_that=None, identity="Some File")
    assert isinstance(story, StatusItem)

def test_creating_a_story_keeps_as_a():
    expected = "someone"
    story = Story(as_a=expected, i_want_to=None, so_that=None, identity="Some File")
    assert story.as_a == expected, "As_a should be %s but was %s" % (expected, story.as_a)

def test_creating_a_story_keeps_i_want_to():
    expected = "do"
    story = Story(as_a=None, i_want_to=expected, so_that=None, identity="Some File")
    assert story.i_want_to == expected, "i_want_to should be %s but was %s" % (expected, story.i_want_to)

def test_creating_a_story_keeps_so_that():
    expected = "so that"
    story = Story(as_a=None, i_want_to=None, so_that=expected, identity="Some File")
    assert story.so_that == expected, "so_that should be %s but was %s" % (expected, story.so_that)

def test_creating_a_story_keeps_an_identity():
    expected = "identity"
    story = Story(as_a=None, i_want_to=None, so_that=None, identity=expected)
    assert story.identity == expected, "identity should be %s but was %s" % (expected, story.identity)

def test_creating_a_story_starts_with_empty_times():
    story = Story(as_a=None, i_want_to=None, so_that=None, identity="Some File")
    assert story.start_time == None, "Story should start with no start time but was %s" % story.start_time
    assert story.end_time == None, "Story should start with no end time but was %s" % story.end_time

def test_creating_a_story_starts_with_empty_scenarios():
    story = Story(as_a=None, i_want_to=None, so_that=None, identity="Some File")
    assert story.scenarios == [], "Story should start with no scenarios but was %s" % story.scenarios

def test_creating_a_story_starts_with_unknown_status():
    story = Story(as_a=None, i_want_to=None, so_that=None, identity="Some File")
    assert story.status == Status.Unknown, "Story should start with Unknown status but was %s" % story.status

def test_story_returns_right_repr():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    expected = u"Story - As a Someone I want to Do Something So that I'm Happy (0 scenarios) - UNKNOWN"
    assert unicode(story) == expected, "Unicode Expected: %s Actual: %s" % (expected, unicode(story))
    assert str(story) == expected, "Str Expected: %s Actual: %s" % (expected, str(story))

def test_mark_story_as_failed():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.mark_as_failed()
    assert story.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, story.status)

def test_mark_story_as_successful():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.mark_as_successful()
    assert story.status == Status.Successful, "The status should be %s but was %s" % (Status.Successful, story.status)

def test_mark_story_as_successful_after_failed_has_no_effect():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.mark_as_failed()
    story.mark_as_successful()
    assert story.status == Status.Failed, "The status should be %s but was %s" % (Status.Failed, story.status)

def test_story_start_run_marks_time():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.start_run()
    assert story.start_time is not None, "There should be some start time after start_run"

def test_story_end_run_marks_time():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.end_run()
    assert story.end_time is not None, "There should be some end time after end_run"

def test_story_ellapsed_returns_zero_for_non_started_stories():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")

    expected = 0
    ellapsed = int(story.ellapsed())
    assert ellapsed == expected, "The ellapsed time should be %d but was %d" % (expected, ellapsed)

def test_story_ellapsed_returns_zero_for_non_finished_stories():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.start_run()
    expected = 0
    ellapsed = int(story.ellapsed())
    assert ellapsed == expected, "The ellapsed time should be %d but was %d" % (expected, ellapsed)

def test_story_ellapsed_returns_seconds():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.start_run()
    time.sleep(0.1)
    story.end_run()

    expected = "0.1"
    ellapsed = "%.1f" % story.ellapsed()
    assert ellapsed == expected, "The ellapsed time should be %s but was %s" % (expected, ellapsed)

def test_append_scenario_adds_to_scenarios_in_story():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.append_scenario(index="1", title="Test")
    assert len(story.scenarios) == 1, "There should be one scenario in the story but there was %d" % len(story.scenarios)

def test_append_scenario_adds_right_class_to_scenarios_in_story():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.append_scenario(index="1", title="Test")
    assert isinstance(story.scenarios[0], Scenario), "There should be an item of class Scenario in the story but there was %s" % story.scenarios[0].__class__

def test_append_scenario_adds_right_index_to_scenarios_in_story():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    story.append_scenario(index="1", title="Test")
    assert story.scenarios[0].index == "1", "There should be a scenario in the story with index 1 but there was %s" % story.scenarios[0].index

