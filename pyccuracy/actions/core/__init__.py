#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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

from os.path import dirname, abspath, join, split
from glob import glob

base_path = abspath(dirname(__file__))
pattern = join(base_path, "*.py")
__all__ = [split(x)[1][:-3] for x in glob(pattern)]

def generate_textile_docs_en_us():
    from pyccuracy.actions import core as core_actions, ActionBase, MetaActionBase
    from pyccuracy.languages import LanguageGetter
    from pyccuracy.help import LanguageViewer

    viewer = LanguageViewer("en-us")
    language = LanguageGetter("en-us")
    
    for module in [module for module in core_actions.__dict__.values() if str(type(module)) == "<type 'module'>" and "_actions" in str(module.__name__)]:
        print "h1. %s" % module.__name__.replace('pyccuracy.actions.core.', '').replace('_', ' ').capitalize()
        print
        
        for action in [action for action in module.__dict__.values() if type(action) == MetaActionBase and action != ActionBase]:
            print "h2. %s" % viewer.make_it_readable(language.get(action.regex)).replace("(And )", "")
            print
            print "*Regex:* <pre><code>%s</code></pre>" % language.get(action.regex)
            print
            
            if action.__doc__:
                print action.__doc__
            else:
                print "__No documentation for this action yet.__"
            
            print
    
if __name__ == "__main__":
    generate_textile_docs_en_us()
    