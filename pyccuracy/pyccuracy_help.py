#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse
import sys

from help import LanguageViewer

def show_terms(term, language):
    viewer = LanguageViewer(language=language)
    actions = viewer.get_actions(term)
    print '\n----- Found %d results for "%s" -----\n' % (len(actions), term if term is not '' else '*')
    for name, value in actions.iteritems():
        print '%-35s = %s' % (name, value)
    print '\n----- Found %d results for "%s" -----\n' % (len(actions), term if term is not '' else '*')

def main(arguments=sys.argv[1:]):
    info = '''
--------------------------------------------------------------------------------------
Use %prog to get quick assistance on the expressions available for Pyccuracy.
--------------------------------------------------------------------------------------

Examples:

$ %prog --language en-us
    --> Shows all actions for english language.

$ %prog --term select
    --> Shows actions in english language for "select" elements.

$ %prog --language pt-br --term textboxes
    --> Shows actions in portuguese language for "textbox" elements.'''
    parser = optparse.OptionParser(info)

    parser.add_option('-t', '--term', dest='term', default='', help='Terms to search. It looks for terms that contains the informed words. [default: "%default"]')
    parser.add_option('-l', '--language', dest='language', default='en-us', help='Language to search for terms. [default: %default]')

    options, args = parser.parse_args()

    show_terms(options.term, options.language)

def console():
    sys.exit(main(sys.argv[1:]))

if __name__ == "__main__":
    console()