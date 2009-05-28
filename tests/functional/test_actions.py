# -*- coding: utf-8 -*-
from pmock import *

from nose.tools import raises, set_trace
from pyccuracy import ActionRegistry, ActionBase
from pyccuracy.languages import LanguageItem

def test_get_suitable_action():
    Action, args, kw = ActionRegistry.suitable_for(u'I see "Welcome to Pyccuracy" title', 'en-us')
    assert issubclass(Action, ActionBase)
    assert isinstance(args, (list, tuple))
    assert isinstance(kw, dict)
    assert args[1] == u'Welcome to Pyccuracy'

def test_do_not_get_suitable_action():
    Action, args, kw = ActionRegistry.suitable_for(u'Blah bluh foo bar', 'en-us')
    assert Action is None
    assert args is None
    assert kw is None

def test_action_registry_suitable_for_returns_type_on_match():
    language_getter_mock = Mock()
    language_getter_mock.expects(once()).get(eq(LanguageItem('page_see_title_regex'))).will(return_value('I see "foo" title'))
    Action, args, kwargs = ActionRegistry.suitable_for('I see "foo" title', 'en-us', getter=language_getter_mock)
    language_getter_mock.verify()
    assert isinstance(Action, type)
