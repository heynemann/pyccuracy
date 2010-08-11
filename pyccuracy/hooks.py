from pyccuracy.colored_terminal import TerminalController

HOOKS = {'after_tests':[], 'before_tests':[]}

class Hooks(object):
    
    #TODO: refactor - merge after & before methods
    @classmethod
    def execute_after_tests(cls, results):
        if len(HOOKS['after_tests']) > 0:
            ctrl = TerminalController()
            hooks_feedback = ctrl.render('${CYAN}')

            for hook in HOOKS['after_tests']:
                hook().execute(results)
                hooks_feedback += ctrl.render('[HOOKS] AfterTestsHook "%s" executed.\n' % hook)

            hooks_feedback += ctrl.render('${NORMAL}')
            hooks_feedback += "\n"

            print hooks_feedback

    @classmethod
    def execute_before_tests(cls):
        if len(HOOKS['before_tests']) > 0:
            ctrl = TerminalController()
            hooks_feedback = ctrl.render('${CYAN}')

            for hook in HOOKS['before_tests']:
                hook().execute()
                hooks_feedback += ctrl.render('[HOOKS] BeforeTestsHook "%s" executed.\n' % hook)

            hooks_feedback += ctrl.render('${NORMAL}')
            hooks_feedback += "\n"

            print hooks_feedback
    
    @classmethod
    def reset(cls):
        HOOKS['after_tests'] = []
        HOOKS['before_tests'] = []

class MetaHookBase(type):
    def __init__(cls, name, bases, attrs):
        if name not in ('AfterTestsHook', 'BeforeTestsHook' ):
            if 'execute' not in attrs:
                raise NotImplementedError("The hook %s does not implement the method execute()" % name)

            # registering
            if AfterTestsHook in bases:
                HOOKS['after_tests'].append(cls)
            
            if BeforeTestsHook in bases:
                HOOKS['before_tests'].append(cls)

        super(MetaHookBase, cls).__init__(name, bases, attrs)

class AfterTestsHook(object):
    __metaclass__ = MetaHookBase

class BeforeTestsHook(object):
    __metaclass__ = MetaHookBase