#!/usr/bin/python2
# -*- coding: utf8 -*-
from socket import *

HOST = ''
PORT = 29600
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket( AF_INET,SOCK_STREAM)

serv.bind((ADDR))
serv.listen(1)
print "listening..."

conn,addr = serv.accept()
print "...connected: ", addr
while 1:
    data = conn.recv(BUFSIZE)
    if not data: break
    print "recived data: ", data
    conn.send(data)
conn.close()

# vim: ts=4 et tw=79 cc=+1
