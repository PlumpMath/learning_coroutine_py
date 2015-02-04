#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A coroutine that catches the close() operation

from coroutine import coroutine

@coroutine
def grep(pattern):
    print 'Looking for %s' % pattern
    try:
        while True:
            line = (yield)
            if pattern in line:
                print line,
    except GeneratorExit:
        print 'Going away. Goodbye'

# Example use
if __name__ == '__main__':
    g = grep('python')
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
    g.close()