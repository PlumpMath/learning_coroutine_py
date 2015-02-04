#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A generator that follows a log file like Unix 'tail -f'.
#
# Note: To see this example work, you need to apply to
# an active server log file.  Run the program "logsim.py"
# in the background to simulate such a file.  This program
# will write entries to a file "access-log".

import time

def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open('access-log')
    for line in follow(logfile):
        print line,