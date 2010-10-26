#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from mocker import Mocker

from pyccuracy.common import URLChecker

def test_url_checker():
    
    mocker = Mocker()
    
    urlmock = mocker.mock()

    urlmock.urlopen("http://foo.bar.com")
    mocker.result(None)

    with mocker:
        checker = URLChecker(lib=urlmock)
        checker.set_url("http://foo.bar.com")
    
        assert checker.url == "http://foo.bar.com"
        assert checker.is_valid()
        assert checker.exists()

def test_url_checker_with_port():
    
    mocker = Mocker()
    
    urlmock = mocker.mock()

    urlmock.urlopen("http://foo.bar.com:8080")
    mocker.result(None)

    with mocker:
        checker = URLChecker(lib=urlmock)
        checker.set_url("http://foo.bar.com:8080")
    
        assert checker.url == "http://foo.bar.com:8080"
        assert checker.is_valid()
        assert checker.exists()

def test_url_checker_with_port_with_sub_folder():
    
    mocker = Mocker()
    
    urlmock = mocker.mock()

    urlmock.urlopen("http://foo.bar.com:8080/login")
    mocker.result(None)

    with mocker:
        checker = URLChecker(lib=urlmock)
        checker.set_url("http://foo.bar.com:8080/login")
    
        assert checker.url == "http://foo.bar.com:8080/login"
        assert checker.is_valid()
        assert checker.exists()

def test_url_checker_with_port_with_sub_folder_in_localhost():
    
    mocker = Mocker()
    
    urlmock = mocker.mock()

    urlmock.urlopen("http://localhost:8080/login")
    mocker.result(None)

    with mocker:
        checker = URLChecker(lib=urlmock)
        checker.set_url("http://localhost:8080/login")
    
        assert checker.url == "http://localhost:8080/login"
        assert checker.is_valid()
        assert checker.exists()
