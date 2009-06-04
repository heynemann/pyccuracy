#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import time
from colored_terminal import ProgressBar

def main():
    pg = ProgressBar("Test Progress")
    pg.update(0.25, "Weird")
    time.sleep(2)
    pg.update(0.50, "Very Weird")
    time.sleep(2)
    pg.update(0.75, "A lot Weirder")
    time.sleep(2)
    pg.update(1.00, "Gabriel")

if __name__ == '__main__':
    sys.exit(main())


