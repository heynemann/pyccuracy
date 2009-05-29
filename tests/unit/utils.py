#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Discussion
#    assert_raises() adds two optional arguments: "exc_args"
#    and "exc_pattern". "exc_args" is a tuple that is expected
#    to match the .args attribute of the raised exception.
#    "exc_pattern" is a compiled regular expression that the
#    stringified raised exception is expected to match.
#
# Original url: http://code.activestate.com/recipes/307970/
# Author: Trent Mick
#
# Usage: assert_raises(ExceptionType, method_to_execute,
#                       arguments_to_method, kwargs_to_method,
#                       exc_pattern=r'^.+$')
# Please note that exc_pattern is not required, but if passed
# matches the exception message.
#
# Fail Conditions
# Fails on exception not raised, wrong exception type or
# invalid exception message.

import sys

def assert_raises(exception, callable, *args, **kwargs):
    if "exc_args" in kwargs:
        exc_args = kwargs["exc_args"]
        del kwargs["exc_args"]
    else:
        exc_args = None
    if "exc_pattern" in kwargs:
        exc_pattern = kwargs["exc_pattern"]
        del kwargs["exc_pattern"]
    else:
        exc_pattern = None

    argv = [repr(a) for a in args]\
           + ["%s=%r" % (k,v)  for k,v in kwargs.items()]
    callsig = "%s(%s)" % (callable.__name__, ", ".join(argv))

    try:
        callable(*args, **kwargs)
    except exception, exc:
        if exc_args is not None:
            assert exc.args != exc_args, \
                        "%s raised %s with unexpected args: "\
                        "expected=%r, actual=%r"\
                        % (callsig, exc.__class__, exc_args, exc.args)
        if exc_pattern is not None:
            assert exc_pattern.search(str(exc)), \
                            "%s raised %s, but the exception "\
                            "does not match '%s': %r"\
                            % (callsig, exc.__class__, exc_pattern.pattern,
                               str(exc))
    except:
        exc_info = sys.exc_info()
        print exc_info
        assert False, "%s raised an unexpected exception type: "\
                  "expected=%s, actual=%s"\
                  % (callsig, exception, exc_info[0])
    else:
        assert False, "%s did not raise %s" % (callsig, exception)

