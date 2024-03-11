import concurrent.futures
from datetime import datetime
import os

domains = []
zones = []
res_path = ''
workers = 8
counter = 0
total = 0


def get_zones() -> bool:
	global zones
	try:
		with open('zones.txt', 'r') as f:
			zones = f.read().split('\n')
		if len(zones) == 0:
			return False
		return True
	except:
		return False

def get_input(filename: str) -> bool:
	global domains
	global counter
	global total
	try:
		with open(f'{os.getcwd()}/input/{filename}', 'r') as f:
			domains_tmp = f.read().split('\n')
		if (len(domains_tmp) > 0):
			domains = domains + domains_tmp
			total += len(domains_tmp)
			return True
		return False
	except Exception as e:
		print(e)
		return False

def create_files() -> None:
	clear = ''
	with open(f'{res_path}big.txt','a') as f:
		f.write(clear)
	with open(f'{res_path}8.txt','a') as f:
		f.write(clear)
	with open(f'{res_path}7.txt','a') as f:
		f.write(clear)
	with open(f'{res_path}6.txt','a') as f:
		f.write(clear)
	with open(f'{res_path}5.txt','a') as f:
		f.write(clear)
	with open(f'{res_path}4.txt','a') as f:
		f.write(clear)
	return

def save_result(domain: str, res: list) -> None:
	global counter
	global total
	resset = list(set(res))
	#print(resset)
	#print()
	global res_path
	result_big = ''
	result_8 = ''
	result_7 = ''
	result_6 = ''
	result_5 = ''
	result_4 = ''
	for element in resset:
		if len(element) < 4:
			continue
		if len(element) == 4:
			result_4 += f'{domain.lower()};{element}\n'
		elif len(element) == 5:
			result_5 += f'{domain.lower()};{element}\n'
		elif len(element) == 6:
			result_6 += f'{domain.lower()};{element}\n'
		elif len(element) == 7:
			result_7 += f'{domain.lower()};{element}\n'
		elif len(element) == 8:
			result_8 += f'{domain.lower()};{element}\n'
		else:
			result_big += f'{domain.lower()};{element}\n'
	if len(result_big) > 0:
		with open(f'{res_path}big.txt','a') as f:
			f.write(result_big)
	if len(result_8) > 0:
		with open(f'{res_path}8.txt','a') as f:
			f.write(result_8)
	if len(result_7) > 0:
		with open(f'{res_path}7.txt','a') as f:
			f.write(result_7)
	if len(result_6) > 0:
		with open(f'{res_path}6.txt','a') as f:
			f.write(result_6)
	if len(result_5) > 0:
		with open(f'{res_path}5.txt','a') as f:
			f.write(result_5)
	if len(result_4) > 0:
		with open(f'{res_path}4.txt','a') as f:
			f.write(result_4)
	counter += 1
	print(f'Count: {counter} of {total}')
	return

def clean_results() -> None:
	with open(f'{res_path}big.txt','r') as f:
		data = f.read().split('\n')
		data = list(set(data))
		towrite = ''
		for element in data:
			if len(element) == 0:
				continue
			else:
				towrite += f'{element}\n'
	with open(f'{res_path}big.txt','w') as f:
		f.write(towrite)
	with open(f'{res_path}8.txt','r') as f:
		data = f.read().split('\n')
		data = list(set(data))
		towrite = ''
		for element in data:
			if len(element) == 0:
				continue
			else:
				towrite += f'{element}\n'
	with open(f'{res_path}8.txt','w') as f:
		f.write(towrite)
	with open(f'{res_path}7.txt','r') as f:
		data = f.read().split('\n')
		data = list(set(data))
		towrite = ''
		for element in data:
			if len(element) == 0:
				continue
			else:
				towrite += f'{element}\n'
	with open(f'{res_path}7.txt','w') as f:
		f.write(towrite)
	with open(f'{res_path}6.txt','r') as f:
		data = f.read().split('\n')
		data = list(set(data))
		towrite = ''
		for element in data:
			if len(element) == 0:
				continue
			else:
				towrite += f'{element}\n'
	with open(f'{res_path}6.txt','w') as f:
		f.write(towrite)
	with open(f'{res_path}5.txt','r') as f:
		data = f.read().split('\n')
		data = list(set(data))
		towrite = ''
		for element in data:
			if len(element) == 0:
				continue
			else:
				towrite += f'{element}\n'
	with open(f'{res_path}5.txt','w') as f:
		f.write(towrite)
	with open(f'{res_path}4.txt','r') as f:
		data = f.read().split('\n')
		data = list(set(data))
		towrite = ''
		for element in data:
			if len(element) == 0:
				continue
			else:
				towrite += f'{element}\n'
	with open(f'{res_path}4.txt','w') as f:
		f.write(towrite)
	return

