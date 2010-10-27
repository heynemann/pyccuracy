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

from mocker import Mocker

from pyccuracy.result import Result
from pyccuracy.common import Settings, Status
from pyccuracy.fixture import Fixture
from pyccuracy.fixture_items import Story, Scenario, Action

summary_template = """================
Test Run Summary
================

Status: $run_status

Test Data Stats
---------------
Successful Stories......$successful_stories/$total_stories ($successful_story_percentage%)
Failed Stories..........$failed_stories/$total_stories ($failed_story_percentage%)
Successful Scenarios....$successful_scenarios/$total_scenarios ($successful_scenario_percentage%)
Failed Scenarios........$failed_scenarios/$total_scenarios ($failed_scenario_percentage%)"""

summary_template_failed_stories = """#if($has_failed_scenarios)


Failed Stories / Scenarios
--------------------------
#foreach ($scenario in $failed_scenario_instances)Story..........As a $scenario.story.as_a I want to $scenario.story.i_want_to So that $scenario.story.so_that
Story file.....To be implemented.
Scenario.......$scenario.index - $scenario.title
    Given
#foreach ($action in $scenario.givens)#if($action.status != "FAILED")        $action.description - $action.status#end
#if($action.status == "FAILED")        $action.description - $action.status - $action.error#end#end

    When
#foreach ($action in $scenario.whens)#if($action.status != "FAILED")        $action.description - $action.status#end
#if($action.status == "FAILED")        $action.description - $action.status - $action.error#end#end

    Then
#foreach ($action in $scenario.thens)#if($action.status != "FAILED")        $action.description - $action.status#end
#if($action.status == "FAILED")        $action.description - $action.status - $action.error#end#end
#end
#end"""

def some_action():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some file")
    scenario = story.append_scenario("1", "Something")
    return scenario.add_given(action_description="Some Action", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})

def complete_scenario_with_then_action_returned():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="Some file")
    scenario = story.append_scenario("1", "Something")
    given = scenario.add_given(action_description="I did something", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})
    when = scenario.add_when(action_description="I do something", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})
    then = scenario.add_then(action_description="Something happens", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})
    return then

def test_empty_result_returns_result():
    result = Result.empty()
    assert result is not None

def test_empty_result_returns_none_fixture():
    result = Result.empty()
    assert result.fixture is None

def test_empty_result_returns_unknown_status():
    result = Result.empty()
    assert result.get_status() == Status.Unknown

def test_see_summary_for_fixture():
    
    mocker = Mocker()
    
    template_loader_mock = mocker.mock()
    template_loader_mock.load("summary")
    mocker.result(summary_template)
    
    with mocker:
        settings = Settings()
        fixture = Fixture()
        action = some_action()
        fixture.append_story(action.scenario.story)
        action.mark_as_successful()
        result = Result(fixture=fixture, template_loader=template_loader_mock)
    
        summary = result.summary_for(settings.default_culture)
        assert summary is not None

def test_see_summary_for_fixture_returns_proper_string():
    
    mocker = Mocker()
    
    expected = """================
Test Run Summary
================

Status: SUCCESSFUL

Test Data Stats
---------------
Successful Stories......1/1 (100.00%)
Failed Stories..........0/1 (0.00%)
Successful Scenarios....1/1 (100.00%)
Failed Scenarios........0/1 (0.00%)"""

    template_loader_mock = mocker.mock()
    template_loader_mock.load("summary")
    mocker.result(summary_template)
    
    with mocker:
        settings = Settings()
        fixture = Fixture()
        action = some_action()
        fixture.append_story(action.scenario.story)
        action.mark_as_successful()
        result = Result(fixture=fixture, template_loader=template_loader_mock)
    
        summary = result.summary_for(settings.default_culture)
        assert summary == expected

def test_see_summary_for_fixture_returns_proper_string_for_failed_tests():
    
    mocker = Mocker()
    
    expected = """================
Test Run Summary
================

Status: FAILED

Test Data Stats
---------------
Successful Stories......0/1 (0.00%)
Failed Stories..........1/1 (100.00%)
Successful Scenarios....0/1 (0.00%)
Failed Scenarios........1/1 (100.00%)"""

    template_loader_mock = mocker.mock()
    template_loader_mock.load("summary")
    mocker.result(summary_template)
    
    with mocker:
        settings = Settings()
        fixture = Fixture()
        action = some_action()
        fixture.append_story(action.scenario.story)
        action.mark_as_failed()
        result = Result(fixture=fixture, template_loader=template_loader_mock)
    
        summary = result.summary_for(settings.default_culture)
        assert summary == expected

def test_see_summary_for_fixture_returns_proper_string_for_no_tests():
    
    mocker = Mocker()
    
    expected = """================
Test Run Summary
================

Status: UNKNOWN

Test Data Stats
---------------
Successful Stories......0/0 (0.00%)
Failed Stories..........0/0 (0.00%)
Successful Scenarios....0/0 (0.00%)
Failed Scenarios........0/0 (0.00%)"""

    template_loader_mock = mocker.mock()
    template_loader_mock.load("summary")
    mocker.result(summary_template)
    
    with mocker:
        settings = Settings()
        fixture = Fixture()
        result = Result(fixture=fixture, template_loader=template_loader_mock)
    
        summary = result.summary_for(settings.default_culture)
        assert summary == expected

def test_see_summary_for_fixture_returns_proper_failed_scenarios_string():
    
    mocker = Mocker()
    
    expected = """================
Test Run Summary
================

Status: FAILED

Test Data Stats
---------------
Successful Stories......0/1 (0.00%)
Failed Stories..........1/1 (100.00%)
Successful Scenarios....0/1 (0.00%)
Failed Scenarios........1/1 (100.00%)

Failed Stories / Scenarios
--------------------------
Story..........As a Someone I want to Do Something So that I'm Happy
Story file.....To be implemented.
Scenario.......1 - Something
    Given
        I did something - UNKNOWN
    When
        I do something - UNKNOWN
    Then
        Something happens - FAILED - Something very bad happened
"""

    template_loader_mock = mocker.mock()
    template_loader_mock.load("summary")
    mocker.result(summary_template + summary_template_failed_stories)
    
    with mocker:
        settings = Settings()
        fixture = Fixture()
        result = Result(fixture=fixture, template_loader=template_loader_mock)
        action = complete_scenario_with_then_action_returned()
        fixture.append_story(action.scenario.story)
        action.mark_as_failed("Something very bad happened")
    
        summary = result.summary_for(settings.default_culture)
    
        assert summary.strip() == expected.strip()

