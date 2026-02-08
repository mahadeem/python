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


i = 0
t = datetime.datetime.now() 
v = "A"
z = "B"
u = "C"
j = "D"
port = 9000
window = Tk()
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), port))
s.listen()
client, address = s.accept()
clients = []
kfrs = []

def a():
    while True:
        try:
            
            print(f'Server is listening at .....\n')
            enCryp = client.recv(1024)
            print(enCryp)
            kfrs.append(enCryp)
            clients.append(client)  
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
