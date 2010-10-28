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

from mocker import Mocker

from pyccuracy.fixture import Fixture
from pyccuracy.fixture_items import Story, Scenario, Action
from pyccuracy.common import Context, Settings, Status
from pyccuracy.story_runner import StoryRunner
from pyccuracy.errors import ActionFailedError
from utils import Object

def some_action():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="some file")
    scenario = story.append_scenario("1", "Something")
    def execute_action(context, *args, **kwargs):
        return None
        
    return scenario.add_given(action_description="Some Action", \
                              execute_function=execute_action, \
                              args=["s"], \
                              kwargs={"a":"b"})

def test_story_runner_returns_a_result():
    
    mocker = Mocker()
    
    settings = Settings()
    fixture = Fixture()
    runner = StoryRunner()
    context = Object()
    context.browser_driver = mocker.mock()
    context.browser_driver.start_test("http://localhost")
    context.browser_driver.stop_test()

    with mocker:
        result = runner.run_stories(settings, fixture, context=context)
        assert result is not None

def test_story_runner_returns_a_result_with_a_Fixture():
    
    mocker = Mocker()
    
    settings = Settings()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    runner = StoryRunner()

    context = Object()
    context.browser_driver = mocker.mock()
    context.browser_driver.start_test("http://localhost")
    context.browser_driver.stop_test()
    context.settings = mocker.mock()
    context.settings.on_before_action
    mocker.result(None)
    context.settings.on_action_successful
    mocker.result(None)
    
    context.language = mocker.mock()
    context.language.get('given')
    mocker.result('Given')
    context.language.get('when')
    mocker.result('When')
    context.language.get('then')
    mocker.result('Then')

    with mocker:
        result = runner.run_stories(settings, fixture, context=context)
    
        assert result.fixture is not None
        assert isinstance(result.fixture, Fixture)

def test_story_runner_returns_a_result_with_the_original_Fixture():
    
    mocker = Mocker()
    
    settings = Settings()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    runner = StoryRunner()

    context = Object()
    context.browser_driver = mocker.mock()
    context.browser_driver.start_test("http://localhost")
    context.browser_driver.stop_test()
    context.settings = mocker.mock()
    context.settings.on_before_action
    mocker.result(None)
    context.settings.on_action_successful
    mocker.result(None)
    
    context.language = mocker.mock()
    context.language.get('given')
    mocker.result('Given')
    context.language.get('when')
    mocker.result('When')
    context.language.get('then')
    mocker.result('Then')

    with mocker:
        result = runner.run_stories(settings, fixture, context=context)
    
        assert result.fixture == fixture

def test_story_runner_returns_failed_story():
    
    mocker = Mocker()
    
    settings = Settings()
    fixture = Fixture()
    runner = StoryRunner()

    context = Object()
    context.browser_driver = mocker.mock()
    context.browser_driver.start_test("http://localhost")
    context.browser_driver.stop_test()

    with mocker:
        result = runner.run_stories(settings, fixture, context=context)
    
        assert result is not None

def test_create_context_for_returns_context():
    settings = Settings()
    runner = StoryRunner()
    context = runner.create_context_for(settings)

    assert context is not None

def test_should_execute_scenarios_successfully():
    
    mocker = Mocker()
    
    settings = Settings()
    runner = StoryRunner()
    fixture = Fixture()
    fixture.append_story(some_action().scenario.story)

    context = Object()
    context.browser_driver = mocker.mock()
    context.browser_driver.start_test("http://localhost")
    context.browser_driver.stop_test()
    context.settings = mocker.mock()
    context.settings.on_before_action
    mocker.result(None)
    context.settings.on_action_successful
    mocker.result(None)
    
    context.language = mocker.mock()
    context.language.get('given')
    mocker.result('Given')
    context.language.get('when')
    mocker.result('When')
    context.language.get('then')
    mocker.result('Then')

    with mocker:
        result = runner.run_stories(settings=settings, fixture=fixture, context=context)
    
        assert fixture.get_status() == Status.Successful

def test_should_handle_action_errors_successfully():
    
    mocker = Mocker()
    
    def action_failed_method(context, *args, **kwargs):
        raise ActionFailedError("bla")
    settings = Settings()
    runner = StoryRunner()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    action.execute_function = action_failed_method

    context = Object()
    context.browser_driver = mocker.mock()
    context.browser_driver.start_test("http://localhost")
    context.browser_driver.stop_test()
    context.settings = mocker.mock()
    context.settings.on_before_action
    mocker.result(None)
    context.settings.on_action_error
    mocker.result(None)
    context.language = mocker.mock()
    context.language.get('given')
    mocker.result('Given')

    with mocker:
        result = runner.run_stories(settings=settings, fixture=fixture, context=context)
    
        assert fixture.get_status() == Status.Failed

def test_should_record_errors_correctly():
    
    mocker = Mocker()
    
    def action_failed_method(context, *args, **kwargs):
        raise ActionFailedError("bla")
    settings = Settings()
    runner = StoryRunner()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    action.execute_function = action_failed_method

    context = Object()
    context.browser_driver = mocker.mock()
    context.browser_driver.start_test("http://localhost")
    context.browser_driver.stop_test()
    context.settings = mocker.mock()
    context.settings.on_before_action
    mocker.result(None)
    context.settings.on_action_error
    mocker.result(None)
    
    context.language = mocker.mock()
    context.language.get('given')
    mocker.result('Given')

    with mocker:
        result = runner.run_stories(settings=settings, fixture=fixture, context=context)
    
        assert isinstance(action.error, ActionFailedError)
        assert action.error.message == "bla"

def test_should_catch_assertion_error():
    
    mocker = Mocker()
    
    def action_failed_method(context, *args, **kwargs):
        assert False, "bla"
    settings = Settings()
    runner = StoryRunner()
    fixture = Fixture()
    action = some_action()
    fixture.append_story(action.scenario.story)
    action.execute_function = action_failed_method

    context = Object()
    context.browser_driver = mocker.mock()
    context.browser_driver.start_test("http://localhost")
    context.browser_driver.stop_test()
    context.settings = mocker.mock()
    context.settings.on_before_action
    mocker.result(None)
    context.settings.on_action_error
    mocker.result(None)
    context.language = mocker.mock()
    context.language.get('given')
    mocker.result('Given')

    with mocker:
        result = runner.run_stories(settings=settings, fixture=fixture, context=context)
    
        assert isinstance(action.error, AssertionError)
        assert action.error.message == "bla"

