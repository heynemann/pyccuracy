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

from pyccuracy.page import PageRegistry, Page
from pyccuracy.actions import ActionBase
from pyccuracy.languages import LanguageItem

def resolve_element_key(context, element_type, element_name, resolve_function):
    element_category = context.language.get(element_type.encode("utf-8") + "_category")
    return resolve_function(context, element_category, element_name)

class TableMatchAction(ActionBase):
    '''h3. Example

  * And I see "some" table as:
        | Name | Age | Sex  |
        | John | 28  | Male |
        | Paul | 30  | Male | 

h3. Description

This action asserts that the given table matches the one the user specified.'''
    __builtin__ = True
    regex = LanguageItem("table_match_regex")

    def execute(self, context, table_name, table):
        element_type = Page.Table
        element_key = self.resolve_element_key(context, element_type, table_name)

        error_message = context.language.format("element_is_visible_failure", "table", table_name)
        self.assert_element_is_visible(context, element_key, error_message)

        rows = context.browser_driver.get_table_rows(element_key)

        error_table_keys = " | ".join(table[0].keys())
        error_table_format = "\n".join([" | ".join(item.values()) for item in table])
        error_rows_format = [" | ".join(item) for item in rows]
        error_message = context.language.format(
                                            "table_invalid_data_failure", 
                                            table_name, 
                                            error_table_keys,
                                            error_table_format, 
                                            error_rows_format)
                
        if not rows or len(rows) <= len(table) :
            raise self.failed(error_message)
        
        actual_keys = rows[0]
        
        for row_index, row in enumerate(rows[1:]):
            if len(row) != len(actual_keys):
                raise self.failed(error_message)
                 
            for cell_index, cell in enumerate(row):
                if cell != table[row_index][actual_keys[cell_index]]:
                    raise self.failed(error_message)
