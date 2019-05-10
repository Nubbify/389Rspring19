# Crypto II Writeup

Name: Oscar Bautista
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Oscar Bautista

## Assignment Writeup

### Part 1 (40 Pts)
Got on the site, looked around to see what was there. Just an about page and a table. The table looked like it formed a get request so
I tried to see if I could do a SQL injection on what I imagined was retrieval from the exploit database. It said SQL Injection Detected, so I obfuscated some of my URL with URL encoding and changed the OR operator to || (url encoded of course) to get the URL: http://1337bank.money:5000/item?id=1%27%20%7C%7C%201=1%20--%20t
I tried to urlencode the hyphens too but those got converted back by chrome. It was good enough to get the flag though.
CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

### Part 2 (60 Pts)

1. <script> alert() </script>

2. <img src="coolpic.jpg" onerror="alert()">

3. URL: https://xss-game.appspot.com/level3/frame#1+%22'%20onerror=alert();%3E%22

4. 1');alert('test

5. 


1. I already knew this from the top of my head.

2. Had to look at the hints to remember that onerror existed. From there, just put a bogey image source and you're in.

3. This one involved looking through the code and seeing how input could be read as code. Similar feeling to SQL injection.

4. Same as above. I ran into a couple of syntax errors but the chrome console was super nice to me and told me what the script was trying to run so I could line up quotations and parenthesis.

5. 
