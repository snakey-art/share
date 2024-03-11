import concurrent.futures
from datetime import datetime
import os

res_path = ''
urls = []
mail_pass = []
workers = 8
counter = 0
total = 0

def delete_conc_files() -> None:
	os.remove(f'{res_path}conc_mail_pass.txt')
	os.remove(f'{res_path}conc_url.txt')

def save_result(res: list) -> None:
	global res_path
	res_s = '\n'.join(res)
	with open(f'{res_path}result.txt', 'a') as f:
		f.write(res_s)
		f.write('\n')

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
		for root, dirs, files in os.walk('./url_login/'):
			for filename in files:
				if ('.txt' in filename):
					with open(f'./url_login/{filename}', 'r') as f:
						data = f.read()
						fconc.write(data)
						fconc.write('\n')
	with open(f'{res_path}conc_url.txt', 'r') as f:
		data = f.read().split('\n')
		urls = urls + data
	while '' in urls:
		urls.remove('')
	total = len(urls)
	return total

def create_conc_files() -> None:
	global res_path
	clear = ''
	with open(f'{res_path}conc_mail_pass.txt', 'a') as f:
		f.write(clear)
	with open(f'{res_path}conc_url.txt', 'a') as f:
		f.write(clear)

def create_files(time_start: str) -> None:
	global res_path
	clear = ''
	with open(f'{res_path}result.txt','a') as f:
		f.write(clear)
	return

def url_handler(url: str) -> None:
	global mail_pass
	global counter
	global total
	if url == '':
		counter += 1
		print(f'Count: {counter} of {total}')
		return
	clean_url = url.lower()
	if ';' in clean_url:
		clean_url = clean_url.split(';')[0]
	if '://www.' in clean_url:
		clean_url = clean_url.split('://www.')[1]
	if '://' in clean_url:
		clean_url = clean_url.split('://')[1]
	if ':' in clean_url:
		clean_url = clean_url.split(':')[0]
	found = []
	for element in mail_pass:
		if clean_url in element.lower():
			found.append(element.split(':')[1])
	if len(found) == 0:
		counter += 1
		print(f'Count: {counter} of {total}')
		return
	res = []
	for element in found:
		res.append(f'{url};{element}')
	save_result(res)
	counter += 1
	print(f'Count: {counter} of {total}')
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
		print('Check url_login directory\nExit')
	create_files(time_start)
	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
		executor.map(url_handler, urls)
	delete_conc_files()

if __name__ == '__main__':
	main()