def domain_splitter(domain: str) -> [str, str, str, str]:
	global zones
	splitted_domain = domain.split('.')
	www = ''
	subdom = ''
	dom = ''
	zone = ''
	for i in range(len(splitted_domain)):
		if splitted_domain[len(splitted_domain)-i-1] == 'www':
			www = 'www'
			break
		if splitted_domain[len(splitted_domain)-i-1] in zones:
			zone = '.' + splitted_domain[len(splitted_domain)-i-1] + zone
			continue
		if not dom:
			dom = splitted_domain[len(splitted_domain)-i-1]
			continue
		if not subdom:
			subdom = splitted_domain[len(splitted_domain)-i-1]
	return www, subdom, dom, zone

def dz(domain: str, dom: str, zone: str) -> None:
	res = []
	if '-' not in dom:
		res.append(dom)
		if len(dom) < 8:
			cake = dom + zone.replace('.','')
			res.append(cake[:8])
			res.append(cake[:7])
			res.append(cake[:6])
			if len(dom + zone) < 9:
				res.append(dom + zone)
		else:
			res.append(dom[:8])
			res.append(dom[:7])
			res.append(dom[:6])
	else:
		res.append(dom)
		res.append(dom.replace('-',''))
		if len(dom.replace('-','')) < 8:
			cake = dom.replace('-','') + zone.replace('.','')
			res.append(cake[:8])
			res.append(cake[:7])
			res.append(cake[:6])
		else:
			res.append(dom.replace('-','')[:8])
			res.append(dom.replace('-','')[:7])
			res.append(dom.replace('-','')[:6])
		if len(dom + zone) < 9:
			res.append(dom + zone)
			res.append(dom.replace('-','') + zone)
		first_word = ''
		for i in range(len(dom.split('-'))):
			if len(dom.split('-')[i]) < 4:
				if i == 0:
					piece1 = dom.split('-')[i]
					piece2 = dom.split('-')[i+1]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
				elif i == (len(dom.split('-')) - 1):
					piece1 = dom.split('-')[i-1]
					piece2 = dom.split('-')[i]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
				else:
					piece1 = dom.split('-')[i]
					piece2 = dom.split('-')[i+1]
					res.append(piece1 + piece2)
					piece1 = dom.split('-')[i-1]
					piece2 = dom.split('-')[i]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
			else:
				res.append(dom.split('-')[i])
				if not first_word:
					first_word = dom.split('-')[i]
		res.append(first_word[:8])
		res.append(first_word[:7])
		res.append(first_word[:6])
	save_result(domain, res)
	return

