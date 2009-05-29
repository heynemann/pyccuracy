from os import listdir
from os.path import dirname, abspath, join, split
from glob import glob

base_path = abspath(dirname(__file__))
folders = listdir(base_path)

templates_by_language = {}
for folder in folders:
    language = split(folder)[1]
    templates_by_language[language] = {}
    pattern = join(folder, "*")
    template_files = [f for f in glob(pattern)]
    for template_file in template_files:
        template_name = split(template_file)[1]
        template_text = open(template_file).read()
        templates_by_language[template_name] = template_text

class TemplateLoader(object):
    def __init__(self, language):
        self.language = language

    def load(self, template_name):
        if language not in templates_by_language:
            raise KeyError("The language %s was not found in the supported templates!" % language)
        if template_name not in templates_by_language[language]:
            raise KeyError("The template %s was not found in the supported templates for language %s!" % (template_name, language))
        return templates_by_language[language][template_name]
