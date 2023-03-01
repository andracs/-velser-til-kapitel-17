#! /usr/bin/python3

import socket

s = socket.socket()

s.connect(("18.195.65.114", 21))

answer = s.recv(1024)

print (answer)

s.close
