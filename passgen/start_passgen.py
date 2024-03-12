import concurrent.futures
from datetime import datetime
import os

dir_names = ['1_login','2_Login','3_LOGIN']
digs = '0123456789'
all_str = []
res_path = ''
workers = 1
counter = 0
total = 0

def gen_passwords(dir_name: str) -> None:
	global digs
	global all_str
	global res_path
	global counter
	global total
	res = []
	try:
		with open(f'{res_path}../rules/{dir_name}.txt', 'r') as f:
			rules = f.read().split('\n')
		while ('' in rules):
			rules.remove('')
		for rule in rules:
			for element in all_str:
				counter += 1
				print(f'Count: {counter} of {total}')
				if dir_name == '1_login':
					res.append(f'{element}{rule.replace("%p","")}')
				elif dir_name == '2_Login':
					if element.split(';')[2][0] in digs:
						continue
					res.append(f'{element.split(";")[0]};{element.split(";")[1]};{element.split(";")[2][0].swapcase()}{element.split(";")[2][1:]}{rule.replace("%p","")}')
				elif dir_name == '3_LOGIN':
					res.append(f'{element.split(";")[0]};{element.split(";")[1]};{element.split(";")[2].upper()}{rule.replace("%p","")}')
			with open(f'{res_path}{dir_name}/{rule}.txt', 'a') as f:
				f.write('\n'.join(res))
				f.write('\n')
			res = []
	except Exception as e:
		print(e)
	return

def get_input(filename: str) -> bool:
	global all_str
	global total
	try:
		with open(f'{os.getcwd()}/input/{filename}', 'r') as f:
			all_str_tmp = f.read().split('\n')
		if (len(all_str_tmp) > 0):
			all_str = all_str + all_str_tmp
			total += len(all_str_tmp)
			return True
		return False
	except Exception as e:
		print(e)
		return False

def create_dirs() -> None:
	global dir_names
	os.mkdir(res_path)
	for element in dir_names:
		os.mkdir(f'{res_path}{element}/')
	return

def create_files() -> None:
	global dir_names
	global total
	clear = ''
	rules_count = 0
	for element in dir_names:
		with open(f'{res_path}../rules/{element}.txt','r') as f:
			rules = f.read().split('\n')
		while ('' in rules):
			rules.remove('')
		rules_count += len(rules)
		for rule in rules:
			with open(f'{res_path}{element}/{rule}.txt','a') as f:
				f.write(clear)
	total *= rules_count
	print(f'Total: {total}\nRules count: {rules_count}\n')
	return

def main() -> None:
	global workers
	global res_path
	global dir_names
	global total
	time_start = datetime.now().strftime("%Y.%m.%d_%H-%M")
	cwd = os.getcwd()
	if os.name == 'posix':
		res_path = f'{cwd}/{time_start}/'
	else:
		res_path = f'{cwd}\\{time_start}\\'
	for root, dirs, files in os.walk('./input/'):
		for filename in files:
			if ('.txt' in filename):
				get_input(filename)
	if total == 0:
		print('Check input\nExit')
		return
	while('' in all_str):
		all_str.remove('')
	total = len(all_str)
	create_dirs()
	create_files()
	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
		executor.map(gen_passwords, dir_names)
	print(f'Check it out: {res_path}')

if __name__ == '__main__':
	main()