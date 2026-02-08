import socket
import ipaddress
import os
import io
from io import BytesIO
import base64
import time
from time import sleep
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


port = 9000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), port))


def a():
    while True:
        try:
            
            cNumber = random.randrange(1,10)
            enCryp = cNumber
            s.sendall(bytes(str(enCryp), "utf-8"))
            enCryp.close()
            l = threading.Thread(target=a)
            l.start()
        except:
            break

def b():
    while True:
        try:
            conn = sqlite3.connect('yourdbfile')
            c = conn.cursor()
            c.execute('''SELECT url, time FROM urls''')
            rows = c.fetchall()
            conn.commit()
            conn.close()
            s.sendall(bytes(str(rows),'utf-8'))
            q = threading.Thread(target=b)
            q.start()
        except:
            break
           

if __name__ == "__main__":
    a()
    b()
