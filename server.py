#!/usr/bin/python2
# -*- coding: utf8 -*-
from socket import *

HOST = ''
PORT = 29600
ADDR = (HOST,PORT)
BUFSIZE = 4096

clipboard = []

serv = socket( AF_INET,SOCK_STREAM)
serv.bind((ADDR))
serv.listen(1)

print "listening..."

conn,addr = serv.accept()
print "...connected: ", addr

while 1:
    data = conn.recv(BUFSIZE)

    if not data: break
    original_data = eval(data)

    if original_data[0] == "0":
        clipboard.append(original_data[1])
        print "Current clipboard: ", clipboard
    elif original_data[0] == "1":
        print original_data[1]
        index = original_data[1]
        print clipboard[:int(index)]
        print "sending data..."

        conn.send(repr(clipboard[:int(index)]))

conn.close()

# vim: ts=4 et tw=79 cc=+1
