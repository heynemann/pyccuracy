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

from setuptools import setup, find_packages
from pyccuracy import Version

#classifier should be changed to "Development Status :: 5 - Production/Stable" soon

setup(
    name = 'Pyccuracy',
    version = Version,
    description = "Pyccuracy is a BDD style Acceptance Testing framework",
    long_description = """Pyccuracy is a Behavior-Driven Acceptance Testing framework (more on http://www.pyccuracy.org).""",
    keywords = 'Acceptance Testing Accuracy Behavior Driven Development',
    author = 'Pyccuracy team',
    author_email = 'pyccuracy@googlegroups.com',
    url = 'http://www.pyccuracy.org',
    license = 'OSI',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Natural Language :: English',
                   'Natural Language :: Portuguese (Brazilian)',
                   'Operating System :: MacOS',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Topic :: Software Development :: Quality Assurance',
                   'Topic :: Software Development :: Testing',],
    packages = find_packages(),
    package_dir = {"pyccuracy": "pyccuracy"},
    include_package_data = True,
    package_data = {
        '': ['*.template'],
        'pyccuracy.languages.data': ['*.txt'],
        'pyccuracy.xslt': ['*.xslt'],
    },

    install_requires=[
        "selenium",
    ],

    entry_points = {
        'console_scripts': [
            'pyccuracy_console = pyccuracy.pyccuracy_console:console',
            'pyccuracy_help = pyccuracy.pyccuracy_help:console',
        ],
    },

)


