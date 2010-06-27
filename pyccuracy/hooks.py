HOOKS = {'after_tests':[]}

class Hooks(object):
    @classmethod
    def execute_after_tests(cls, results):
        for hook in HOOKS['after_tests']:
            try:
                hook().execute(results)
            except Exception, e:
                raise HookError(e)
    
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

class HookError(Exception):
    def __init__(self, origin):
        self.origin = origin

    def __str__(self):
        return unicode(self)
    
    def __unicode__(self):
        return "HookError: %s" % (self.origin)
