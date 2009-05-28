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

import pmock
from nose.tools import raises

from pyccuracy.pyccuracy_core import Settings
from pyccuracy.parsers import FileParser
from pyccuracy.fixture import Fixture

def test_can_create_file_parser():
    parser = FileParser()

    assert isinstance(parser, FileParser), "The created instance should be an instance of FileParser but was %s" % parser.__class__

def test_can_create_file_parser_with_mocked_filesystem():
    filemock = pmock.Mock()
    parser = FileParser(file_object=filemock)

    assert parser.file_object == filemock

def test_parsing_stories_returns_list():
    settings = Settings()
    filemock = pmock.Mock()
    filemock.expects(pmock.once()).list_files(directory=pmock.same(settings.tests_dir), pattern=pmock.same(settings.file_pattern)).will(pmock.return_value([]))
    parser = FileParser(file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert isinstance(fixture, Fixture)

def test_parsing_folder_with_no_stories_returns_empty_list():
    settings = Settings()
    files = []
    filemock = pmock.Mock()
    filemock.expects(pmock.once()).list_files(directory=pmock.same(settings.tests_dir), pattern=pmock.same(settings.file_pattern)).will(pmock.return_value(files))

    parser = FileParser(file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.stories) == 0
    filemock.verify()

def test_parsing_files_with_empty_content_returns_invalid_files_list():
    settings = Settings()
    files = ["some path"]

    story_text = ""

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).list_files(directory=pmock.same(settings.tests_dir), pattern=pmock.same(settings.file_pattern)).will(pmock.return_value(files))
    filemock.expects(pmock.once()).read_file(pmock.eq(files[0])).will(pmock.return_value(story_text))

    language_mock = pmock.Mock()
    language_mock.expects(pmock.once()).get(pmock.eq("as_a")).will(pmock.return_value("As a"))
    language_mock.expects(pmock.once()).get(pmock.eq("i_want_to")).will(pmock.return_value("I want to"))
    language_mock.expects(pmock.once()).get(pmock.eq("so_that")).will(pmock.return_value("So that"))
    language_mock.expects(pmock.once()).get(pmock.eq("no_header_failure")).will(pmock.return_value("No header found"))

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path == "some path"
    filemock.verify()
    
def test_parsing_files_with_invalid_as_a_returns_invalid_files_list():
    settings = Settings()
    files = ["some path"]
    
    story_text = """As someone
I want to do something
So that I'm happy"""

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).list_files(directory=pmock.same(settings.tests_dir), pattern=pmock.same(settings.file_pattern)).will(pmock.return_value(files))
    filemock.expects(pmock.once()).read_file(pmock.eq(files[0])).will(pmock.return_value(story_text))

    language_mock = pmock.Mock()
    language_mock.expects(pmock.once()).get(pmock.eq("as_a")).will(pmock.return_value("As a"))
    language_mock.expects(pmock.once()).get(pmock.eq("i_want_to")).will(pmock.return_value("I want to"))
    language_mock.expects(pmock.once()).get(pmock.eq("so_that")).will(pmock.return_value("So that"))
    language_mock.expects(pmock.once()).get(pmock.eq("no_header_failure")).will(pmock.return_value("No header found"))

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path == "some path"
    filemock.verify()

def test_parsing_files_with_invalid_i_want_to_returns_invalid_files_list():
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want something
So that I'm happy"""

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).list_files(directory=pmock.same(settings.tests_dir), pattern=pmock.same(settings.file_pattern)).will(pmock.return_value(files))
    filemock.expects(pmock.once()).read_file(pmock.eq(files[0])).will(pmock.return_value(story_text))

    language_mock = pmock.Mock()
    language_mock.expects(pmock.once()).get(pmock.eq("as_a")).will(pmock.return_value("As a"))
    language_mock.expects(pmock.once()).get(pmock.eq("i_want_to")).will(pmock.return_value("I want to"))
    language_mock.expects(pmock.once()).get(pmock.eq("so_that")).will(pmock.return_value("So that"))
    language_mock.expects(pmock.once()).get(pmock.eq("no_header_failure")).will(pmock.return_value("No header found"))

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path == "some path"
    filemock.verify()

def test_parsing_files_with_invalid_so_that_returns_invalid_files_list():
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want to do something
So I'm happy"""

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).list_files(directory=pmock.same(settings.tests_dir), pattern=pmock.same(settings.file_pattern)).will(pmock.return_value(files))
    filemock.expects(pmock.once()).read_file(pmock.eq(files[0])).will(pmock.return_value(story_text))

    language_mock = pmock.Mock()
    language_mock.expects(pmock.once()).get(pmock.eq("as_a")).will(pmock.return_value("As a"))
    language_mock.expects(pmock.once()).get(pmock.eq("i_want_to")).will(pmock.return_value("I want to"))
    language_mock.expects(pmock.once()).get(pmock.eq("so_that")).will(pmock.return_value("So that"))
    language_mock.expects(pmock.once()).get(pmock.eq("no_header_failure")).will(pmock.return_value("No header found"))

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.no_story_header) == 1
    file_path = fixture.no_story_header[0]
    assert file_path == "some path"
    filemock.verify()

def test_parsing_files_with_proper_header_returns_parsed_scenario():
    settings = Settings()
    files = ["some path"]
    
    story_text = """As a someone
I want to do something
So that I'm happy"""

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).list_files(directory=pmock.same(settings.tests_dir), pattern=pmock.same(settings.file_pattern)).will(pmock.return_value(files))
    filemock.expects(pmock.once()).read_file(pmock.eq(files[0])).will(pmock.return_value(story_text))

    language_mock = pmock.Mock()
    language_mock.expects(pmock.once()).get(pmock.eq("as_a")).will(pmock.return_value("As a"))
    language_mock.expects(pmock.once()).get(pmock.eq("i_want_to")).will(pmock.return_value("I want to"))
    language_mock.expects(pmock.once()).get(pmock.eq("so_that")).will(pmock.return_value("So that"))
    language_mock.expects(pmock.once()).get(pmock.eq("no_header_failure")).will(pmock.return_value("No header found"))

    parser = FileParser(language=language_mock, file_object=filemock)

    fixture = parser.get_stories(settings=settings)
    assert len(fixture.stories) == 1
    assert fixture.stories[0].as_a == "someone"
    assert fixture.stories[0].i_want_to == "do something"
    assert fixture.stories[0].so_that == "I'm happy"
    filemock.verify()

