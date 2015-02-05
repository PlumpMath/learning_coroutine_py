#!/usr/bin/env python
# -*- coding: utf-8 -*-

# An example showing how to push SAX events into a coroutine target

import xml.sax


class EventHandler(xml.sax.ContentHandler):
    def __init__(self, target):
        self.target = target

    def startElement(self, name, attrs):
        self.target.send(('start', (name, attrs._attrs)))

    def endElement(self, name):
        self.target.send(('end', name))

    def characters(self, text):
        self.target.send(('text', text))

# Example use
if __name__ == '__main__':
    from coroutine import coroutine

    @coroutine
    def printer():
        while True:
            event = (yield)
            print event

    xml.sax.parse('allroutes.xml',
                  EventHandler(printer()))