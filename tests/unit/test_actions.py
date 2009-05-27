# -*- coding: utf-8 -*-

from nose.tools import raises, set_trace

from pyccuracy import ActionBase

def test_construction():
    class DoNothingAction(ActionBase):
        regex = r'^My Regex$'
        def execute(self, context, *args, **kwargs):
            pass

    assert DoNothingAction.regex == r'^My Regex$'

@raises(NotImplementedError)
def test_construction_fails_without_implementing_execute():
    class DoNothingAction(ActionBase):
        regex = r'^My Regex$'

@raises(NotImplementedError)
def test_construction_fails_without_implementing_setting_regex():
    class DoNothingAction(ActionBase):
        def execute(self, context, *args, **kw):
            pass

@raises(NotImplementedError)
def test_construction_fails_without_implementing_basic_attrs():
    class DoNothingAction(ActionBase):
        pass

@raises(TypeError)
def test_construction_fails_if_regex_nonstring():
    class DoNothingAction(ActionBase):
        regex = range(10)
        def execute(self, context, *args, **kw):
            pass

def test_can_resolves_string():
    class DoSomethingAction(ActionBase):
        regex = r'^(And )?I do "(?P<what>\w+)"$'
        def execute(self, context, *args, **kwargs):
            pass

    assert DoSomethingAction.can_resolve('And I do "test"')
    assert DoSomethingAction.can_resolve('I do "test"')

def test_can_not_resolves_string():
    class DoSomethingAction(ActionBase):
        regex = r'^(And )?I do "(?P<what>\w+)"$'
        def execute(self, context, *args, **kwargs):
            pass

    assert not DoSomethingAction.can_resolve('Not for me')
    assert not DoSomethingAction.can_resolve('Foo Bar')

# def test_execute_takes_regex_groups_as_args_and_kwargs():
#     class DoSomethingAction(ActionBase):
#         regex = r'^(And )?I do "(?P<what>[\w\s]+)"$'

#         def execute(self, context, *args, **kwargs):
#             assert args[0] == 'And '
#             assert kwargs['what'] == 'mock things'

#     my_action = DoSomethingAction(None, None)
#     re
#     assert my_action.execute('And I do "mock things"', None, )
