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

from os.path import join, dirname, abspath

from pyccuracy.common import Settings
from pyccuracy.parsers import FileParser
from pyccuracy.fixture import Fixture
from pyccuracy.fixture_items import Story
from pyccuracy import ActionBase

def assert_no_invalid_stories(fixture):
    if fixture.invalid_test_files:
        raise fixture.invalid_test_files[0][1]

def test_parsing_folder_with_no_stories_returns_empty_list():
    settings = Settings()
    settings.tests_dirs = [abspath(join(dirname(__file__), "no_stories_folder"))]
    parser = FileParser()

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.stories) == 0

def test_parsing_files_with_empty_content_returns_no_story_header_list():
    settings = Settings()
    settings.tests_dirs = [abspath(join(dirname(__file__), "invalid_content_stories"))]
    settings.file_pattern = "empty_story.acc"

    parser = FileParser()

    fixture = parser.get_stories(settings=settings)

    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path.endswith("empty_story.acc")

def test_parsing_files_with_wrong_content_returns_no_story_header_list():
    settings = Settings()
    settings.tests_dirs = [abspath(join(dirname(__file__), "invalid_content_stories"))]
    settings.file_pattern = "invalid_story.acc"

    parser = FileParser()

    fixture = parser.get_stories(settings=settings)

    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path.endswith("invalid_story.acc")

def test_parsing_files_with_wrong_as_a_returns_no_story_header_list():
    settings = Settings()
    settings.tests_dirs = [abspath(join(dirname(__file__), "invalid_content_stories"))]
    settings.file_pattern = "invalid_as_a.acc"

    parser = FileParser()

    fixture = parser.get_stories(settings=settings)

    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path.endswith("invalid_as_a.acc")
    
def test_parsing_files_with_wrong_i_want_to_returns_no_story_header_list():
    settings = Settings()
    settings.tests_dirs = [abspath(join(dirname(__file__), "invalid_content_stories"))]
    settings.file_pattern = "invalid_i_want_to.acc"

    parser = FileParser()

    fixture = parser.get_stories(settings=settings)

    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path.endswith("invalid_i_want_to.acc")
    
def test_parsing_files_with_wrong_so_that_returns_no_story_header_list():
    settings = Settings()
    settings.tests_dirs = [abspath(join(dirname(__file__), "invalid_content_stories"))]
    settings.file_pattern = "invalid_so_that.acc"

    parser = FileParser()

    fixture = parser.get_stories(settings=settings)

    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path.endswith("invalid_so_that.acc")

def test_parsing_files_with_many_scenarios_returns_parsed_scenarios():
    class DoSomethingAction(ActionBase):
        regex = r'I do something$'
        def execute(context, *args, **kwargs):
            pass

    class DoSomethingElseAction(ActionBase):
        regex = r'I do something else$'
        def execute(context, *args, **kwargs):
            pass

    class DoYetAnotherThingAction(ActionBase):
        regex = r'I do yet another thing$'
        def execute(context, *args, **kwargs):
            pass

    settings = Settings()
    settings.tests_dirs = [abspath(dirname(__file__))]
    settings.file_pattern = "some_test.acc"

    parser = FileParser()

    fixture = parser.get_stories(settings=settings)

    assert_no_invalid_stories(fixture)

    assert len(fixture.stories) == 1, "Expected 1, Actual: %d" % len(fixture.stories)
    assert len(fixture.stories[0].scenarios) == 2
    assert fixture.stories[0].scenarios[1].whens[0].description == "#some custom comment"

