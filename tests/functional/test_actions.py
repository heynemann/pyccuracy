#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2009 Bernardo Heynemann <heynemann@gmail.com>
# Copyright (C) 2009 Gabriel Falcão <gabriel@nacaolivre.org>
#
# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.opensource.org/licenses/osl-3.0.php
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyccuracy import ActionRegistry, ActionBase
from pyccuracy.languages import LanguageItem
from pyccuracy.actions.core.page_actions import *

def test_get_suitable_action():
    Action, args, kw = ActionRegistry.suitable_for(u'I see "Welcome to Pyccuracy" title', 'en-us')
    assert Action, "Action cannot be None"
    assert issubclass(Action, ActionBase)
    assert isinstance(args, (list, tuple))
    assert isinstance(kw, dict)
    assert args[1] == u'Welcome to Pyccuracy'

def test_do_not_get_suitable_action():
    Action, args, kw = ActionRegistry.suitable_for(u'Blah bluh foo bar', 'en-us')
    assert Action is None
    assert args is None
    assert kw is None

def test_action_registry_suitable_for_returns_type_on_match():
    class FooTitleAction(ActionBase):
        regex = r'I see "foo" title'
        def execute(self, context, *args, **kwargs):
            pass

    Action, args, kwargs = ActionRegistry.suitable_for('I see "foo" title', 'en-us')
    assert isinstance(Action, type)

# Action-specific tests

def test_get_suitable_action_appropriately_for_page_actions_enus():
    Action, args, kw = ActionRegistry.suitable_for(u'I go to My Page', 'en-us')
    assert issubclass(Action, PageGoToAction)
    assert kw['url'] == u'My Page'
    
    Action, args, kw = ActionRegistry.suitable_for(u'I go to My Page for parameter "value"', 'en-us')
    assert issubclass(Action, PageGoToWithParametersAction)
    assert kw['url'] == u'My Page'
    assert kw['parameters'] == u'parameter "value"'

    Action, args, kw = ActionRegistry.suitable_for(u'I go to My Page of parameter "value"', 'en-us')
    assert issubclass(Action, PageGoToWithParametersAction)
    assert kw['url'] == u'My Page'
    assert kw['parameters'] == u'parameter "value"'
    
    Action, args, kw = ActionRegistry.suitable_for(u'I go to My Page with parameter1 "value1", parameter2 "value2"', 'en-us')
    assert issubclass(Action, PageGoToWithParametersAction)
    assert kw['url'] == u'My Page'
    assert kw['parameters'] == u'parameter1 "value1", parameter2 "value2"'

def test_get_suitable_action_appropriately_for_page_actions_ptbr():
    # Reset action regexes (this is necessary because pyccuracy was not built
    # to run 2 different languages in the same execution, then we do this to 
    # allow appropriate testing)
    PageGoToAction.regex = LanguageItem('page_go_to_regex')
    PageGoToWithParametersAction.regex = LanguageItem('page_go_to_with_parameters_regex')
    
    Action, args, kw = ActionRegistry.suitable_for(u'Eu navego para Uma Pagina', 'pt-br')
    assert issubclass(Action, PageGoToAction)
    assert kw['url'] == u'Uma Pagina'

    Action, args, kw = ActionRegistry.suitable_for(u'Eu navego para Pagina de Blog do usuario "nome"', 'pt-br')
    assert issubclass(Action, PageGoToWithParametersAction)
    assert kw['url'] == u'Pagina de Blog'
    assert kw['parameters'] == u'usuario "nome"'

    Action, args, kw = ActionRegistry.suitable_for(u'Eu navego para Pagina de Busca para query "palavra"', 'pt-br')
    assert issubclass(Action, PageGoToWithParametersAction)
    assert kw['url'] == u'Pagina de Busca'
    assert kw['parameters'] == u'query "palavra"'

    Action, args, kw = ActionRegistry.suitable_for(u'Eu navego para Pagina de Config com parameter1 "value1", parameter2 "value2"', 'pt-br')
    assert issubclass(Action, PageGoToWithParametersAction)
    assert kw['url'] == u'Pagina de Config'
    assert kw['parameters'] == u'parameter1 "value1", parameter2 "value2"'
