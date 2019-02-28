# Writeup 3 - Operational Security and Social Engineering

Name: Oscar Bautista 
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Oscar Bautista

## Assignment Writeup

### Part 1 (40 pts)

Since most people in this day and age use paypal, I would probably attempt this in by phishing. Spoofing my email address to seem like it's coming from paypal, I would send an email as paypal requesting an update on bank information in the account. I would create a landing page that looks identical to paypal's landing page and then collect Moffet's username, password, and log her into the actual paypal website so that she wouldn't suspect anything. From there, I would hope she would update her paypal information as requested in the email.

From there, I would need to get information on what her bank is out of the paypal account and create another landing page that looks identical to her bank's. I could get her browser type from here and if it's the same as the paypal link, I would be able to identify what browser she primarily uses. From there, I would get her to log into her "bank account" and notify her that she needs to update her security questions. I would ask the questions that seem like very standard security questions for a bank (mother's maiden name, city of birth, first pet) and then ask her to confirm the answers with her pin. Then I would log her into her bank as usual. I would have the information and Moffet would hopefully be none the wiser as she believed that these emails were automated and from their legitimate respective sources. 

### Part 2 (60 pts)

Vulnerability 1: Weak password combined with universal username for the admin panel.

The fact that I was able to brute force the password using a wordlist containing common passwords means that you need to update your password to something that isn't as common and would require much more time to brute force. You can use password managers to create and store complex passwords, only needing to remember one of them. However you should make that one password more complicated and also ensure that you have two factor authentication enabled so nobody can get into your password vault even if they can crack your passwords.

Vulnerability 2: Lack of timeout or warning on brute force attempts.

The service being hosted on port 1337 needs to identify when a certain IP has attempted too many connections and failed and either alert you or lock them out of the system until someone overrides it. Many websites do this, disabling log in attempts if you fail your password too many times in a row. Even your phone should stop additional attempts at guessing a pin or pattern after 5 attempts. There's no reason you should need more than 5 attempts every minute if you know the passwords that could have been used so make sure IPs can't connect more than 5 times. 

Vulnerability 3: No passwords or security on secret directories.

The website's robots.txt file included information on a secret directory. This directory had no security whatsoever and its existence was announced by the robots.txt file so anybody could have gotten into it. Make sure that directories accessible through http that aren't meant to be accessed by anyone are secured, either through passwords or a need to have a cookie.
