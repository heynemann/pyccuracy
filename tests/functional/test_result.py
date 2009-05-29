#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pyccuracy.result import Result
from pyccuracy.common import Settings
from pyccuracy.fixture import Fixture
from pyccuracy.fixture_items import Story, Scenario, Action

def complete_scenario_with_then_action_returned():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy")
    scenario = story.append_scenario("1", "Something")
    given = scenario.add_given(action_description="I did something", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})
    when = scenario.add_when(action_description="I do something", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})
    then = scenario.add_then(action_description="Something happens", execute_function=lambda: None, args=["s"], kwargs={"a":"b"})
    return then

def test_see_summary_for_fixture_returns_proper_failed_scenarios_string():
    expected = u"""================
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
        Something happens - FAILED - Something very bad happened"""

    settings = Settings()
    fixture = Fixture()
    result = Result(fixture=fixture)
    action = complete_scenario_with_then_action_returned()
    fixture.append_story(action.scenario.story)
    action.mark_as_failed("Something very bad happened")

    summary = result.summary_for("en-us")

    assert summary.strip() == expected.strip(), compare(summary.strip(), expected.strip())

def compare(str_a, str_b):

    for index in range(len(str_a)):
        if index > len(str_b):
            print "Strings differ at position %d" % index
            return

        char_a = str_a[index:index+1]
        char_b = str_b[index:index+1]
        if char_a != char_b:
            print "Strings differ at position %d\nString A: %s\nString B: %s" % (index, str_a[:index+1], str_b[:index+1])
            return

