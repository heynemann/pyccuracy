# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
from pyccuracy.errors import ActionFailedError
from pyccuracy.languages import LanguageItem, AVAILABLE_LANGUAGES, LanguageGetter

ACTIONS = {}
LANGUAGE_DICT = dict([(l, []) for l in AVAILABLE_LANGUAGES])

class ActionRegistry(object):
    @classmethod
    def suitable_for(cls, line, language):
        for action in LANGUAGE_DICT[language]:
            match = action.can_resolve(line)
            if not match:
                translated_regex = LanguageGetter(language).get(action.regex)
                match = re.match(translated_regex, line)

            if match:
                return action, match.groups(), match.groupdict()

        # nothing found
        return None, None, None

class MetaActionBase(type):
    def __init__(cls, name, bases, attrs):
        if name not in ('ActionBase', ):
            if 'execute' not in attrs:
                raise NotImplementedError("The action %s does not implements the method execute()", name)
            if 'regex' not in attrs:
                raise NotImplementedError("The action %s does not implements the attribute regex", name)

            if not isinstance(attrs['regex'], basestring):
                regex = attrs['regex']
                raise TypeError("%s.regex attribute must be a string, got %r(%r)." % (regex.__class__, regex))

            # registering
            ACTIONS[name] = cls
            for language in AVAILABLE_LANGUAGES:
                LANGUAGE_DICT[language].append(cls)

        super(MetaActionBase, cls).__init__(name, bases, attrs)

class ActionBase(object):
    __metaclass__ = MetaActionBase
    ActionFailedError = ActionFailedError

    @classmethod
    def can_resolve(cls, string):
        return re.match(cls.regex, string)
