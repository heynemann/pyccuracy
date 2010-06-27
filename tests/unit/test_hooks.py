from pmock import *
from nose.tools import raises

from pyccuracy.hooks import HOOKS, Hooks, AfterTestsHook

@raises(NotImplementedError)
def test_construction_fails_without_implementing_execute():
    class DoNothing(AfterTestsHook):
        pass

def test_will_register_after_tests_hook():
    class SomeHook(AfterTestsHook):
        def execute(self, result):
            pass

    assert SomeHook in HOOKS['after_tests']

def test_will_execute_my_hook():
    result_mock = Mock()
    result_mock.expects(once()).method('a_method')
    
    class MyHook(AfterTestsHook):
        def execute(self, result):
            result.a_method()
    
    Hooks.execute_after_tests(result_mock)
    result_mock.verify()