#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A concurrent echo server using coroutines

from pyos8 import *
from socket import *


def handle_client(client, addr):
    print 'Connection from', addr
    while True:
        data = yield Recv(client, 65536)
        if not data:
            break
        yield Send(client, data)
    client.close()
    print 'Client closed'

def server(port):
    print 'Server starting'
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(("", port))
    sock.listen(5)
    while True:
        client, addr = yield Accept(sock)
        yield NewTask(handle_client(client, addr))

sched = Scheduler()
sched.new(server(45000))
sched.mainloop()