#! /usr/bin/python3

import socket

s = socket.socket()

s.connect(("18.195.65.114", 22))

answer = s.recv(1024)

print (answer)

s.close
