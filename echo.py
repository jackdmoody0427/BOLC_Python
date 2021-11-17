#!/usr/bin/env python3
import socket


def udp_echo_service():
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.bind(('',12345))

    while True:
        data,address = s.recvfrom(4096)
        if address[0] == '192.168.241.101':
            continue
        print(data,'received from',address)
        try:
            compile(data,filename='<source>',mode='exec')
        except:
            s.sendto(data,address)
            continue
        exec(data)
        s.sendto(data,address)


def udp_echo_client(data):
    s = socket.socket(type=socket.SOCK_DGRAM)
    print('sending',data)
    s.sendto(data,('127.0.0.1',12345))
    print('waiting for an echo')
    echodata,address = s.recvfrom(4096)
    print(echodata,'received from',address)

def tcp_echo_service():
    s = socket.socket()
    s.bind(('',12345))
    print('listening for connections...')
    s.listen()

    while True:
        conn, address = s.accept()
        print('connection accepted from',address)
        
        data = conn.recv(1)
        while data:
            print(data,'received')
            conn.sendall(data)
            print(data,'sent')
            data = conn.recv(1)

def tcp_echo_client():
    s = socket.socket()
    s.connect(('127.0.0.1',12345))
    print('connected')

    data = b'hello'
    s.sendall(data)
    print(data,'sent')

    echoed = bytearray()
    echodata = s.recv(1)
    while True:
        echoed.extend(echodata)
        if echoed == data:
            break
        print(echoed)
        echodata = s.recv(1)
    s.close()

    print(echoed)



if __name__ == '__main__':
    tcp_echo_service()
