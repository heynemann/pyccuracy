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

'''<!-- automatic table of contents for H1 and H2 items -->
<script src="http://gist.github.com/raw/391639/24a166b60b6e468ecd5b1f0d811032e78e34b65c/github_toc.js" type="text/javascript"></script>

h1. Pyccuracy Built-In Actions

Pyccuracy comes with a set of actions that allow the user to control the browser in the most usual ways, like clicking a link or checking if a textbox contains a given text.

If you want to create your own actions you can learn more about it at the "[[Creating custom Actions]]" page.

Pyccuracy's actions are divided in categories according to the element they relate to: element, checkbox, image, link, page, radio, select and textbox.

If you are not sure about the action you are looking for, we *always* advise you to look the Element actions, because that's where most of the fun is.'''

from os.path import dirname, abspath, join, split
from glob import glob
import codecs
import sys

base_path = abspath(dirname(__file__))
pattern = join(base_path, "*.py")
__all__ = [split(x)[1][:-3] for x in glob(pattern)]

def generate_textile_docs():
    # loading modules only here when they are needed
    from pyccuracy.actions import core as core_actions, ActionBase, MetaActionBase
    from pyccuracy.languages import LanguageGetter
    from pyccuracy.help import LanguageViewer
    
    # fixing print in non-utf8 terminals
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

    viewer = LanguageViewer("en-us")
    language_enus = LanguageGetter("en-us")
    language_ptbr = LanguageGetter("pt-br")
    
    # documentation intro
    print __doc__
    print
    
    custom_action_modules = [module for module in core_actions.__dict__.values() if str(type(module)) == "<type 'module'>" and "_actions" in str(module.__name__)]
    for module in custom_action_modules:
        print "h1. %s" % module.__name__.replace('pyccuracy.actions.core.', '').replace('_', ' ').capitalize()
        print
        if module.__doc__:
            print module.__doc__
            print
    
        module_actions = [action for action in module.__dict__.values() if type(action) == MetaActionBase and action != ActionBase]
        for action in module_actions:
            print "h2. %s" % viewer.make_it_readable(language_enus.get(action.regex)).replace("(And )", "")
            print
            if action.__doc__:
                print action.__doc__
                print
            print "h3. Syntax"
            print
            print "<pre><code># en-us\n%s\n \n# pt-br\n%s</code></pre>" % (viewer.make_it_readable(language_enus.get(action.regex)), viewer.make_it_readable(language_ptbr.get(action.regex)))
            print
            print "h3. Regex"    
            print
            print "<pre><code># en-us\n%s\n \n# pt-br\n%s</code></pre>" % (language_enus.get(action.regex), language_ptbr.get(action.regex))
            print
    
if __name__ == "__main__":
    generate_textile_docs()
    