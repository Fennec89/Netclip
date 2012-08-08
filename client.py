#!/usr/bin/python2
# -*- coding: utf8 -*-
from socket import *

HOST = 'localhost'
PORT = 29600
ADDR = (HOST,PORT)
BUFSIZE = 4096

cli = socket( AF_INET,SOCK_STREAM)
cli.connect((ADDR))

for i in range(1, 200):
    cli.send(str(i) + ", ")

data = cli.recv(BUFSIZE)
cli.close()

print "Recieved data: ", data

# vim: ts=4 et tw=79 cc=+1
