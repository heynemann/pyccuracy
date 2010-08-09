from pmock import *
from nose.tools import raises
from time import sleep

from pyccuracy.hooks import *

@raises(NotImplementedError)
def test_construction_fails_without_implementing_execute_for_after_tests_hook():
    class DoNothing(AfterTestsHook):
        pass
    Hooks.reset()

@raises(NotImplementedError)
def test_construction_fails_without_implementing_execute_for_before_tests_hook():
    class DoNothing(BeforeTestsHook):
        pass
    Hooks.reset()

def test_will_register_after_tests_hook():
    class SomeHook(AfterTestsHook):
        def execute(self, result):
            pass

    assert SomeHook in HOOKS['after_tests']
    Hooks.reset()

def test_will_register_before_tests_hook():
    class SomeHook(BeforeTestsHook):
        def execute(self):
            pass

    assert SomeHook in HOOKS['before_tests']
    Hooks.reset()

def test_will_execute_after_tests_hook():
    mock = Mock()
    mock.expects(once()).method('a_method')
    
    class MyHook(AfterTestsHook):
        def execute(self, result):
            MyHook.mock.a_method()
    
    MyHook.mock = mock
    Hooks.execute_after_tests(None)
    mock.verify()
    Hooks.reset()

def test_will_execute_before_tests_hook():
    mock = Mock()
    mock.expects(once()).method('a_method')

    class MyHook(BeforeTestsHook):
        def execute(self):
            MyHook.mock.a_method()

    MyHook.mock = mock
    Hooks.execute_before_tests()
    mock.verify()
    Hooks.reset()

@raises(RuntimeError)
def test_user_exceptions_make_pyccuracy_raises_after_hook_error():
    class BrokenHook(AfterTestsHook):
        def execute(self, results):
            raise RuntimeError("user did stupid things")
    
    Hooks.execute_after_tests(None)
    Hooks.reset()

@raises(RuntimeError)
def test_user_exceptions_make_pyccuracy_raises_before_hook_error():
    class BrokenHook(BeforeTestsHook):
        def execute(self):
            raise RuntimeError("user did stupid things")

    Hooks.execute_before_tests()
    Hooks.reset()

def test_reset_hooks():
    Hooks.reset()
    class AHook(AfterTestsHook):
        def execute(self, results):
            pass
    class AnotherHook(BeforeTestsHook):
        def execute(self):
            pass
    assert len(HOOKS['after_tests']) == 1
    assert len(HOOKS['before_tests']) == 1
    assert AHook in HOOKS['after_tests']
    assert AnotherHook in HOOKS['before_tests']
    Hooks.reset()
    assert len(HOOKS['after_tests']) == 0
    assert len(HOOKS['before_tests']) == 0
