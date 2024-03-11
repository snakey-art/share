import os
import runpy

static = ''

def login_gen():
	global static
	print(40*'-')
	print(f'Static dir: {static}')
	if os.path.isdir(f'{static}/logingen/'):
		print('[+] LOGINGEN work dir found')
	else:
		print(f'[-] LOGINGEN work dir not found! Check out {static}/logingen/')
		return
	if os.path.isfile(f'{static}/logingen/zones.txt'):
		print('[+] ZONES LIST found')
	else:
		print(f'[-] ZONES LIST not found! Check out {static}/logingen/zones.txt')
		return
	for root, dirs, files in os.walk(f'{static}/logingen/input/'):
		if len(files) > 0:
			print('[+] INPUT found')
		else:
			print(f'[-] INPUT not found! Check out {static}/logingen/input/')
			return
	print('[+] Start script...')
	if os.name == 'posix':
		os.chdir(f'{static}/logingen')
		os.system(f'python3 start_logingen.py')
	else:
		os.chdir(f'{static}\\logingen')
		os.system(f'python start_logingen.py')
	print('[+] Done')
	print(40*'-')

def url_login_mail_pass():
	global static
	print(40*'-')
	print(f'Static dir: {static}')
	if os.path.isdir(f'{static}/url_login/'):
		print('[+] URL_LOGIN + MAIL_PASS work dir found')
	else:
		print(f'[-] URL_LOGIN + MAIL_PASS work dir not found! Check out {static}/url_login/')
		return
	for root, dirs, files in os.walk(f'{static}/url_login/url_login/'):
		if len(files) > 0:
			print('[+] URL_LOGINS LISTS found')
		else:
			print(f'[-] URL_LOGINS LISTS not found! Check out {static}/url_login/url_login/')
			return
	for root, dirs, files in os.walk(f'{static}/url_login/mail_pass/'):
		if len(files) > 0:
			print('[+] MAIL_PASS LISTS found')
		else:
			print(f'[-] MAIL_PASS LISTS not found! Check out {static}/url_login/mail_pass/')
			return
	print('[+] Start script...')
	if os.name == 'posix':
		os.chdir(f'{static}/url_login')
		os.system(f'python3 start_url_login.py')
	else:
		os.chdir(f'{static}\\url_login')
		os.system(f'python start_url_login.py')
	print('[+] Done')
	print(40*'-')

def url_mail_pass():
	global static
	print(40*'-')
	print(f'Static dir: {static}')
	if os.path.isdir(f'{static}/url/'):
		print('[+] URL + MAIL_PASS work dir found')
	else:
		print(f'[-] URL + MAIL_PASS work dir not found! Check out {static}/url/')
		return
	for root, dirs, files in os.walk(f'{static}/url/url/'):
		if len(files) > 0:
			print('[+] URLS LISTS found')
		else:
			print(f'[-] URLS LISTS not found! Check out {static}/url/url/')
			return
	for root, dirs, files in os.walk(f'{static}/url/mail_pass/'):
		if len(files) > 0:
			print('[+] MAIL_PASS LISTS found')
		else:
			print(f'[-] MAIL_PASS LISTS not found! Check out {static}/url/mail_pass/')
			return
	print('[+] Start script...')
	if os.name == 'posix':
		os.chdir(f'{static}/url')
		os.system(f'python3 start_url.py')
	else:
		os.chdir(f'{static}\\url')
		os.system(f'python start_url.py')
	print('[+] Done')
	print(40*'-')

def main():
	global static
	static = os.getcwd()
	print(''' ______ _______ _______ _______ 
|   __ \   _   |     __|     __|
|    __/       |__     |__     |
|___|  |___|___|_______|_______|''')
	print(''' _______ _______ _______ 
|     __|    ___|    |  |
|    |  |    ___|       |
|_______|_______|__|____|''')
	while True:
		print(40*'=' + 2*'\n')
		print('1 - URL + MAIL_PASS\n2 - URL;LOGIN + MAIL_PASS\n3 - LOGIN GEN\n4 - RESERVED\n0 - EXIT')
		choise = input()
		if choise == '1':
			url_mail_pass()
		elif choise == '2':
			url_login_mail_pass()
		elif choise == '3':
			login_gen()
		elif choise == '4':
			print('RESERVED')
		elif choise == '0':
			return

if __name__ == '__main__':
	main()