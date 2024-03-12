import concurrent.futures
from datetime import datetime
import os

res_path = ''
urls = []
mail_pass = []
workers = 1
counter = 0
total = 0

def delete_conc_files() -> None:
	os.remove(f'{res_path}conc_mail_pass.txt')
	os.remove(f'{res_path}conc_url.txt')

def save_result(res_ll: list, res_lp: list, res_pp: list) -> None:
	global res_path
	res_ll_s = '\n'.join(res_ll)
	res_lp_s = '\n'.join(res_lp)
	res_pp_s = '\n'.join(res_pp)
	for root, dirs, files in os.walk(res_path):
			for filename in files:
				if ('login_login_' in filename):
					with open(f'{res_path}{filename}', 'a') as f:
						f.write(res_ll_s)
						f.write('\n')
				if ('login_pass_' in filename):
					with open(f'{res_path}{filename}', 'a') as f:
						f.write(res_lp_s)
						f.write('\n')
				if ('pass_pass_' in filename):
					with open(f'{res_path}{filename}', 'a') as f:
						f.write(res_pp_s)
						f.write('\n')

def url_handler(url: str) -> None:
	global mail_pass
	global counter
	global total
	clean_url = url.lower()
	if '://www.' in clean_url:
		clean_url = clean_url.split('://www.')[1]
	if '://' in clean_url:
		clean_url = clean_url.split('://')[1]
	if ':' in clean_url:
		clean_url = clean_url.split(':')[0]
	found = []
	for element in mail_pass:
		if clean_url in element.lower():
			found.append(element)
	if len(found) == 0:
		counter += 1
		print(f'Count: {counter} of {total}')
		return
	res_ll = []
	res_lp = []
	res_pp = []
	logins = []
	passwords = []
	for element in found:
		logins.append(element.split('@')[0])
		passwords.append(element.split(':')[1])
		if '.' in element.split('@')[0]:
			logins.append(element.split('@')[0].replace('.',''))
			logins.append(element.split('@')[0].replace('.','')[:8])
	logins = list(set(logins))
	passwords = list(set(passwords))
	for l in logins:
		for p in passwords:
			res_ll.append(f'{url.lower()};{l.lower()};{l.lower()}')
			res_lp.append(f'{url.lower()};{l.lower()};{p}')
			res_pp.append(f'{url.lower()};{p};{p}')
	res_ll = list(set(res_ll))
	res_lp = list(set(res_lp))
	res_pp = list(set(res_pp))
	save_result(res_ll, res_lp, res_pp)
	counter += 1
	print(f'Count: {counter} of {total}')
	return

def create_conc_files() -> None:
	global res_path
	clear = ''
	with open(f'{res_path}conc_mail_pass.txt', 'a') as f:
		f.write(clear)
	with open(f'{res_path}conc_url.txt', 'a') as f:
		f.write(clear)

def conc_mail_pass() -> int:
	global mail_pass
	with open(f'{res_path}conc_mail_pass.txt', 'w') as fconc:
		for root, dirs, files in os.walk('./mail_pass/'):
			for filename in files:
				if ('.txt' in filename):
					with open(f'./mail_pass/{filename}', 'r') as f:
						data = f.read()
						fconc.write(data)
						fconc.write('\n')
	with open(f'{res_path}conc_mail_pass.txt', 'r') as f:
		data = f.read().split('\n')
		mail_pass = mail_pass + data
	if '' in mail_pass:
		mail_pass.remove('')
	return len(mail_pass)

def conc_url() -> int:
	global urls
	global total
	with open(f'{res_path}conc_url.txt', 'w') as fconc:
		for root, dirs, files in os.walk('./url/'):
			for filename in files:
				if ('.txt' in filename):
					with open(f'./url/{filename}', 'r') as f:
						data = f.read()
						fconc.write(data)
						fconc.write('\n')
	with open(f'{res_path}conc_url.txt', 'r') as f:
		data = f.read().split('\n')
		urls = urls + data
	if '' in urls:
		urls.remove('')
	total = len(urls)
	return total

def create_files(time_start: str) -> None:
	global res_path
	clear = ''
	with open(f'{res_path}login_login_{time_start}.txt','a') as f:
		f.write(clear)
	with open(f'{res_path}login_pass_{time_start}.txt','a') as f:
		f.write(clear)
	with open(f'{res_path}pass_pass_{time_start}.txt','a') as f:
		f.write(clear)
	return

def main() -> None:
	global res_path
	global workers
	global urls
	time_start = datetime.now().strftime("%Y.%m.%d_%H-%M")
	cwd = os.getcwd()
	if os.name == 'posix':
		res_path = f'{cwd}/{time_start}/'
	else:
		res_path = f'{cwd}\\{time_start}\\'
	os.mkdir(res_path)
	create_conc_files()
	if conc_mail_pass() == 0:
		print('Check mail_pass directory\nExit')
	if conc_url() == 0:
		print('Check url directory\nExit')
	create_files(time_start)
	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
		executor.map(url_handler, urls)
	delete_conc_files()
	print(f'Check it out: {res_path}')

if __name__ == '__main__':
	main()