#!/usr/local/virtual/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'Pyccuracy==1.2.25','console_scripts','pyccuracy_console'

from pyccuracy import Version
__requires__ = 'Pyccuracy==%s' % Version
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('Pyccuracy==%s' % Version, 'console_scripts', 'pyccuracy_console')()
)
