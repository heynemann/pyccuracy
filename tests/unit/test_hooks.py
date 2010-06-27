from pmock import *
from nose.tools import raises
from time import sleep

from pyccuracy.hooks import HOOKS, Hooks, AfterTestsHook, HookError

@raises(NotImplementedError)
def test_construction_fails_without_implementing_execute():
    class DoNothing(AfterTestsHook):
        pass
    Hooks.reset()

def test_will_register_after_tests_hook():
    class SomeHook(AfterTestsHook):
        def execute(self, result):
            pass

    assert SomeHook in HOOKS['after_tests']
    Hooks.reset()

def test_will_execute_my_hook():
    result_mock = Mock()
    result_mock.expects(once()).method('a_method')
    
    class MyHook(AfterTestsHook):
        def execute(self, result):
            result.a_method()
    
    Hooks.execute_after_tests(result_mock)
    result_mock.verify()
    Hooks.reset()

@raises(HookError)
def test_user_exceptions_make_pyccuracy_raises_hook_error():
    class BrokenHook(AfterTestsHook):
        def execute(self, results):
            raise Exception("user did stupid things")
    
    Hooks.execute_after_tests(None)
    Hooks.reset()

def test_reset_hooks():
    Hooks.reset()
    class AHook(AfterTestsHook):
        def execute(self, results):
            pass
    assert len(HOOKS['after_tests']) == 1
    assert AHook in HOOKS['after_tests']
    Hooks.reset()
    assert len(HOOKS['after_tests']) == 0
