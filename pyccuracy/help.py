# coding: utf-8
import os
import re

CURR_DIR = os.path.dirname(__file__) or '.'

class LanguageViewer(object):
    ACTIONS = ['page', 'button', 'checkbox',
               'div', 'image', 'link',
               'radio', 'select', 'textbox',]
    PT_BR_ACTIONS = {'page' : 'página',
                     'button': 'botão',
                     'checkbox': 'checkbox',
                     'div': 'div',
                     'image': 'imagem',
                     'radio': 'radio',
                     'select': 'select',
                     'link': 'link',
                     'textbox': 'caixa de texto',}
    EN_US_ACTIONS = {'page': 'page',
                     'button': 'button',
                     'checkbox': 'checkbox',
                     'div': 'div',
                     'image': 'image',
                     'radio': 'radio',
                     'select': 'select',
                     'link': 'link',
                     'textbox': 'textbox',}
    ACTIONS_TRANSLATIONS = {'pt-br' : PT_BR_ACTIONS,
                            'en-us' : EN_US_ACTIONS,}

    def __init__(self, languages_dir=CURR_DIR+'/languages/data', language='en-us'):
        self.languages_dir = languages_dir
        self.language = language
        self.actions = {}
        self._set_all_actions()

    def _get_some_translated(self, action_type):
        if self.language == 'pt-br':
            if action_type in ['page', 'image', 'textbox',
                               'checkbox', 'select']:
                return 'alguma'
            return 'algum'
        elif self.language == 'en-us':
            return 'some'

    def _get_action_translated(self, action_type):
        return self.ACTIONS_TRANSLATIONS[self.language][action_type]

    def _set_all_actions(self):
        language_filename = os.path.join(self.languages_dir,
                                        '%s.txt' % self.language)
        if not os.path.exists(language_filename):
            raise Exception, 'There is no %s' % language_filename

        language_file = open(language_filename)

        possible_action_lines = []
        for line in language_file:
            line = line.strip()
            if not line.startswith('#') and '=' in line:
                left, right = line.split('=')
                left = left.strip()
                right = right.strip()
                splitted_left_operand = left.split('_')
                if splitted_left_operand[-1] == 'regex' and\
                   splitted_left_operand[0] in self.ACTIONS:
                    action_name = '_'.join(splitted_left_operand[:-1])
                    new_right_value = self._make_it_readable(splitted_left_operand[0], right)
                    self.actions[action_name] = new_right_value
        language_file.close()
        
    def _remove_anchors(self, value):
        return value.replace('$', '').replace('^', '')

    def _replace_quotes(self, value):
        return value.replace('[\\"]', '"')

    def _replace_digits(self, value):
        return value.replace('\d+', 'X').replace('(X)', 'X')

    def _make_it_readable(self, action_type, value):
        new_value = self._remove_anchors(value)
        new_value = self._replace_quotes(new_value)
        new_value = self._replace_digits(new_value)
        
                         
        action_word = self._get_action_translated(action_type)
        some_word = self._get_some_translated(action_type)
        replacement = '%s %s' % (some_word, action_word)
        if action_type == 'page':
            new_value = new_value.replace('("([\\w:/.]+)"|([\\w\\s]+))',
                                          '"%s"'%replacement)
        new_value = new_value.replace('(.+)', replacement)
        return new_value

    def get_actions(self, action):
        matches = {}
        for key in self.actions.keys():
            if action in key:
                matches[key] = self.actions.get(key)
            
        return matches
