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

import fudge
from pyccuracy.common import URLChecker
from nose.tools import with_setup

def teardown():
    fudge.clear_expectations()

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_url_checker():

    urlmock = fudge.Fake('urlmock').expects('urlopen') \
        .with_args("http://foo.bar.com") \
        .returns(None)\
        .times_called(1)

    checker = URLChecker(lib=urlmock)
    checker.set_url("http://foo.bar.com")

    assert checker.url == "http://foo.bar.com"
    assert checker.is_valid()
    assert checker.exists()

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_url_checker_with_port():

    urlmock = fudge.Fake('urlmock')\
            .expects('urlopen') \
            .with_args("http://foo.bar.com:8080") \
            .returns(None)\
            .times_called(1)

    checker = URLChecker(lib=urlmock)
    checker.set_url("http://foo.bar.com:8080")

    assert checker.url == "http://foo.bar.com:8080"
    assert checker.is_valid()
    assert checker.exists()

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_url_checker_with_port_with_sub_folder():
    urlmock = fudge.Fake('urlmock')\
            .expects('urlopen') \
            .with_args("http://foo.bar.com:8080/login") \
            .returns(None)\
            .times_called(1)

    checker = URLChecker(lib=urlmock)
    checker.set_url("http://foo.bar.com:8080/login")

    assert checker.url == "http://foo.bar.com:8080/login"
    assert checker.is_valid()
    assert checker.exists()

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_url_checker_with_port_with_sub_folder_in_localhost():
    urlmock = fudge.Fake('urlmock')\
            .expects('urlopen') \
            .with_args("http://localhost:8080/login") \
            .returns(None)\
            .times_called(1)

    checker = URLChecker(lib=urlmock)
    checker.set_url("http://localhost:8080/login")

    assert checker.url == "http://localhost:8080/login"
    assert checker.is_valid()
    assert checker.exists()
