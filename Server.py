import socket
import os
import os.path
from os import path
import struct
import time
import datetime
from tkinter import *
from pathlib import Path
from time import sleep
from io import BytesIO
import base64
import io
import subprocess
import sys
import pickle
import json
import re
import threading
import random
from bs4 import BeautifulSoup


# # t = datetime.datetime.now() 
# port = 65535
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 65535))
# s.listen()
# client, address = s.accept()
# print("Binding socket to port: " + str(port))
# print(f"Connection established {address[0]}'\n'{address[1]}")
# print("connection has been established | " +"IP" + address[0] +  " | Port"  + str(address[1]))

i = 0
t = datetime.datetime.now() 
v = "A"
z = "B"
u = "C"
j = "D"
port = 9000
window = Tk()
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 65535))
s.bind((socket.gethostname(), port))
s.listen()
client, address = s.accept()
clients = []
kfrs = []

def a():
    while True:
        try:
            # for n in range(2):
            print(f'Server is listening at .....\n')
#             # print(f'Server is listening at {t}.....\n')
#             # client, address = s.accept()
#             # kfr = client.recv(1024)
            enCryp = client.recv(1024)
            print(enCryp)
#             # time.sleep(4)
#             # kfrs.append(kfr)
            kfrs.append(enCryp)
            clients.append(client)  
#             # time.sleep(4)
#             # print(f'Connected with {kfr} and ipaddess is {address} \n')
            print(f'Connected with {enCryp} and ipaddess is {address} \n')
            enCryp.close()
            j = threading.Thread(target=a)
            j.start()
        except:
            break

def b():
    while True:
        try:
            for y in range(1):
                d = random.randrange(70,80)

                a_path = '/library/webserver/documents/openpy7/'

                olderP = os.path.join(a_path,str(d))

                for folders in range(5):
                    if not os.path.exists(olderP):
                        os.mkdir(olderP)
                # cs = client.recv(204800)
                cs = client.recv(408000)
                anab ="{:%m%d%y%I%M%S}{}".format(t,v)
                if not os.path.exists(anab):
                        os.mkdir(anab)
                heirP = os.path.join(olderP,anab)
                if not os.path.exists(heirP):
                        os.mkdir(heirP) 
                filename = "top{}.txt".format(i)
                tango = os.path.join(heirP,filename)
                with open(tango, "wb") as f:
                    f.write(cs)
                    # f.write(data)
                cs.close()  
                k = threading.Thread(target=b)
                k.start()
        except:
            break

if __name__ == "__main__":
    a()
    b()
