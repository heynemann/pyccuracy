from pyccuracy.colored_terminal import TerminalController

HOOKS = {'after_tests':[]}

class Hooks(object):
    @classmethod
    def execute_after_tests(cls, results):
        ctrl = TerminalController()
        hooks_feedback = ctrl.render('${CYAN}')
        
        for hook in HOOKS['after_tests']:
            hook().execute(results)
            hooks_feedback += ctrl.render('[HOOKS] AfterTestsHook "%s" executed.\n' % hook)
        
        hooks_feedback += ctrl.render('${NORMAL}')
        hooks_feedback += "\n"
        
        print hooks_feedback
    
    @classmethod
    def reset(cls):
        HOOKS['after_tests'] = []

class MetaHookBase(type):
    def __init__(cls, name, bases, attrs):
        if name not in ('AfterTestsHook', ):
            if 'execute' not in attrs:
                raise NotImplementedError("The hook %s does not implements the method execute()" % name)

            # registering
            if AfterTestsHook in bases:
                HOOKS['after_tests'].append(cls)

        super(MetaHookBase, cls).__init__(name, bases, attrs)

class AfterTestsHook(object):
    __metaclass__ = MetaHookBase
