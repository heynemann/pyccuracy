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
from pyccuracy.fixture_items import Story

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
    story = Story("some","other","data")
    fixture.append_story(story)
    assert len(fixture.stories) == 1

def test_append_story_keeps_data():
    fixture = Fixture()
    story = Story("some","other","data")
    fixture.append_story(story)
    assert fixture.stories[0].as_a == "some"
    assert fixture.stories[0].i_want_to == "other"
    assert fixture.stories[0].so_that == "data"

