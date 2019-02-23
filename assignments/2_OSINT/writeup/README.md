# Writeup 2 - OSINT

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)

OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

What is v0idcache's real name?
Elizabeth Moffet
 
Where does v0idcache work? What is the URL to their website?
1337 Bank, 1337bank.money
 
List all personal information (including social media accounts, contacts, etc) you can find about v0idcache. For each, briefly detail how you discovered them.
v0idcache has a twitter that I discovered by putting the v0idcache name through namechk.com and checking each website where the name was taken.
v0idcache has a (mostly) empty reddit account that was found in a similar way.
v0idcache's email is listed on the 1337bank site as v0idcache@protonmail.com
v0idcache is the CEO from the Netherlands of 1337 Bank. I got this information off of twitter
 
List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
142.93.136.81 - Waterland, Netherlands (Found through WHOIS) // No DNS history other than 1337bank.money and http://1337bank.money
 
List any hidden files or directories you found on this website. For full credit, list two distinct flags.
I found secret_directory by looking in the robots.txt file and it had the flag {h1ding_fil3s_in_r0bots_L0L}.
nmap also picked up a .git directory with the flag {h1d3_s3cret_glts}
 
What ports are open on the website? What services are running behind these ports? How did you discover this?
From running "nmap -v -Pn -p- 1337bank.money", I discovered the following open tcp ports:
port 22 (ssh), port 80 (http), port 1337 (looks like a custom service)
 
Which operating system is running on the server that is hosting the website? How did you discover this?
Ubuntu 4 Linux, discovered it by trying to use nc on port 22 before realizing I wasn't checking all 65535 ports with nmap.
 
BONUS: Did you find any other flags on your OSINT mission? (Up to 9 pts!)
{h1dd3n_1n_plain_5ight}
{0M3G4LUL_G3T_pWN3d_N00b}
{Ef2FlaGwJKdwt3tmJcIbBir5q}
{brut3_f0rce_m4ster}

I also found these from 
grep -r -i CMSC389R on the webserver's port 1337
home/files/AA0002.txt:CMSC389R-{1v9DrCMtpe8DcbxuMK7j6viO0}
home/files/AA0004.txt:CMSC389R-{1isN7fp9kCsNOJw6OD1DeK0xd}
home/files/AA0005.txt:CMSC389R-{4dy21Idh6EP3Ii0X5Ut27bo6s}
home/files/AA0006.txt:CMSC389R-{dcG4U5OXN9Z2YoWjKQVEF3JnO}
home/files/AA0008.txt:CMSC389R-{8EXu2TOPCz4aS93tfitDz0Nci}
home/files/AA0009.txt:CMSC389R-{S0YRxnf3jmBXSrCQ6TuFZY3yr}
home/files/AA0010.txt:CMSC389R-{prW64YPXP8RVZ1d0a3BbXhHua}
home/files/AA0011.txt:CMSC389R-{2OUqDPSXD0GxgRXuovbyWQVCx}
home/files/AA0012.txt:CMSC389R-{gUcSDsEPvg4vaoy84B53HLCVq}
home/files/AA0013.txt:CMSC389R-{Em6p1wmCnhyM2JMJMtd9Emzn8}
home/files/AA0015.txt:CMSC389R-{MO15o2YUBW2qriAK7aF8eMeuV}
home/files/AA0017.txt:CMSC389R-{sG3YJq0soKOwUinvSv9AZJquK}
home/files/AA0018.txt:CMSC389R-{LEaP7mxTDNfWOZrjQFjLQx9Xx}
home/files/AA0019.txt:CMSC389R-{r8KQ5eZ9Yl4vYgxVyflvDz3Il}
{a lot of other lines here}


### Part 2

After discovering the weird service on port 1337, I connected directly to it with nc. From there, I got an idea of how input was read by the service and how failed requests worked (the connection got dropped). Knowing these two things, I made it so the socket would get recreated everytime a password failed and I sent the username and passwords when requested by the service. The username was guessed to be v0idcache as that was the username of the CEO on multiple sites. The passwords were pulled from the wordlist available on Kali. The program goes through until it finds something other than a fail response and it then prints the password that was successful.

