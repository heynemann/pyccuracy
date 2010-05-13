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

from pmock import *
from nose.tools import *

from pyccuracy.parsers import FileParser

def test_parse_block_lines():
    parser = FileParser(None, None, None)
    
    line_index = 5
    line = "And I see table as:"
    scenario_lines = [
        'Line 1',
        'Line 2',
        'Line 3',
        'Scenario bla',
        'Given',
        '    And I see table as:',
        '        | Name | Age | Sex  |',
        '        | Paul | 28  | Male |',
        '        | John | 30  | Male |'
    ]
    offset, rows, parsed_rows = parser.parse_rows(line_index, line, scenario_lines)
    
    assert offset == 3
    assert rows == [
        '        | Name | Age | Sex  |',
        '        | Paul | 28  | Male |',
        '        | John | 30  | Male |'
    ]
    assert parsed_rows == [
                        {
                            'Name':'Paul',
                            'Age':'28',
                            'Sex':'Male'
                        },
                        {
                            'Name':'John',
                            'Age':'30',
                            'Sex':'Male'
                        }
                   ]
