# -*- coding: utf-8 -*-
import pmock
from nose.tools import raises, set_trace
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
