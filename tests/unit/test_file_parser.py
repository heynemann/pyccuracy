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

    stories = parser.get_stories(settings=settings)
    assert isinstance(stories, (list,tuple))

def test_parsing_folder_with_no_stories_returns_empty_list():
    settings = Settings()
    files = []
    filemock = pmock.Mock()
    filemock.expects(pmock.once()).list_files(directory=pmock.same(settings.tests_dir), pattern=pmock.same(settings.file_pattern)).will(pmock.return_value(files))

    parser = FileParser(file_object=filemock)

    stories = parser.get_stories(settings=settings)
    assert len(stories) == 0
    filemock.verify()

