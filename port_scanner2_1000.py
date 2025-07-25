#!/USR/BIN/PYTHON

# socket 

import socket

# to add colors to the open ports and closed ports

from termcolor import colored

# create an object
# socket.AF_INET- stand for ipv4 address
# socket.sock_stream - uses tcp packetsfor connection (tcp-3way handshake method used

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# it checks the specified port only for 2 seconds as default.

socket.setdefaulttimeout(2)

# host ip add and port to scan

host = "152.59.199.112"
# port = 445

# function to scan

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("port %d is closed" % (port),'red'))
        # print("port %d is closed" % (port))
    else:
        print(colored("port %d is opened" % (port),'green'))
        # print("port %d is opened" % (port))

# calling the function portscanner

for port in range(1,1001,1):
    portscanner(port)
'''
# to take input from user use raw_input() to read a input instead of using input()
# raw_input() method is for older versions of pyhon so use input method

host = input("enter host ip : ")
port = int(input("enter host port : "))

# calling the function portscanner

portscanner(port)
'''
