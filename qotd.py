#!/usr/bin/env python3
import socket



def qotd(server='djxmmx.net',port=17):
    s = socket.socket()
    s.connect((server,port))

    msg = bytearray()
    chunk = s.recv(32)
    while chunk:
        msg.extend(chunk)
        chunk = s.recv(32)

    return msg

if __name__ == '__main__':
    msg = qotd('time.nist.gov',port=13)
    print(msg.decode('ascii'))
