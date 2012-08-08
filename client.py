#!/usr/bin/python2
# -*- coding: utf8 -*-
from socket import *
import time
import sys

HOST = sys.argv[2]
PORT = 29600
ADDR = (HOST,PORT)
BUFSIZE = 4096
MESSAGE = ['0','TO THE BOARD'] #first element: 1 = recive clipboard, 0 = paste to server
MSG = ['1', str(sys.argv[1])] # second element defines how many lines to get from CB
cli = socket( AF_INET,SOCK_STREAM)
cli.connect((ADDR))

for i in range(0,4):
    MESSAGE[1] = MESSAGE[1]+str(i)
    print MESSAGE
    cli.send(repr(MESSAGE))
    time.sleep(1)
time.sleep(2)
cli.send(repr(MSG))
data = eval(cli.recv(BUFSIZE))

cli.close()

print "Recieved data: ", data

# vim: ts=4 et tw=79 cc=+1
