import os 
import sys
import time 
from os import system
from time import sleep
import requests

#clrnumber

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

##### LOGO #####
logo = """
\033[1;96m==============================================
\033[1;96m     
\033[1;96m    ____    __  __   ____    _   _
\033[1;92m   / ___|  |  \/  | / ___|  | | | |
\033[1;96m   \___ \  | |\/| | \___ \  | |_| |
\033[1;92m    ___) | | |  | |  ___) | |  _  |
\033[1;96m   |____/  |_|  |_| |____/  |_| |_|
 
\033[1;93m     Facebook : www.facebook.com/smsh.me
\033[1;96m=============================================
"""

def hp(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)
        
system("clear")
print(logo)
('')
hp('')
print(G + " Hello!I am S M Shakib Hasan ")

print('')

hp(R + ' If you want to do the job.')
hp(G + ' And if you love your job.' )
hp(R + ' Then one day you will be successful.')
hp(C + ' Inshallah.')
hp(G +  '                  --SMSH')
print("")
hp(R + ""                   SMS BOMBING "     )
print("")
