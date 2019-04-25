#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = []
    passwords = []
    
    with open('hashes.txt') as fp:
        line = fp.readline()
        while line:
            hashes.append(line.rstrip())
            line = fp.readline()
    fp.close()
    with open('passwords.txt') as fp:
        line = fp.readline()
        while line:
            passwords.append(line.rstrip())
            line = fp.readline()
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            h = hashlib.sha256(c + p)
            if h.hexdigest() in hashes:
                print(p + ":" + h.hexdigest())
            # crack hashes

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
