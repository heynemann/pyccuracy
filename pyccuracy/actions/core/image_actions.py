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

class ImageHasSrcOfAction(ActionBase):
    '''h3. Example

  * And I see "logo" image has src of "images/logo.png"

h3. Description

This action asserts that an image has the given src attribute.'''
    __builtin__ = True
    regex = LanguageItem("image_has_src_regex")

    def execute(self, context, image_name, src):
        image = self.resolve_element_key(context, Page.Image, image_name)

        error_message = context.language.format("element_is_visible_failure", "image", image_name)
        self.assert_element_is_visible(context, image, error_message)
        
        current_src = context.browser_driver.get_image_src(image)
        if src.lower() != current_src.lower():
            error_message = self.language.format("image_has_src_failure", image_name, src, current_src)
            raise self.failed(error_message)

class ImageDoesNotHaveSrcOfAction(ActionBase):
    '''h3. Example

  * And I see "logo" image does not have src of "images/logo.png"

h3. Description

This action asserts that an image does not have the given src attribute.'''
    __builtin__ = True
    regex = LanguageItem("image_does_not_have_src_regex")

    def execute(self, context, image_name, src):
        image = self.resolve_element_key(context, Page.Image, image_name)

        error_message = context.language.format("element_is_visible_failure", "image", image_name)
        self.assert_element_is_visible(context, image, error_message)
        
        current_src = context.browser_driver.get_image_src(image)
        if src.lower() == current_src.lower():
            error_message = self.language.format("image_does_not_have_src_failure", image_name, src, current_src)
            raise self.failed(error_message)
