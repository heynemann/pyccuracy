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

from re import compile as re_compile

from utils import assert_raises
from pyccuracy.common import Settings
from pyccuracy.page import PageRegistry, Page

def test_page_registry_resolve_raises_with_wrong_none_settings():
    def do_resolve_fail():
        PageRegistry.resolve(None, 'http://google.com')

    exc = 'PageRegistry.resolve takes a pyccuracy.common.Settings ' \
          'object first parameter. Got None.'
    assert_raises(TypeError, do_resolve_fail,
                  exc_pattern=re_compile(exc))

def test_page_registry_resolve_raises_with_wrong_none_settings_and_none_url():
    def do_resolve_fail():
        PageRegistry.resolve(None, None)

    exc = 'PageRegistry.resolve takes a pyccuracy.common.Settings ' \
          'object first parameter. Got None.'
    assert_raises(TypeError, do_resolve_fail,
                  exc_pattern=re_compile(exc))

def test_page_registry_resolve_raises_with_wrong_none_url():
    def do_resolve_fail():
        PageRegistry.resolve(Settings(), None)

    exc = 'PageRegistry.resolve argument 2 must be a string. Got None.'
    assert_raises(TypeError, do_resolve_fail,
                  exc_pattern=re_compile(exc))

def test_page_registry_does_not_raises_when_must_raise_is_false():
    assert PageRegistry.resolve(None, None, must_raise=False) is None

def test_page_registry_resolve_by_page_class_name_get_right_class():
    class MyPage(Page):
        url = 'blabla'

    PageGot, url = PageRegistry.resolve(Settings(), 'My Page')
    assert PageGot is MyPage, 'The page resolved by "My Page" should be a type class: MyPage. Got %r.' % PageGot

def test_page_registry_resolve_by_page_class_name_with_base_url_get_right_url():
    class MyPage(Page):
        url = 'blabla'

    PageGot, url = PageRegistry.resolve(Settings({'base_url': 'http://pyccuracy.org'}), 'My Page')
    assert PageGot is MyPage, 'The page resolved by "My Page" should be a type class: MyPage. Got %r.' % PageGot
    assert url == 'http://pyccuracy.org/blabla', 'The url must be http://pyccuracy.org concatenated with "/" and "blabla". Got "%s".' % url

def test_page_registry_resolve_by_page_class_name_with_base_url_get_right_url_without_slash():
    class MyPage(Page):
        url = 'blabla'

    PageGot, url = PageRegistry.resolve(Settings(cur_dir='/home'), 'My Page')

    assert PageGot is MyPage, 'The page resolved by "My Page" should be a type class: MyPage. Got %r.' % PageGot
    assert url == 'file:///home/blabla', 'The url must be "file:///home" concatenated with "/" and "blabla". Got "%s".' % url

def test_page_registry_resolve_by_page_class_name_with_base_url_get_right_url_with_slash():
    class MyPage(Page):
        url = 'blabla'

    PageGot, url = PageRegistry.resolve(Settings(cur_dir='/home/'), 'My Page')

    assert PageGot is MyPage, 'The page resolved by "My Page" should be a type class: MyPage. Got %r.' % PageGot
    assert url == 'file:///home/blabla', 'The url must be "file:///home" concatenated with "/" and "blabla". Got "%s".' % url

def test_page_registry_resolve_by_page_class_name_with_base_url_get_right_url_with_slash():
    class MyPage(Page):
        url = 'blabla'

    PageGot, url = PageRegistry.resolve(Settings(cur_dir='/home/'), 'My Page')

    assert PageGot is MyPage, 'The page resolved by "My Page" should be a type class: MyPage. Got %r.' % PageGot
    assert url == 'file:///home/blabla', 'The url must be "file:///home" concatenated with "/" and "blabla". Got "%s".' % url

def test_page_registry_resolve_page_by_url_with_base_url():
    class MyPage(Page):
        url = 'my_url'

    PageGot, url = PageRegistry.resolve(Settings({'base_url': 'http://pyccuracy.org'}), 'my_url')

    assert PageGot is MyPage, 'The page resolved by "my_url" should be a type class: MyPage. Got %r.' % PageGot
    assert url == 'http://pyccuracy.org/my_url', 'The url must be "http://pyccuracy.org/my_url". Got "%s".' % url

def test_page_registry_resolve_page_by_url_without_base_url_with_slash():
    class MyPage(Page):
        url = 'my_url'

    PageGot, url = PageRegistry.resolve(Settings(cur_dir='/test/'), 'my_url')

    assert PageGot is MyPage, 'The page resolved by "my_url" should be a type class: MyPage. Got %r.' % PageGot
    assert url == 'file:///test/my_url', 'The url must be "file:///test/my_url". Got "%s".' % url

def test_page_registry_resolve_page_by_url_without_base_url_without_slash():
    class MyPage(Page):
        url = 'my_url'

    PageGot, url = PageRegistry.resolve(Settings(cur_dir='/test'), 'my_url')

    assert PageGot is MyPage, 'The page resolved by "my_url" should be a type class: MyPage. Got %r.' % PageGot
    assert url == 'file:///test/my_url', 'The url must be "file:///test/my_url". Got "%s".' % url