def wdz(domain: str, dom: str, zone: str) -> None:
	res = []
	res.append(('www' + dom.replace('-','') + zone.replace('.',''))[:8])
	if len(dom) <= 4:
		res.append(('www' + dom.replace('-','') + zone.replace('.',''))[:7])
		res.append(('www' + dom.replace('-','') + zone.replace('.',''))[:6])
	if '-' not in dom:
		res.append(dom)
		if len(dom) < 8:
			cake = dom + zone.replace('.','')
			res.append(cake[:8])
			res.append(cake[:7])
			res.append(cake[:6])
			if len(dom + zone) < 9:
				res.append(dom + zone)
		else:
			res.append(dom[:8])
			res.append(dom[:7])
			res.append(dom[:6])
	else:
		res.append(dom)
		res.append(dom.replace('-',''))
		if len(dom.replace('-','')) < 8:
			cake = dom.replace('-','') + zone.replace('.','')
			res.append(cake[:8])
			res.append(cake[:7])
			res.append(cake[:6])
		else:
			res.append(dom.replace('-','')[:8])
			res.append(dom.replace('-','')[:7])
			res.append(dom.replace('-','')[:6])
		if len(dom + zone) < 9:
			res.append(dom + zone)
			res.append(dom.replace('-','') + zone)
		first_word = ''
		for i in range(len(dom.split('-'))):
			if len(dom.split('-')[i]) < 4:
				if i == 0:
					piece1 = dom.split('-')[i]
					piece2 = dom.split('-')[i+1]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
				elif i == (len(dom.split('-')) - 1):
					piece1 = dom.split('-')[i-1]
					piece2 = dom.split('-')[i]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
				else:
					piece1 = dom.split('-')[i]
					piece2 = dom.split('-')[i+1]
					res.append(piece1 + piece2)
					piece1 = dom.split('-')[i-1]
					piece2 = dom.split('-')[i]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
			else:
				res.append(dom.split('-')[i])
				if not first_word:
					first_word = dom.split('-')[i]
		res.append(first_word[:8])
		res.append(first_word[:7])
		res.append(first_word[:6])
	save_result(domain, res)
	return

def sdz(domain: str, subdom: str, dom: str, zone: str) -> None:
	res = []
	if '-' not in dom:
		res.append(dom)
		if len(dom) < 8:
			cake = dom + zone.replace('.','')
			res.append(cake[:8])
			res.append(cake[:7])
			res.append(cake[:6])
			if len(dom + zone) < 9:
				res.append(dom + zone)
		else:
			res.append(dom[:8])
			res.append(dom[:7])
			res.append(dom[:6])
	else:
		res.append(dom)
		res.append(dom.replace('-',''))
		if len(dom.replace('-','')) < 8:
			cake = dom.replace('-','') + zone.replace('.','')
			res.append(cake[:8])
			res.append(cake[:7])
			res.append(cake[:6])
		else:
			res.append(dom.replace('-','')[:8])
			res.append(dom.replace('-','')[:7])
			res.append(dom.replace('-','')[:6])
		if len(dom + zone) < 9:
			res.append(dom + zone)
			res.append(dom.replace('-','') + zone)
		first_word = ''
		for i in range(len(dom.split('-'))):
			if len(dom.split('-')[i]) < 4:
				if i == 0:
					piece1 = dom.split('-')[i]
					piece2 = dom.split('-')[i+1]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
				elif i == (len(dom.split('-')) - 1):
					piece1 = dom.split('-')[i-1]
					piece2 = dom.split('-')[i]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
				else:
					piece1 = dom.split('-')[i]
					piece2 = dom.split('-')[i+1]
					res.append(piece1 + piece2)
					piece1 = dom.split('-')[i-1]
					piece2 = dom.split('-')[i]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
			else:
				res.append(dom.split('-')[i])
				if not first_word:
					first_word = dom.split('-')[i]
		res.append(first_word[:8])
		res.append(first_word[:7])
		res.append(first_word[:6])
	if not '-' in subdom:
		res.append(subdom)
	res.append(subdom + '.' + dom)
	res.append(subdom.replace('-','') + dom.replace('-',''))
	res.append((subdom.replace('-','') + dom.replace('-',''))[:8])
	if len(dom) < 6:
		res.append(subdom)
		res.append(subdom.replace('-','')[:8])
		res.append(subdom.replace('-','')[:7])
		res.append(subdom.replace('-','')[:6])
	save_result(domain, res)
	return

