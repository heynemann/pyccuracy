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
from pyccuracy.languages import LanguageGetter

def test_language_getter_get():
    language = 'data1 = something\n' \
               'data2 = something else'

    filemock = pmock.Mock()
    filemock.expects(pmock.once()).read().will(pmock.return_value(language))

    lg = LanguageGetter('pt-br', file_object=filemock)
    lg.fill_data()

    assert lg.raw_data == language
    assert 'data' in lg.language_path
    assert lg.language_path.endswith('pt-br.txt')
    assert lg.get('data1') == u'something'
    assert lg.get('data2') == u'something else'
    filemock.verify()
