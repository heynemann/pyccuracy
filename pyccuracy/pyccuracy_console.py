#!/usr/local/virtual/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'Pyccuracy==1.2.25','console_scripts','pyccuracy_console'
__requires__ = 'Pyccuracy==1.2.25'
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('Pyccuracy==1.2.25', 'console_scripts', 'pyccuracy_console')()
)
