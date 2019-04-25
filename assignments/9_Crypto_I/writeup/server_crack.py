#!/usr/bin/env python3

import hashlib
import string
import socket
import time

import hashlib
import string

def crack(passwordfilename, hashtarget):
    passwords = []
    
    with open(passwordfilename) as fp:
        line = fp.readline()
        while line:
            passwords.append(line.rstrip())
            line = fp.readline()
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            h = hashlib.sha256(c + p)
            if h.hexdigest() == hashtarget:
                return c + p + '\n'

def server_crack():
    passwords = 'passwords.txt'
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    hashtarget = data.split('\n')[2]
    time.sleep(.05)
    s.sendall(crack(passwords, hashtarget))
    time.sleep(.05)
    data = s.recv(1024)
    hashtarget = data.split('\n')[2]
    s.sendall(crack(passwords, hashtarget))
    time.sleep(.05)
    data = s.recv(1024)
    hashtarget = data.split('\n')[2]
    s.sendall(crack(passwords, hashtarget))
    time.sleep(.05)
    data = s.recv(1024)
    print data
    # parse data
    # crack 3 times

if __name__ == "__main__":
    server_crack()
