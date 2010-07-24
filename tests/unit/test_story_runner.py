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

from pmock import *;

from pyccuracy.fixture import Fixture
from pyccuracy.fixture_items import Story, Scenario, Action
from pyccuracy.common import Context, Settings, Status
from pyccuracy.story_runner import StoryRunner
from pyccuracy.errors import ActionFailedError

def some_action():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="some file")
    scenario = story.append_scenario("1", "Something")
    return scenario.add_given(action_description="Some Action", \
                              execute_function=lambda context, *args, **kwargs: None, \
                              args=["s"], \
                              kwargs={"a":"b"})

def test_story_runner_returns_a_result():
    settings = Settings()
    fixture = Fixture()
    runner = StoryRunner()
    context = Mock()
    context.browser_driver = Mock()
    context.browser_driver.expects(once()).start_test(eq("http://localhost"))
    context.browser_driver.expects(once()).stop_test()

    result = runner.run_stories(settings, fixture, context=context)
    assert result is not None

    context.verify()
    context.browser_driver.verify()

def test_story_runner_returns_a_result_with_a_Fixture():
    settings = Settings()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    runner = StoryRunner()

    context = Mock()
    context.browser_driver = Mock()
    context.browser_driver.expects(once()).start_test(eq("http://localhost"))
    context.browser_driver.expects(once()).stop_test()
    context.settings = Mock()
    context.settings.on_before_action = None
    context.settings.on_action_successful = None
    context.settings.on_action_error = None
    context.language = Mock()
    context.language \
           .expects(once()) \
           .get(eq('given')) \
           .will(return_value('Given'))
    context.language \
           .expects(once()) \
           .get(eq('when')) \
           .will(return_value('When'))
    context.language \
           .expects(once()) \
           .get(eq('then')) \
           .will(return_value('Then'))

    result = runner.run_stories(settings, fixture, context=context)

    assert result.fixture is not None
    context.verify()
    context.browser_driver.verify()

def test_story_runner_returns_a_result_with_the_original_Fixture():
    settings = Settings()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    runner = StoryRunner()

    context = Mock()
    context.browser_driver = Mock()
    context.browser_driver.expects(once()).start_test(eq("http://localhost"))
    context.browser_driver.expects(once()).stop_test()
    context.settings = Mock()
    context.settings.on_before_action = None
    context.settings.on_action_successful = None
    context.settings.on_action_error = None
    context.language = Mock()
    context.language \
           .expects(once()) \
           .get(eq('given')) \
           .will(return_value('Given'))
    context.language \
           .expects(once()) \
           .get(eq('when')) \
           .will(return_value('When'))
    context.language \
           .expects(once()) \
           .get(eq('then')) \
           .will(return_value('Then'))

    result = runner.run_stories(settings, fixture, context=context)

    assert result.fixture == fixture
    context.verify()
    context.browser_driver.verify()

def test_story_runner_returns_failed_story():
    settings = Settings()
    fixture = Fixture()
    runner = StoryRunner()

    context = Mock()
    context.browser_driver = Mock()
    context.browser_driver.expects(once()).start_test(eq("http://localhost"))
    context.browser_driver.expects(once()).stop_test()

    result = runner.run_stories(settings, fixture, context=context)

    assert result is not None
    context.verify()
    context.browser_driver.verify()

def test_create_context_for_returns_context():
    settings = Settings()
    runner = StoryRunner()
    context = runner.create_context_for(settings)

    assert context is not None

def test_should_execute_scenarios_successfully():
    settings = Settings()
    runner = StoryRunner()
    fixture = Fixture()
    fixture.append_story(some_action().scenario.story)

    context = Mock()
    context.browser_driver = Mock()
    context.browser_driver.expects(once()).start_test(eq("http://localhost"))
    context.browser_driver.expects(once()).stop_test()
    context.settings = Mock()
    context.settings.on_before_action = None
    context.settings.on_action_successful = None
    context.settings.on_action_error = None
    context.language = Mock()
    context.language \
           .expects(once()) \
           .get(eq('given')) \
           .will(return_value('Given'))
    context.language \
           .expects(once()) \
           .get(eq('when')) \
           .will(return_value('When'))
    context.language \
           .expects(once()) \
           .get(eq('then')) \
           .will(return_value('Then'))

    result = runner.run_stories(settings=settings, fixture=fixture, context=context)

    assert fixture.get_status() == Status.Successful
    context.verify()
    context.browser_driver.verify()

def test_should_handle_action_errors_successfully():
    def action_failed_method(context, *args, **kwargs):
        raise ActionFailedError("bla")
    settings = Settings()
    runner = StoryRunner()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    action.execute_function = action_failed_method

    context = Mock()
    context.browser_driver = Mock()
    context.browser_driver.expects(once()).start_test(eq("http://localhost"))
    context.browser_driver.expects(once()).stop_test()
    context.settings = Mock()
    context.settings.on_before_action = None
    context.settings.on_action_successful = None
    context.settings.on_action_error = None
    context.language = Mock()
    context.language \
           .expects(once()) \
           .get(eq('given')) \
           .will(return_value('Given'))
    context.language \
           .expects(once()) \
           .get(eq('when')) \
           .will(return_value('When'))
    context.language \
           .expects(once()) \
           .get(eq('then')) \
           .will(return_value('Then'))

    result = runner.run_stories(settings=settings, fixture=fixture, context=context)

    assert fixture.get_status() == Status.Failed
    context.verify()
    context.browser_driver.verify()

def test_should_record_errors_correctly():
    def action_failed_method(context, *args, **kwargs):
        raise ActionFailedError("bla")
    settings = Settings()
    runner = StoryRunner()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    action.execute_function = action_failed_method

    context = Mock()
    context.browser_driver = Mock()
    context.browser_driver.expects(once()).start_test(eq("http://localhost"))
    context.browser_driver.expects(once()).stop_test()
    context.settings = Mock()
    context.settings.on_before_action = None
    context.settings.on_action_successful = None
    context.settings.on_action_error = None
    context.language = Mock()
    context.language \
           .expects(once()) \
           .get(eq('given')) \
           .will(return_value('Given'))
    context.language \
           .expects(once()) \
           .get(eq('when')) \
           .will(return_value('When'))
    context.language \
           .expects(once()) \
           .get(eq('then')) \
           .will(return_value('Then'))

    result = runner.run_stories(settings=settings, fixture=fixture, context=context)

    assert isinstance(action.error, ActionFailedError)
    assert action.error.message == "bla"

    context.verify()
    context.browser_driver.verify()

def test_should_catch_assertion_error():
    def action_failed_method(context, *args, **kwargs):
        assert False, "bla"
    settings = Settings()
    runner = StoryRunner()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    action.execute_function = action_failed_method

    context = Mock()
    context.browser_driver = Mock()
    context.browser_driver.expects(once()).start_test(eq("http://localhost"))
    context.browser_driver.expects(once()).stop_test()
    context.settings = Mock()
    context.settings.on_before_action = None
    context.settings.on_action_successful = None
    context.settings.on_action_error = None
    context.language = Mock()
    context.language \
           .expects(once()) \
           .get(eq('given')) \
           .will(return_value('Given'))
    context.language \
           .expects(once()) \
           .get(eq('when')) \
           .will(return_value('When'))
    context.language \
           .expects(once()) \
           .get(eq('then')) \
           .will(return_value('Then'))

    result = runner.run_stories(settings=settings, fixture=fixture, context=context)

    assert isinstance(action.error, AssertionError)
    assert action.error.message == "bla"

    context.verify()
    context.browser_driver.verify()

