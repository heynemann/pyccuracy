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

import fudge
from fudge.inspector import arg as fudge_arg
from nose.tools import raises, with_setup

from pyccuracy.common import Settings
from pyccuracy.parsers import FileParser
from pyccuracy.fixture import Fixture
from pyccuracy.fixture_items import Story

class Object(object):
    pass

def teardown():
    fudge.clear_expectations()

def assert_no_invalid_stories(fixture):
    if fixture.invalid_test_files:
        raise fixture.invalid_test_files[0][1]

def test_can_create_file_parser():
    parser = FileParser()

    assert isinstance(parser, FileParser), "The created instance should be an instance of FileParser but was %s" % parser.__class__

def test_can_create_file_parser_with_mocked_filesystem():
    filemock = Object()
    parser = FileParser(file_object=filemock)

    assert parser.file_object == filemock

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parsing_stories_returns_list():
    settings = Settings()
    filemock = fudge.Fake('filemock')
    filemock.expects('list_files') \
            .with_args(directories=settings.tests_dirs, pattern=settings.file_pattern) \
            .returns([]) \
            .times_called(1)
    parser = FileParser(file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert isinstance(fixture, Fixture)

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parsing_folder_with_no_stories_returns_empty_list():
    settings = Settings()
    files = []
    filemock = fudge.Fake('filemock')
    filemock.expects('list_files') \
            .with_args(directories=settings.tests_dirs, pattern=settings.file_pattern) \
            .returns(files) \
            .times_called(1)

    parser = FileParser(file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.stories) == 0

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parsing_files_with_empty_content_returns_invalid_files_list():
    settings = Settings()
    files = ["some path"]

    story_text = ""

    filemock = fudge.Fake('filemock')
    filemock.expects('list_files') \
            .with_args(directories=settings.tests_dirs, pattern=settings.file_pattern) \
            .returns(files) \
            .times_called(1)
    filemock.expects('read_file') \
            .with_args(files[0]) \
            .returns(story_text) \
            .times_called(1)

    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("as_a") \
                 .returns("As a")
    language_mock.expects('get') \
                 .with_args("i_want_to") \
                 .returns("I want to")
    language_mock.expects('get') \
                 .with_args("so_that") \
                 .returns("So that")
    language_mock.expects('get') \
                 .with_args("no_header_failure") \
                 .returns("No header found")

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path == "some path"

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parsing_files_with_invalid_as_a_returns_invalid_files_list():
    settings = Settings()
    files = ["some path"]
    
    story_text = """As someone
I want to do something
So that I'm happy"""

    filemock = fudge.Fake('filemock')
    filemock.expects('list_files') \
            .with_args(directories=settings.tests_dirs, pattern=settings.file_pattern) \
            .returns(files) \
            .times_called(1)
    filemock.expects('read_file') \
            .with_args(files[0]) \
            .returns(story_text) \
            .times_called(1)

    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("as_a") \
                 .returns("As a")
    language_mock.expects('get') \
                 .with_args("i_want_to") \
                 .returns("I want to")
    language_mock.expects('get') \
                 .with_args("so_that") \
                 .returns("So that")
    language_mock.expects('get') \
                 .with_args("no_header_failure") \
                 .returns("No header found")

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path == "some path"

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parsing_files_with_invalid_i_want_to_returns_invalid_files_list():
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want something
So that I'm happy"""

    filemock = fudge.Fake('filemock')
    filemock.expects('list_files') \
            .with_args(directories=settings.tests_dirs, pattern=settings.file_pattern) \
            .returns(files) \
            .times_called(1)
    filemock.expects('read_file') \
            .with_args(files[0]) \
            .returns(story_text) \
            .times_called(1)

    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("as_a") \
                 .returns("As a")
    language_mock.expects('get') \
                 .with_args("i_want_to") \
                 .returns("I want to")
    language_mock.expects('get') \
                 .with_args("so_that") \
                 .returns("So that")
    language_mock.expects('get') \
                 .with_args("no_header_failure") \
                 .returns("No header found")

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path == "some path"

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parsing_files_with_invalid_so_that_returns_invalid_files_list():
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want to do something
So I'm happy"""

    filemock = fudge.Fake('filemock')
    filemock.expects('list_files') \
            .with_args(directories=settings.tests_dirs, pattern=settings.file_pattern) \
            .returns(files) \
            .times_called(1)
    filemock.expects('read_file') \
            .with_args(files[0]) \
            .returns(story_text) \
            .times_called(1)

    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("as_a") \
                 .returns("As a")
    language_mock.expects('get') \
                 .with_args("i_want_to") \
                 .returns("I want to")
    language_mock.expects('get') \
                 .with_args("so_that") \
                 .returns("So that")
    language_mock.expects('get') \
                 .with_args("no_header_failure") \
                 .returns("No header found")

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path == "some path"

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parsing_files_with_proper_header_returns_parsed_scenario():
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want to do something
So that I'm happy"""

    filemock = fudge.Fake('filemock')
    filemock.expects('list_files') \
            .with_args(directories=settings.tests_dirs, pattern=settings.file_pattern) \
            .returns(files) \
            .times_called(1)
    filemock.expects('read_file') \
            .with_args(files[0]) \
            .returns(story_text) \
            .times_called(1)

    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("as_a") \
                 .returns("As a")
    language_mock.expects('get') \
                 .with_args("i_want_to") \
                 .returns("I want to")
    language_mock.expects('get') \
                 .with_args("so_that") \
                 .returns("So that")

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.stories) == 1
    assert fixture.stories[0].as_a == "someone"
    assert fixture.stories[0].i_want_to == "do something"
    assert fixture.stories[0].so_that == "I'm happy"

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_is_scenario_starter_line():
    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("scenario") \
                 .returns("Scenario") \
                 .times_called(1)

    parser = FileParser(language=language_mock, file_object=None)
    is_scenario_starter_line = parser.is_scenario_starter_line("Scenario bla")
    
    assert is_scenario_starter_line

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_is_not_scenario_starter_line():
    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("scenario") \
                 .returns("Scenario") \
                 .times_called(1)

    parser = FileParser(language=language_mock, file_object=None)
    is_scenario_starter_line = parser.is_scenario_starter_line("Cenario bla")
    
    assert not is_scenario_starter_line

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parse_scenario_line():
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="some file")

    settings_mock = Object()
    settings_mock.scenarios_to_run = []

    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("scenario") \
                 .returns("Scenario") \
                 .times_called(1)

    parser = FileParser(language=language_mock, file_object=None)
    scenario = parser.parse_scenario_line(story, "Scenario 1 - Doing something", settings_mock)

    assert scenario is not None
    assert scenario.index == "1", "Expected 1 actual %s" % scenario.index
    assert scenario.title == "Doing something"

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_is_keyword():
    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("keyword") \
                 .returns("kw") \
                 .times_called(1)

    parser = FileParser(language=language_mock, file_object=None)
    is_keyword = parser.is_keyword("kw", "keyword")

    assert is_keyword

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_is_not_keyword():
    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("keyword") \
                 .returns("kw") \
                 .times_called(1)

    parser = FileParser(language=language_mock, file_object=None)
    is_keyword = parser.is_keyword("other", "keyword")

    assert not is_keyword

