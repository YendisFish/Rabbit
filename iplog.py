import os
import subprocess

try:
    ip = os.system('wget http://ipecho.net/plain -O - -q > iplog.txt')
    print(ip)
except:
    print('Linux Try Failed')
