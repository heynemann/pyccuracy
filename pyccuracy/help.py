# coding: utf-8
import os
import re

CURR_DIR = os.path.dirname(__file__) or '.'

class LanguageViewer(object):
    ACTIONS = ['page', 'button', 'checkbox', 'div', 'image', 
            'link', 'radio', 'select', 'textbox', 'element', ]

    def __init__(self, language='en-us'):
        self.languages_dir = CURR_DIR + '/languages/data'
        self.language = language
        self.actions = {}
        self._set_all_actions()
    
    def _set_all_actions(self):
        language_filename = os.path.join(self.languages_dir, '%s.txt' % self.language)

        if not os.path.exists(language_filename):
            raise Exception, 'Language file not found: %s' % language_filename

        language_file = open(language_filename)

        possible_action_lines = []
        for line in language_file:
            line = line.strip()
            if not line.startswith('#') and '=' in line:
                left, right = line.split('=')
                left = left.strip()
                right = right.strip()
                splitted_left_operand = left.split('_')
                if splitted_left_operand[-1] == 'regex' and splitted_left_operand[0] in self.ACTIONS:
                    action_name = '_'.join(splitted_left_operand[:-1])
                    new_right_value = self.make_it_readable(right)
                    self.actions[action_name] = new_right_value

        language_file.close()

    def make_it_readable(self, value):
        value = value.replace('(?P<url>[\\"]([\w:/._-]+)[\\"]|([\w\s_.-]+))$', '[page|"url"]') #replace urls
        value = re.sub(r'\(\?\P\<([\w\s]*)\>\<([\w\s]*)\>\)', r'[\1|\2]', value)
        value = re.sub(r'\(\?\P\<([\w\s]*)\>\[\^\"\]\+\)', r'\1', value)
        value = re.sub(r'\(\?\P\<([\w\s]*)\>\.\+\)', r'\1', value)
        value = re.sub(r'\(\?\P\<([\w\s]*)\>\\d\+\)', r'X', value)
        value = re.sub(r'\(\?\P\<\w\>(.*)\)', r'\1', value)
        value = re.sub(r'\(\?\P\<\w*\>\\d\+\(\[\.\]\\d\+\)\?\)', '[X|X.X]', value)
        value = re.sub(r'\P\<\w*\>', '', value)
        value = value.replace('[\\"]', '"') #replace quotes
        value = value.replace('(.+)', 'blah') #replace random text
        value = value.replace('\d+', 'X').replace('(X)', 'X') #replace digits
        value = value.replace('[\\\"\\\']', '"').replace('[\\\'\\\"]', '"') #replace quotes
        value = value.replace('X([.]X)?', '[X|X.X]')
        value = value.replace('?', '').replace('$', '').replace('^', '')
        return value

    def get_actions(self, term):
        matches = {}
        for key in self.actions.keys():
            if term in key:
                matches[key] = self.actions.get(key)
            
        return matches
