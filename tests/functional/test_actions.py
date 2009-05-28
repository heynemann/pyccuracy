# -*- coding: utf-8 -*-

from nose.tools import raises, set_trace
from pyccuracy import ActionRegistry, ActionBase

def test_get_suitable_action():
    Action, args, kw = ActionRegistry.suitable_for(u'I see "Welcome to Pyccuracy" title', 'en-us')
    assert issubclass(Action, ActionBase)
    assert isinstance(args, (list, tuple))
    assert isinstance(kw, dict)
    assert args[1] == u'Welcome to Pyccuracy'
