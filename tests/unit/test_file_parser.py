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
from nose.tools import raises

from pyccuracy.common import Settings
from pyccuracy.parsers import FileParser
from pyccuracy.fixture import Fixture
from pyccuracy.fixture_items import Story

def assert_no_invalid_stories(fixture):
    if fixture.invalid_test_files:
        raise fixture.invalid_test_files[0][1]

def test_can_create_file_parser():
    parser = FileParser()

    assert isinstance(parser, FileParser), "The created instance should be an instance of FileParser but was %s" % parser.__class__

def test_can_create_file_parser_with_mocked_filesystem():
    
    mocker = Mocker()
    
    filemock = mocker.mock()
    parser = FileParser(file_object=filemock)

    assert parser.file_object == filemock

def test_parsing_stories_returns_list():
    
    mocker = Mocker()
    
    settings = Settings()
    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result([])
    
    with mocker:
        parser = FileParser(file_object=filemock)
    
        fixture = parser.get_stories(settings=settings)
        assert isinstance(fixture, Fixture)

def test_parsing_folder_with_no_stories_returns_empty_list():
    
    mocker = Mocker()
    
    settings = Settings()
    files = []
    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result(files)

    with mocker:
        parser = FileParser(file_object=filemock)
    
        fixture = parser.get_stories(settings=settings)
        assert len(fixture.stories) == 0

def test_parsing_files_with_empty_content_returns_invalid_files_list():
    
    mocker = Mocker()
    
    settings = Settings()
    files = ["some path"]

    story_text = ""

    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result(files)
    filemock.read_file(files[0])
    mocker.result(story_text)

    language_mock = mocker.mock()
    language_mock.get("as_a")
    mocker.result("As a")
    language_mock.get("i_want_to")
    mocker.result("I want to")
    language_mock.get("so_that")
    mocker.result("So that")
    language_mock.get("no_header_failure")
    mocker.result("No header found")

    with mocker:
        parser = FileParser(language=language_mock, file_object=filemock)
    
        fixture = parser.get_stories(settings=settings)
        assert len(fixture.no_story_header) == 1
        file_path = fixture.no_story_header[0]
        assert file_path == "some path"

def test_parsing_files_with_invalid_as_a_returns_invalid_files_list():
    
    mocker = Mocker()
    
    settings = Settings()
    files = ["some path"]
    
    story_text = """As someone
I want to do something
So that I'm happy"""

    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result(files)
    filemock.read_file(files[0])
    mocker.result(story_text)

    language_mock = mocker.mock()
    language_mock.get("as_a")
    mocker.result("As a")
    language_mock.get("i_want_to")
    mocker.result("I want to")
    language_mock.get("so_that")
    mocker.result("So that")
    language_mock.get("no_header_failure")
    mocker.result("No header found")

    with mocker:
        parser = FileParser(language=language_mock, file_object=filemock)
    
        fixture = parser.get_stories(settings=settings)
        assert len(fixture.no_story_header) == 1
        file_path = fixture.no_story_header[0]
        assert file_path == "some path"

def test_parsing_files_with_invalid_i_want_to_returns_invalid_files_list():
    
    mocker = Mocker()
    
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want something
So that I'm happy"""

    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result(files)
    filemock.read_file(files[0])
    mocker.result(story_text)

    language_mock = mocker.mock()
    language_mock.get("as_a")
    mocker.result("As a")
    language_mock.get("i_want_to")
    mocker.result("I want to")
    language_mock.get("so_that")
    mocker.result("So that")
    language_mock.get("no_header_failure")
    mocker.result("No header found")

    with mocker:
        parser = FileParser(language=language_mock, file_object=filemock)
    
        fixture = parser.get_stories(settings=settings)
        assert len(fixture.no_story_header) == 1
        file_path = fixture.no_story_header[0]
        assert file_path == "some path"

def test_parsing_files_with_invalid_so_that_returns_invalid_files_list():
    
    mocker = Mocker()
    
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want to do something
So I'm happy"""

    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result(files)
    filemock.read_file(files[0])
    mocker.result(story_text)

    language_mock = mocker.mock()
    language_mock.get("as_a")
    mocker.result("As a")
    language_mock.get("i_want_to")
    mocker.result("I want to")
    language_mock.get("so_that")
    mocker.result("So that")
    language_mock.get("no_header_failure")
    mocker.result("No header found")

    with mocker:
        parser = FileParser(language=language_mock, file_object=filemock)
    
        fixture = parser.get_stories(settings=settings)
        assert len(fixture.no_story_header) == 1
        file_path = fixture.no_story_header[0]
        assert file_path == "some path"

def test_parsing_files_with_proper_header_returns_parsed_scenario():
    
    mocker = Mocker()
    
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want to do something
So that I'm happy"""

    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result(files)
    filemock.read_file(files[0])
    mocker.result(story_text)

    language_mock = mocker.mock()
    language_mock.get("as_a")
    mocker.result("As a")
    language_mock.get("i_want_to")
    mocker.result("I want to")
    language_mock.get("so_that")
    mocker.result("So that")

    with mocker:
        parser = FileParser(language=language_mock, file_object=filemock)
    
        fixture = parser.get_stories(settings=settings)
        assert len(fixture.stories) == 1
        assert fixture.stories[0].as_a == "someone"
        assert fixture.stories[0].i_want_to == "do something"
        assert fixture.stories[0].so_that == "I'm happy"

