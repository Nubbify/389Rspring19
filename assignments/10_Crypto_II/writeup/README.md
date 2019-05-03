# Crypto II Writeup

Name: Oscar Bautista
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Oscar Bautista

## Assignment Writeup

### Part 1 (70 Pts)

CMSC389R-{m3ss@g3_!n_A_b0ttl3} was the flag I got from decrypting message.txt.gpg. I just imported the key into 
gpg using "gpg --import key.asc" and then I just ran "gpg --decrypt message.txt.gpg" and it decrypted the file
using the imported key. 

### Part 2 (30 Pts)

cbc.bmp
![](cbc.bmp)

ecb.bmp
![](ecb.bmp)

1. cbc.bmp is more random and you can't tell what the original picture was at all. ecb.bmp has the colors changed up but the general shape
of the original image is still preserved.

2. Because ECB encrypts each segment independently, it means that segments that look identical will be encrypted identically. This means that 
patterns become easy to spot. CBC however, uses part of the last encrypted segment to encrypt the new segment, continuously adding noise to 
the encryption that makes it hard to identify patterns. 
