# Writeup 6 - Forensics

Name: Oscar Bautista
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Oscar Bautista

## Assignment Writeup

### Part 1 (45 Pts)

So I took the file provided and ran it through wireshark. At first, I was confused by the immense amounts of random connections before realizing that the attacker was probably testing for open ports since the port numbers differed so much. I scrolled all the way to the bottom and then found ftp information.
I then followed the ftp data streams in order to get the file uploaded and downloaded. For information on the IP addresses, I looked it up online. For information on the jpeg, I used a metadata reader I found online for jpeg files. 

Warmup: what IP address has been attacked?

142.93.136.81

What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
- nmap is probably the source of all the noise at the start of the dump.
- Some form of web browser probably received the HTTP request at the start


What are the hackers' IP addresses, and where are they connecting from?

159.203.113.181 - Clifton, New Jersey

What port are they using to steal files on the server?

Port 20/21 (FTP)

Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,

a) What kind of file is it?

.jpeg

b) Where was this photo taken? Provide a country and city in your answer.

Punta del Esta, Uruguay

c) When was this photo taken? Provide a timestamp in your answer.

12/23/2018 @ 17:16

d) What kind of camera took this photo?

Apple iPhone 8 Back Camera

e) How high up was this photo taken? Provide an answer in meters.

4.57 meters above sea level

Which file did the attackers leave on the server?

greetz.fpff

What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is not an option.

1337bank could implement firewall rules that would only allow FTP connections from trusted IP addresses. 

### Part 2 (55 Pts)

For this, I just kind of made the parser identify the header and what the sections consisted of. Since I was only parsing this file, I wanted to identify what kind of section types 
were in this file so I could figure out what parsing capabilities to add to my parser. After identifying the section types, I went ahead and coded a way to read the section value
for the relevant section types. I couldn't quite figure out how to read the coordinates so I just converted the two 8 byte values into integers. The ASCII sections were parsed. The
PNG file was saved to a file called File0.png for further analysis. 

Looking at File0, I saw the IHDR chunk but the initial bytes weren't quite valid PNG file signatures so it was impossible to view the image. I opened up a hex editor and inserted the 
typical PNG file signature before the IHDR bytes and was able to get a picture of testudo with the flag CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}


Parse greetz.fpff, and report the following information:

When was greetz.fpff generated?

March 27th, 2019 @ 00:15:05

Who authored greetz.fpff?

fl1nch

List each section, giving us the data in it and its type.

Section 1: Section Type: SECTION_ASCII,  
 Section Length: 24  
Section Value: Hey you, keep looking :)  
Section 2: Section Type: SECTION_COORD,  
 Section Length: 16  
Section Value: 4632562459425875931,4617181167703417214  
Section 3: Section Type: SECTION_PNG,  
 Section Length: 202776  
Section Value: Value read but not processed  
Section 4: Section Type: SECTION_ASCII,  
 Section Length: 44  
Section Value: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC  
Section 5: Section Type: SECTION_ASCII,  
 Section Length: 80  
Section Value: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=  


Report at least one flag hidden in greetz.fpff. Any other flag found will count as bonus points towards the competition portion of the syllabus.

- CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R} : Reversal of section 4 above.
- CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak} : Extracted from PNG file in the .fpff file.
