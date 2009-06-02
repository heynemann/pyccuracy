# -*- coding: utf-8 -*-
import os
from nose.tools import raises, set_trace
from pyccuracy.languages import LanguageGetter, AVAILABLE_LANGUAGES

def test_pt_br_exists():
    lg = LanguageGetter('pt-br')
    assert os.path.exists(lg.language_path), "There is no language file for pt-br culture: %s" % lg.language_path

def test_pt_br_basic_items():
    lg = LanguageGetter('pt-br')
    assert lg.get('as_a')
    assert lg.get('i_want_to')
    assert lg.get('so_that')
    assert lg.get('scenario')
    assert lg.get('given')
    assert lg.get('when')
    assert lg.get('then')
    assert lg.get('invalid_test_files')
    assert lg.get('files_without_header')
    assert lg.get('story_status')

def test_en_us_exists():
    lg = LanguageGetter('en-us')
    assert os.path.exists(lg.language_path), "There is no language file for en-us culture: %s" % lg.language_path

def test_en_us_basic_items():
    lg = LanguageGetter('en-us')
    assert lg.get('as_a')
    assert lg.get('i_want_to')
    assert lg.get('so_that')
    assert lg.get('scenario')
    assert lg.get('given')
    assert lg.get('when')
    assert lg.get('then')
    assert lg.get('invalid_test_files')
    assert lg.get('files_without_header')
    assert lg.get('story_status')

def test_available_languages():
    assert 'pt-br' in AVAILABLE_LANGUAGES
    assert 'en-us' in AVAILABLE_LANGUAGES
