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

import codecs
from glob import glob
from os import listdir
from os.path import dirname, abspath, join, split

base_path = abspath(dirname(__file__))
folders = listdir(base_path)

templates_by_language = {}

for folder in folders:
    language = split(folder)[1]
    if language.startswith("__"):
        continue

    templates_by_language[language] = {}
    pattern = join(base_path, folder, "*.template")

    for template_file in [f for f in glob(pattern)]:
        template_file_name = split(template_file)[1]
        template_name = template_file_name.split('.')[0]
        template_text = codecs.open(template_file, 'r', 'utf-8').read()
        templates_by_language[language][template_name] = template_text

class TemplateLoader(object):
    def __init__(self, language):
        self.language = language

    def load(self, template_name):
        if self.language not in templates_by_language:
            raise KeyError("The language %s was not found in the supported templates!" % self.language)

        if template_name not in templates_by_language[self.language]:
            raise KeyError("The template %s was not found in the supported templates for language %s!" % (template_name, self.language))

        return templates_by_language[self.language][template_name]
