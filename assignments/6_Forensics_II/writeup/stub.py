#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

filenum = 0

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

def hextostring(hexcode):
    return bytearray.fromhex(hexcode.lstrip("0x")).decode("utf-8")

def get_section_type(code):
    switcher = {
        1: "SECTION_ASCII",
        2: "SECTION_UTF8",
        3: "SECTION_WORDS",
        4: "SECTION_DWORDS",
        5: "SECTION_DOUBLES",
        6: "SECTION_COORD",
        7: "SECTION_REFERENCE",
        8: "SECTION_PNG",
        9: "SECTION_GIF87",
        10: "SECTION_GIF89",
    }
    return switcher.get(code, "SECTION_UNKNOWN")

def read_value(type, len, data):
    if (type == 1):
        return data.decode()
    if (type == 2):
        return data.decode('utf-8')
    if (type == 3):
        if (slen % 4 != 0):
            bork("SECTION_WORDS corrupted")
        ret = []    
        for i in range(slen/4):
            ret.append(data[i*4:(i+1)*4])
        return ",".join(str(x) for x in ret)
    if (type == 6):
        if (slen != 16):
            bork("SECTION_COORD corrupted")
        latitude, longitude = struct.unpack("QQ", data[0:16])
        return str(latitude) + "," + str(longitude)
    if (type == 8):
        global filenum
        f = open("File" + str(filenum) + ".png", "wb")
        f.write(data)
        f.close()
        filenum += 1
        return "Value saved to File" + str(filenum-1) + ".png"
    return "Value read but not processed"


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1
HEADER_SIZE = 24

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp = struct.unpack("<LLL", data[0:12])
author = struct.unpack(">Q", data[12:20])
sections = struct.unpack("<L", data[20:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

if sections[0] <= 0:
    bork("No sections!")

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S"))
print("AUTHOR: %s" % hextostring(hex(author[0]))) 
print("SECTION COUNT: %d" % int(sections[0]))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

offset = HEADER_SIZE

for i in range(int(sections[0])):
    size = 8
    stype, slen = struct.unpack("<LL", data[offset:offset+size])
    offset += size

    print("Section %d: Section Type: %s, \n Section Length: %d" % (i+1, get_section_type(stype), int(slen)))
    if(slen > 0): 
        sval = data[offset:offset+slen]
        offset += slen
    print("Section Value: %s" % read_value(stype, slen, sval))