def test_parsing_files_with_proper_scenario_returns_parsed_scenario():
    class DoSomethingAction:
        def execute(context, *args, **kwargs):
            pass

    class DoSomethingElseAction:
        def execute(context, *args, **kwargs):
            pass
    class DoYetAnotherThingAction:
        def execute(context, *args, **kwargs):
            pass

    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want to do something
So that I'm happy

Scenario 1 - Test Scenario
Given
    I do something
When
    I do something else
Then
    I do yet another thing"""

    filemock = Mock()
    filemock.expects(once()) \
            .list_files(directories=same(settings.tests_dirs), pattern=same(settings.file_pattern)) \
            .will(return_value(files))
    filemock.expects(once()) \
            .read_file(eq(files[0])) \
            .will(return_value(story_text))

    language_mock = Mock()
    language_mock.expects(at_least_once()) \
                 .get(eq("as_a")) \
                 .will(return_value("As a"))
    language_mock.expects(at_least_once()) \
                 .get(eq("i_want_to")) \
                 .will(return_value("I want to"))
    language_mock.expects(at_least_once()) \
                 .get(eq("so_that")) \
                 .will(return_value("So that"))
    language_mock.expects(at_least_once()) \
                 .get(eq("given")) \
                 .will(return_value("Given"))
    language_mock.expects(at_least_once()) \
                 .get(eq("when")) \
                 .will(return_value("When"))
    language_mock.expects(at_least_once()) \
                 .get(eq("then")) \
                 .will(return_value("Then"))
    language_mock.expects(at_least_once()) \
                 .get(eq("scenario")) \
                 .will(return_value("Scenario"))

    action_registry_mock = Mock()
    action_registry_mock.expects(once()) \
                        .suitable_for(eq("I do something"), eq('en-us')) \
                        .will(return_value((DoSomethingAction, [], {})))
    action_registry_mock.expects(once()) \
                        .suitable_for(eq("I do something else"), eq('en-us')) \
                        .will(return_value((DoSomethingElseAction, [], {})))
    action_registry_mock.expects(once()) \
                        .suitable_for(eq("I do yet another thing"), eq('en-us')) \
                        .will(return_value((DoYetAnotherThingAction, [], {})))

    parser = FileParser(language=language_mock, file_object=filemock, action_registry=action_registry_mock)

    fixture = parser.get_stories(settings=settings)

    assert_no_invalid_stories(fixture)

    assert len(fixture.stories) == 1, "Expected 1, Actual: %d" % len(fixture.stories)
    assert len(fixture.stories[0].scenarios) == 1
    assert len(fixture.stories[0].scenarios[0].givens) == 1
    assert len(fixture.stories[0].scenarios[0].whens) == 1
    assert len(fixture.stories[0].scenarios[0].thens) == 1

    assert fixture.stories[0].scenarios[0].givens[0].description == "I do something"
    assert fixture.stories[0].scenarios[0].whens[0].description == "I do something else"
    assert fixture.stories[0].scenarios[0].thens[0].description == "I do yet another thing"

    language_mock.verify()
    filemock.verify()
    action_registry_mock.verify()

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_parsing_files_with_many_scenarios_returns_parsed_scenarios():
    class DoSomethingAction:
        def execute(context, *args, **kwargs):
            pass

    class DoSomethingElseAction:
        def execute(context, *args, **kwargs):
            pass
    class DoYetAnotherThingAction:
        def execute(context, *args, **kwargs):
            pass

    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want to do something
So that I'm happy

Scenario 1 - Test Scenario
Given
    I do something
When
    I do something else
Then
    I do yet another thing

Scenario 2 - Test Scenario
Given
    I do something
When
    #some custom comment
Then
    I do yet another thing"""

    filemock = fudge.Fake('filemock')
    filemock.expects('list_files') \
            .with_args(directories=settings.tests_dirs, pattern=settings.file_pattern) \
            .returns(files) \
            .times_called(1)
    filemock.expects('read_file') \
            .with_args(files[0]) \
            .returns(story_text) \
            .times_called(1)

    language_mock = fudge.Fake('language_mock')
    language_mock.expects('get') \
                 .with_args("as_a") \
                 .returns("As a")
    language_mock.expects('get') \
                 .with_args("i_want_to") \
                 .returns("I want to")
    language_mock.expects('get') \
                 .with_args("so_that") \
                 .returns("So that")
    
    class LanguageMock(object):
        
        def __init__(self):
            self.verifications = dict(
                scenario=fudge.Fake('verify_scenario_keyword', expect_call=True),
                given=fudge.Fake('verify_given_keyword', expect_call=True),
                when=fudge.Fake('verify_when_keyword', expect_call=True),
                then=fudge.Fake('verify_then_keyword', expect_call=True)
                )
            self.words = dict(
                scenario='Scenario',
                given='',
                when='',
                then=''
                )
        def get(self, regex):
            if regex == 'foo_bar_regex':
                verify_specific_regex()
                return 'My regex .+'
            return '^$'
    
    keywords = dict(
        scenario=fudge.Fake('verify_scenario_keyword', expect_call=True),
        given=fudge.Fake('verify_given_keyword', expect_call=True),
        when=fudge.Fake('verify_when_keyword', expect_call=True),
        then=fudge.Fake('verify_then_keyword', expect_call=True)
        )
    
    def verify_keyword(key):
        keywords[key].call()
    
    language_mock.expects('get') \
                 .with_args(fudge_arg.passes_test(verify_keyword)) \
                 .returns("Scenario")

    action_registry_mock = fudge.Fake('action_registry_mock')
    action_registry_mock.expects('suitable_for') \
                        .with_args("I do something", 'en-us') \
                        .returns((DoSomethingAction, [], {}))
    action_registry_mock.expects('suitable_for') \
                        .with_args("I do something else", 'en-us') \
                        .returns((DoSomethingElseAction, [], {}))
    action_registry_mock.expects('suitable_for') \
                        .with_args("I do yet another thing", 'en-us') \
                        .returns((DoYetAnotherThingAction, [], {}))

    parser = FileParser(language=language_mock, file_object=filemock, action_registry=action_registry_mock)

    fixture = parser.get_stories(settings=settings)

    assert_no_invalid_stories(fixture)

    assert len(fixture.stories) == 1, "Expected 1, Actual: %d" % len(fixture.stories)
    assert len(fixture.stories[0].scenarios) == 2
    assert fixture.stories[0].scenarios[1].whens[0].description == "#some custom comment"