def wsdz(domain: str, subdom: str, dom: str, zone: str) -> None:
	res = []
	if '-' not in dom:
		res.append(dom)
		if len(dom) < 8:
			cake = dom + zone.replace('.','')
			res.append(cake[:8])
			res.append(cake[:7])
			res.append(cake[:6])
			if len(dom + zone) < 9:
				res.append(dom + zone)
		else:
			res.append(dom[:8])
			res.append(dom[:7])
			res.append(dom[:6])
	else:
		res.append(dom)
		res.append(dom.replace('-',''))
		if len(dom.replace('-','')) < 8:
			cake = dom.replace('-','') + zone.replace('.','')
			res.append(cake[:8])
			res.append(cake[:7])
			res.append(cake[:6])
		else:
			res.append(dom.replace('-','')[:8])
			res.append(dom.replace('-','')[:7])
			res.append(dom.replace('-','')[:6])
		if len(dom + zone) < 9:
			res.append(dom + zone)
			res.append(dom.replace('-','') + zone)
		first_word = ''
		for i in range(len(dom.split('-'))):
			if len(dom.split('-')[i]) < 4:
				if i == 0:
					piece1 = dom.split('-')[i]
					piece2 = dom.split('-')[i+1]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
				elif i == (len(dom.split('-')) - 1):
					piece1 = dom.split('-')[i-1]
					piece2 = dom.split('-')[i]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
				else:
					piece1 = dom.split('-')[i]
					piece2 = dom.split('-')[i+1]
					res.append(piece1 + piece2)
					piece1 = dom.split('-')[i-1]
					piece2 = dom.split('-')[i]
					res.append(piece1 + piece2)
					if not first_word:
						first_word = piece1 + piece2
			else:
				res.append(dom.split('-')[i])
				if not first_word:
					first_word = dom.split('-')[i]
		res.append(first_word[:8])
		res.append(first_word[:7])
		res.append(first_word[:6])
	if not '-' in subdom:
		res.append(subdom)
	res.append(subdom + '.' + dom)
	res.append(subdom.replace('-','') + dom.replace('-',''))
	res.append((subdom.replace('-','') + dom.replace('-',''))[:8])
	if len(dom) < 6:
		res.append(subdom.replace('-','')[:8])
		res.append(subdom.replace('-','')[:7])
		res.append(subdom.replace('-','')[:6])
	res.append(('www' + subdom.replace('-','') + dom.replace('-','') + zone.replace('.',''))[:8])
	save_result(domain, res)
	return

def domain_sorter(domain: str) -> None:
	clean_domain = domain.lower()
	if '://' in clean_domain:
		clean_domain = clean_domain.split('://')[1]
	if ':' in clean_domain:
		clean_domain = clean_domain.split(':')[0]
	#print(clean_domain)
	www, subdom, dom, zone = domain_splitter(clean_domain)
	if not www and not subdom:
		dz(domain, dom, zone)
	if www and not subdom:
		wdz(domain, dom, zone)
	if subdom and not www:
		sdz(domain, subdom, dom, zone)
	if subdom and www:
		wsdz(domain, subdom, dom, zone)
	return

def main() -> None:
	global domains
	global workers
	global res_path
	time_start = datetime.now().strftime("%Y.%m.%d_%H-%M")
	cwd = os.getcwd()
	if os.name == 'posix':
		res_path = f'{cwd}/{time_start}/'
	else:
		res_path = f'{cwd}\\{time_start}\\'
	os.mkdir(res_path)
	create_files()
	if not get_zones():
		print('Check zones.txt\nExit')
		return
	for root, dirs, files in os.walk('./input/'):
		for filename in files:
			if ('.txt' in filename):
				get_input(filename)
	if total == 0:
		print('Check input\nExit')
		return
	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
		executor.map(domain_sorter, domains)
	clean_results()

if __name__ == "__main__":
	main()
