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
from nose.tools import raises, set_trace
from pyccuracy.languages import LanguageGetter
from pyccuracy.errors import WrongArgumentsError

def test_language_getter_get():
    language = 'data1 = something\n' \
               'data2 = something else'

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).read().will(pmock.return_value(language))

    lg = LanguageGetter('en-us', file_object=filemock)
    lg.fill_data()

    assert lg.raw_data == language
    assert 'data' in lg.language_path
    assert lg.language_path.endswith('en-us.txt')
    assert lg.get('data1') == u'something'
    assert lg.get('data2') == u'something else'
    filemock.verify()

def test_laguage_getter_format_args():
    language = 'error_one_ok_args = you expected %s but got %s'

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).read().will(pmock.return_value(language))

    lg = LanguageGetter('en-us', file_object=filemock)
    lg.fill_data()

    assert lg.format('error_one_ok_args', 'X', 'Y') == u'you expected X but got Y'

def test_laguage_getter_format():
    language = 'error_one_ok_kwargs = you expected %(expected)s but got %(what_got)s'

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).read().will(pmock.return_value(language))

    lg = LanguageGetter('en-us', file_object=filemock)
    lg.fill_data()

    assert lg.format('error_one_ok_kwargs', expected='Xabba', what_got='Yabba') == u'you expected Xabba but got Yabba'

def test_laguage_getter_format_raises_too_many_args():
    language = 'error_two_too_many_args = impossible to check %s'

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).read().will(pmock.return_value(language))

    lg = LanguageGetter('en-us', file_object=filemock)
    lg.fill_data()

    @raises(WrongArgumentsError)
    def format_wrong_too_many_args():
        assert lg.format('error_two_too_many_args', 'X', '!Y') != u'impossible to check X'

    format_wrong_too_many_args()

def test_laguage_getter_format_raises_not_enough_args():
    language = 'error_three_not_enough_args = impossible to check %s in %s\n'

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).read().will(pmock.return_value(language))

    lg = LanguageGetter('en-us', file_object=filemock)
    lg.fill_data()

    @raises(WrongArgumentsError)
    def format_wrong_not_enough_args():
        assert lg.format('error_three_not_enough_args', 'X') != u'impossible to check X in %s'

    format_wrong_not_enough_args()

def test_laguage_getter_format_raises_args_got_kwargs():
    language = 'error_five_args_got_kwargs = impossible to check %s'

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).read().will(pmock.return_value(language))

    lg = LanguageGetter('en-us', file_object=filemock)
    lg.fill_data()

    @raises(WrongArgumentsError)
    def format_wrong_args_got_kwargs():
        assert lg.format('error_five_args_got_kwargs', what='X') != u'impossible to check X in %s'
    format_wrong_args_got_kwargs()

def test_laguage_getter_format_raises_kwargs_got_args():
    language = 'error_six_kwargs_got_args = impossible to check %(param)s'

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).read().will(pmock.return_value(language))

    lg = LanguageGetter('en-us', file_object=filemock)
    lg.fill_data()

    @raises(WrongArgumentsError)
    def format_wrong_args_got_kwargs():
        assert lg.format('error_six_kwargs_got_args', 'X') != u'impossible to check X in %s'
    format_wrong_args_got_kwargs()

