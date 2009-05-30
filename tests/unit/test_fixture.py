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

from pyccuracy.fixture import Fixture
from pyccuracy.common import Status
from pyccuracy.fixture_items import Story, Scenario, Action

def some_action():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some File")
    scenario = story.append_scenario("1", "Something")
    return scenario.add_given(action_description="Some Action", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})

def test_create_fixture_returns_fixture():
    fixture = Fixture()
    assert isinstance(fixture, Fixture)

def test_fixture_starts_with_empty_lists():
    fixture = Fixture()
    assert len(fixture.invalid_test_files) == 0
    assert len(fixture.no_story_header) == 0
    assert len(fixture.stories) == 0

def test_reset_clears_lists():
    fixture = Fixture()
    fixture.invalid_test_files.append("some")
    fixture.no_story_header.append("some")
    fixture.stories.append("some")

    fixture.clear()

    assert len(fixture.invalid_test_files) == 0
    assert len(fixture.no_story_header) == 0
    assert len(fixture.stories) == 0

def test_append_invalid_test_file():
    fixture = Fixture()
    fixture.append_invalid_test_file("some", "error")
    assert len(fixture.invalid_test_files) == 1

def test_append_invalid_test_file_keeps_file():
    fixture = Fixture()
    fixture.append_invalid_test_file("some", "error")
    assert fixture.invalid_test_files[0][0] == "some"
    assert fixture.invalid_test_files[0][1] == "error"

def test_append_no_story_header():
    fixture = Fixture()
    fixture.append_no_story_header("some")
    assert len(fixture.no_story_header) == 1

def test_append_no_story_header_keeps_file():
    fixture = Fixture()
    fixture.append_no_story_header("some")
    assert fixture.no_story_header[0] == "some"

def test_append_story():
    fixture = Fixture()
    story = Story("some","other","data", identity="Some File")
    fixture.append_story(story)
    assert len(fixture.stories) == 1

def test_append_story_keeps_data():
    fixture = Fixture()
    story = Story("some","other","data", identity="Some File")
    fixture.append_story(story)
    assert fixture.stories[0].as_a == "some"
    assert fixture.stories[0].i_want_to == "other"
    assert fixture.stories[0].so_that == "data"

def test_fixture_returns_unknown_status_if_no_stories():
    fixture = Fixture()
    assert fixture.get_status() == Status.Unknown

def test_fixture_returns_proper_status_if_action_failed():
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    action.mark_as_failed()

    assert fixture.get_status() == Status.Failed

def test_fixture_returns_proper_status_if_action_succeeded():
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    action.mark_as_successful()

    assert fixture.get_status() == Status.Successful

def test_fixture_returns_proper_status_with_two_scenarios():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_successful()
    other_action.mark_as_failed()

    assert fixture.get_status() == Status.Failed

def test_fixture_returns_proper_status_with_two_scenarios_with_failed_first():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_failed()
    other_action.mark_as_successful()

    assert fixture.get_status() == Status.Failed

def test_fixture_returns_proper_status_with_two_scenarios_with_both_successful():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_successful()
    other_action.mark_as_successful()

    assert fixture.get_status() == Status.Successful

def test_fixture_returns_total_number_of_stories():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_successful()
    other_action.mark_as_successful()

    assert fixture.count_total_stories() == 3

def test_fixture_returns_total_number_of_scenarios():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_successful()
    other_action.mark_as_successful()

    assert fixture.count_total_scenarios() == 3

def test_fixture_returns_total_successful_stories():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_successful()
    other_action.mark_as_failed()

    assert fixture.count_successful_stories() == 1

def test_fixture_returns_total_failed_stories():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_successful()
    other_action.mark_as_failed()

    assert fixture.count_failed_stories() == 1

def test_fixture_returns_total_successful_scenarios():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_successful()
    other_action.mark_as_successful()

    assert fixture.count_successful_scenarios() == 2

def test_fixture_returns_total_failed_scenarios():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_failed()
    other_action.mark_as_failed()

    assert fixture.count_failed_scenarios() == 2

def test_fixture_returns_successful_scenarios():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_successful()
    other_action.mark_as_successful()

    assert len(fixture.get_successful_scenarios()) == 2

def test_fixture_returns_failed_scenarios():
    fixture = Fixture()
    action = some_action()
    other_action = some_action()
    fixture.append_story(action.scenario.story)
    fixture.append_story(other_action.scenario.story)
    action.mark_as_failed()
    other_action.mark_as_failed()

    assert len(fixture.get_failed_scenarios()) == 2