def test_is_scenario_starter_line():
    
    mocker = Mocker()
    
    language_mock = mocker.mock()
    language_mock.get("scenario")
    mocker.result("Scenario")

    with mocker:
        parser = FileParser(language=language_mock, file_object=None)
        is_scenario_starter_line = parser.is_scenario_starter_line("Scenario bla")
        
        assert is_scenario_starter_line

def test_is_not_scenario_starter_line():
    
    mocker = Mocker()
    
    language_mock = mocker.mock()
    language_mock.get("scenario")
    mocker.result("Scenario")

    with mocker:
        parser = FileParser(language=language_mock, file_object=None)
        is_scenario_starter_line = parser.is_scenario_starter_line("Cenario bla")
        
        assert not is_scenario_starter_line

def test_parse_scenario_line():
    
    mocker = Mocker()
    
    story = Story(as_a="Someone", i_want_to="Do Something", so_that="I'm Happy", identity="some file")

    settings_mock = mocker.mock()
    settings_mock.scenarios_to_run
    mocker.result([])
    
    language_mock = mocker.mock()
    language_mock.get("scenario")
    mocker.result("Scenario")

    with mocker:
        parser = FileParser(language=language_mock, file_object=None)
        scenario = parser.parse_scenario_line(story, "Scenario 1 - Doing something", settings_mock)
    
        assert scenario is not None
        assert scenario.index == "1", "Expected 1 actual %s" % scenario.index
        assert scenario.title == "Doing something"

def test_is_keyword():
    
    mocker = Mocker()
    
    language_mock = mocker.mock()
    language_mock.get("keyword")
    mocker.result("kw")

    with mocker:
        parser = FileParser(language=language_mock, file_object=None)
        is_keyword = parser.is_keyword("kw", "keyword")
    
        assert is_keyword

def test_is_not_keyword():
    
    mocker = Mocker()
    
    language_mock = mocker.mock()
    language_mock.get("keyword")
    mocker.result("kw")

    with mocker:
        parser = FileParser(language=language_mock, file_object=None)
        is_keyword = parser.is_keyword("other", "keyword")
    
        assert not is_keyword

def test_parsing_files_with_proper_scenario_returns_parsed_scenario():
    
    mocker = Mocker()
    
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

    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result(files)
    filemock.read_file(files[0])
    mocker.result(story_text)

    language_mock = mocker.mock()
    language_mock.get("as_a")
    mocker.result("As a")
    language_mock.get("i_want_to")
    mocker.result("I want to")
    language_mock.get("so_that")
    mocker.result("So that")
    language_mock.get("given")
    mocker.result("Given")
    mocker.count(min=1, max=None)
    language_mock.get("when")
    mocker.result("When")
    mocker.count(min=1, max=None)
    language_mock.get("then")
    mocker.result("Then")
    mocker.count(min=1, max=None)
    language_mock.get("scenario")
    mocker.result("Scenario")
    mocker.count(min=1, max=None)

    action_registry_mock = mocker.mock()
    action_registry_mock.suitable_for("I do something", 'en-us')
    mocker.result((DoSomethingAction, [], {}))
    action_registry_mock.suitable_for("I do something else", 'en-us')
    mocker.result((DoSomethingElseAction, [], {}))
    action_registry_mock.suitable_for("I do yet another thing", 'en-us')
    mocker.result((DoYetAnotherThingAction, [], {}))

    with mocker:
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

def test_parsing_files_with_many_scenarios_returns_parsed_scenarios():
    
    mocker = Mocker()
    
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

    filemock = mocker.mock()
    filemock.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
    mocker.result(files)
    filemock.read_file(files[0])
    mocker.result(story_text)

    language_mock = mocker.mock()
    language_mock.get("as_a")
    mocker.result("As a")
    language_mock.get("i_want_to")
    mocker.result("I want to")
    language_mock.get("so_that")
    mocker.result("So that")
    language_mock.get("given")
    mocker.result("Given")
    mocker.count(min=1, max=None)
    language_mock.get("when")
    mocker.result("When")
    mocker.count(min=1, max=None)
    language_mock.get("then")
    mocker.result("Then")
    mocker.count(min=1, max=None)
    language_mock.get("scenario")
    mocker.result("Scenario")
    mocker.count(min=1, max=None)

    action_registry_mock = mocker.mock()
    action_registry_mock.suitable_for("I do something", 'en-us')
    mocker.result((DoSomethingAction, [], {}))
    mocker.count(min=1, max=None)
    action_registry_mock.suitable_for("I do something else", 'en-us')
    mocker.result((DoSomethingElseAction, [], {}))
    mocker.count(min=1, max=None)
    action_registry_mock.suitable_for("I do yet another thing", 'en-us')
    mocker.result((DoYetAnotherThingAction, [], {}))
    mocker.count(min=1, max=None)

    with mocker:
        parser = FileParser(language=language_mock, file_object=filemock, action_registry=action_registry_mock)
    
        fixture = parser.get_stories(settings=settings)
    
        assert_no_invalid_stories(fixture)
    
        assert len(fixture.stories) == 1, "Expected 1, Actual: %d" % len(fixture.stories)
        assert len(fixture.stories[0].scenarios) == 2
        assert fixture.stories[0].scenarios[1].whens[0].description == "#some custom comment"
