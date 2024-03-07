import concurrent.futures
from datetime import datetime
import os

domains = []
res_path = ''
workers = 16
counter = 0
total = 0

def get_input() -> bool:
	global domains
	global counter
	global total
	try:
		with open('input.txt', 'r') as f:
			domains = f.read().split('\n')
		if len(domains) > 0:
			total = len(domains)
			return True
		return False
	except:
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

def save_result(res: list) -> None:
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
			result_4 += f'{element}\n'
		elif len(element) == 5:
			result_5 += f'{element}\n'
		elif len(element) == 6:
			result_6 += f'{element}\n'
		elif len(element) == 7:
			result_7 += f'{element}\n'
		elif len(element) == 8:
			result_8 += f'{element}\n'
		else:
			result_big += f'{element}\n'
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

def process_domain(domain: str) -> None:
	#print(domain)
	clean_domain = domain
	res = []
	if '://' in clean_domain: #https://anydomain.com:2083
		clean_domain = clean_domain.split('://')[1] #anydomain.com:2083
	if ':' in clean_domain: #anydomain.com:2083
		clean_domain = clean_domain.split(':')[0] #anydomain.com
	if clean_domain.count('.') == 1: #anydomain.com
		if len(clean_domain.split('.')[0]) <= 3: #dom.com
			res.append(clean_domain) #dom.com
			res.append(clean_domain.replace('.','')) #domcom
			res.append(clean_domain.split('.')[0]) #dom
			save_result(res)
			return
		else: #anydomain.com
			res.append(clean_domain.split('.')[0]) #anydomain / #anydomain-else
			if '-' not in clean_domain: #anydomain.com
				res.append(clean_domain.split('.')[0][:8]) #anydomai
				res.append(clean_domain.split('.')[0][:7]) #anydoma
				res.append(clean_domain.split('.')[0][:6]) #anydom
			else: #anydomain-else.com
				res.append(clean_domain.split('.')[0].replace('-','')) #anydomainelse
				res.append(clean_domain.split('.')[0].replace('-','')[:8]) #anydomai
				res.append(clean_domain.split('.')[0].replace('-','')[:7]) #anydoma
				res.append(clean_domain.split('.')[0].replace('-','')[:6]) #anydom
				for i in range(len(clean_domain.split('.')[0].split('-'))):
					if len(clean_domain.split('.')[0].split('-')[i]) < 4: #an-do-ma.com
						if i == 0: #an
							piece1 = clean_domain.split('.')[0].split('-')[i] #an
							piece2 = clean_domain.split('.')[0].split('-')[i+1] #do
							res.append(f'{piece1}{piece2}') #ando
						elif i == (len(clean_domain.split('.')[0].split('-')) - 1): #ma
							piece1 = clean_domain.split('.')[0].split('-')[i-1] #do
							piece2 = clean_domain.split('.')[0].split('-')[i] #ma
							res.append(f'{piece1}{piece2}') #doma
						else: #do
							piece1 = clean_domain.split('.')[0].split('-')[i] #do
							piece2 = clean_domain.split('.')[0].split('-')[i+1] #ma
							res.append(f'{piece1}{piece2}') #doma
							piece1 = clean_domain.split('.')[0].split('-')[i-1] #an
							piece2 = clean_domain.split('.')[0].split('-')[i] #do
							res.append(f'{piece1}{piece2}') #ando
					else:
						res.append(clean_domain.split('.')[0].split('-')[i]) #anydomain / #else
			save_result(res)
			return
	if clean_domain.count('.') == 2: #www.anydomain.com
		if clean_domain.split('.')[0] == 'www': #www.anydomain.com
			if len(clean_domain.split('.')[1]) < 8: #www.dom.com
				clean_domain.split('.')[1]
				res.append(clean_domain.replace('.','')[:8])
				res.append(clean_domain.replace('.','')[:7])
				res.append(clean_domain.replace('.','')[:6])
				piece1 = clean_domain.split('.')[1]
				piece2 = clean_domain.split('.')[2]
				dotcake = f'{piece1}.{piece2}'
				res.append(dotcake)
				cake = f'{piece1}{piece2}'
				res.append(cake)
				save_result(res)
				return
			else:
				res.append(clean_domain.split('.')[1]) #anydomain / #anydomain-else
				if '-' not in clean_domain.split('.')[1]: #www.anydomain.com
					res.append(clean_domain.split('.')[1][:8]) #anydomai
					res.append(clean_domain.split('.')[1][:7]) #anydoma
					res.append(clean_domain.split('.')[1][:6]) #anydom
					piece5 = clean_domain.split('.')[1][:5] #anydo
					res.append(f'www{piece5}') #wwwanydo
				else: #www.anydomain-else.com
					res.append(clean_domain.split('.')[1].replace('-','')) #anydomainelse
					res.append(clean_domain.split('.')[1].replace('-','')[:8]) #anydomai
					res.append(clean_domain.split('.')[1].replace('-','')[:7]) #anydoma
					res.append(clean_domain.split('.')[1].replace('-','')[:6]) #anydom
					piece5 = clean_domain.split('.')[1].replace('-','')[:5] #anydo
					res.append(f'www{piece5}') #wwwanydo
					for i in range(len(clean_domain.split('.')[1].split('-'))): 
						if len(clean_domain.split('.')[1].split('-')[i]) < 4: #www.an-do-ma.com
							if i == 0:
								piece1 = clean_domain.split('.')[1].split('-')[i] #an
								piece2 = clean_domain.split('.')[1].split('-')[i+1] #do
								res.append(f'{piece1}{piece2}') #ando
							elif i == (len(clean_domain.split('.')[1].split('-')) - 1):
								piece1 = clean_domain.split('.')[1].split('-')[i-1] #do
								piece2 = clean_domain.split('.')[1].split('-')[i] #ma
								res.append(f'{piece1}{piece2}') #doma
							else:
								piece1 = clean_domain.split('.')[1].split('-')[i] #do
								piece2 = clean_domain.split('.')[1].split('-')[i+1] #ma
								res.append(f'{piece1}{piece2}') #doma
								piece1 = clean_domain.split('.')[1].split('-')[i-1] #an
								piece2 = clean_domain.split('.')[1].split('-')[i] #do
								res.append(f'{piece1}{piece2}') #ando
						else:
							res.append(clean_domain.split('.')[1].split('-')[i]) #anydomain / #else
				save_result(res)
				return
		else: #sub.dom.com
			if '-' not in clean_domain.split('.')[1]:
				if len(clean_domain.split('.')[1]) < 8:
					res.append(clean_domain.split('.')[0]) #sub
					res.append(clean_domain.split('.')[1]) #dom
					piece1 = clean_domain.split('.')[0] #sub
					piece2 = clean_domain.split('.')[1] #dom
					res.append(f'{piece1}.{piece2}') #sub.dom
					res.append(f'{piece1}{piece2}') #subdom
					res.append(clean_domain.replace('.','')[:8]) #subdomco
					res.append(clean_domain.replace('.','')[:7]) #subdomc
					res.append(clean_domain.replace('.','')[:6]) #subdom
					save_result(res)
					return
				else:
					piece1 = clean_domain.split('.')[0]
					piece2 = clean_domain.split('.')[1]
					dotcake = f'{piece1}.{piece2}'
					res.append(dotcake)
					cake = f'{piece1}{piece2}'
					res.append(cake)
					res.append(cake[:8])
					res.append(clean_domain.split('.')[1])
					res.append(clean_domain.split('.')[1][:8])
					res.append(clean_domain.split('.')[1][:7])
					res.append(clean_domain.split('.')[1][:6])
					save_result(res)
					return
			else:
				if len(clean_domain.split('.')[1].replace('-','')) < 8: #sub.dom-ain.com
					piece1 = clean_domain.split('.')[0]
					piece2 = clean_domain.split('.')[1]
					dotcake = f'{piece1}.{piece2}'
					res.append(dotcake)
					res.append(dotcake.replace('.',''))
					res.append(dotcake.replace('.','').replace('-',''))
					res.append(clean_domain.split('.')[1].replace('-',''))
					res.append(dotcake.replace('.','').replace('-','')[:8])
					res.append(dotcake.replace('.','').replace('-','')[:7])
					res.append(dotcake.replace('.','').replace('-','')[:6])
					for i in range(len(clean_domain.split('.')[1].split('-'))): 
						if len(clean_domain.split('.')[1].split('-')[i]) < 4: #www.an-do-ma.com
							if i == 0:
								piece1 = clean_domain.split('.')[1].split('-')[i] #an
								piece2 = clean_domain.split('.')[1].split('-')[i+1] #do
								res.append(f'{piece1}{piece2}') #ando
							elif i == (len(clean_domain.split('.')[1].split('-')) - 1):
								piece1 = clean_domain.split('.')[1].split('-')[i-1] #do
								piece2 = clean_domain.split('.')[1].split('-')[i] #ma
								res.append(f'{piece1}{piece2}') #doma
							else:
								piece1 = clean_domain.split('.')[1].split('-')[i] #do
								piece2 = clean_domain.split('.')[1].split('-')[i+1] #ma
								res.append(f'{piece1}{piece2}') #doma
								piece1 = clean_domain.split('.')[1].split('-')[i-1] #an
								piece2 = clean_domain.split('.')[1].split('-')[i] #do
								res.append(f'{piece1}{piece2}') #ando
						else:
							res.append(clean_domain.split('.')[1].split('-')[i]) #anydomain / #else
					save_result(res)
					return
				else:
					piece1 = clean_domain.split('.')[0]
					piece2 = clean_domain.split('.')[1]
					dotcake = f'{piece1}.{piece2}'
					res.append(dotcake)
					res.append(dotcake.replace('.',''))
					res.append(dotcake.replace('.','').replace('-',''))
					res.append(dotcake.replace('.','').replace('-','')[:8])
					res.append(dotcake.replace('.','').replace('-','')[:7])
					res.append(dotcake.replace('.','').replace('-','')[:6])
					for i in range(len(clean_domain.split('.')[1].split('-'))): 
						if len(clean_domain.split('.')[1].split('-')[i]) < 4: #www.an-do-ma.com
							if i == 0:
								piece1 = clean_domain.split('.')[1].split('-')[i] #an
								piece2 = clean_domain.split('.')[1].split('-')[i+1] #do
								res.append(f'{piece1}{piece2}') #ando
							elif i == (len(clean_domain.split('.')[1].split('-')) - 1):
								piece1 = clean_domain.split('.')[1].split('-')[i-1] #do
								piece2 = clean_domain.split('.')[1].split('-')[i] #ma
								res.append(f'{piece1}{piece2}') #doma
							else:
								piece1 = clean_domain.split('.')[1].split('-')[i] #do
								piece2 = clean_domain.split('.')[1].split('-')[i+1] #ma
								res.append(f'{piece1}{piece2}') #doma
								piece1 = clean_domain.split('.')[1].split('-')[i-1] #an
								piece2 = clean_domain.split('.')[1].split('-')[i] #do
								res.append(f'{piece1}{piece2}') #ando
						else:
							res.append(clean_domain.split('.')[1].split('-')[i]) #anydomain / #else
					save_result(res)
					return

	if clean_domain.count('.') == 3: #www.sub.domain.com
		if clean_domain.split('.')[0] != 'www': #subsub.sub.domain.com
			piece1 = clean_domain.split('.')[0] #subsub
			piece2 = clean_domain.split('.')[1] #sub
			piece3 = clean_domain.split('.')[2] #domain
			dotcake = f'{piece1}.{piece2}.{piece3}'
			res.append(f'{piece1}.{piece2}.{piece3}') #subsub.sub.domain
			piece1 = clean_domain.split('.')[0].replace('-','') #subsub
			piece2 = clean_domain.split('.')[1].replace('-','') #sub
			piece3 = clean_domain.split('.')[2].replace('-','') #domain
			cake = f'{piece1}{piece2}{piece3}'
			res.append(cake) #subsubsubdomain
			res.append(cake[:8]) #subsubsu
			for piece in dotcake.split('.'):
				if '-' in piece: #one-tw
					for i in range(len(piece.split('-'))):
						if len(piece.split('-')[i]) >= 3:
							res.append(piece.split('-')[i]) #one
						else: #an-do-ma
							if i == 0:
								ipiece1 = clean_domain.split('.')[1].split('-')[i] #an
								ipiece2 = clean_domain.split('.')[1].split('-')[i+1] #do
								res.append(f'{ipiece1}{ipiece2}') #ando
							elif i == (len(clean_domain.split('.')[1].split('-')) - 1):
								ipiece1 = clean_domain.split('.')[1].split('-')[i-1] #do
								ipiece2 = clean_domain.split('.')[1].split('-')[i] #ma
								res.append(f'{ipiece1}{ipiece2}') #doma
							else:
								ipiece1 = clean_domain.split('.')[1].split('-')[i] #do
								ipiece2 = clean_domain.split('.')[1].split('-')[i+1] #ma
								res.append(f'{ipiece1}{ipiece2}') #doma
								ipiece1 = clean_domain.split('.')[1].split('-')[i-1] #an
								ipiece2 = clean_domain.split('.')[1].split('-')[i] #do
								res.append(f'{ipiece1}{ipiece2}') #ando
				else: #onetw
					res.append(piece) #onetw
			save_result(res)
			return
		else: #www.sub.dom-ain.com
			piece1 = clean_domain.split('.')[1] #sub
			piece2 = clean_domain.split('.')[2] #dom-ain
			dotcake = f'{piece1}.{piece2}'
			res.append(f'{piece1}.{piece2}') #sub.dom-ain
			piece1 = clean_domain.split('.')[1].replace('-','') #sub
			piece2 = clean_domain.split('.')[2].replace('-','') #domain
			cake = f'{piece1}{piece2}'
			res.append(cake) #subdomain
			res.append(cake[:8]) #subdomai
			piece5 = cake[:5]
			res.append(f'www{piece5}')
			for piece in dotcake.split('.'):
				if '-' in piece: #one-tw
					for i in range(len(piece.split('-'))):
						if len(piece.split('-')[i]) >= 3:
							res.append(piece.split('-')[i]) #one
						else: #an-do-ma
							if i == 0:
								ipiece1 = clean_domain.split('.')[1].split('-')[i] #an
								ipiece2 = clean_domain.split('.')[1].split('-')[i+1] #do
								res.append(f'{ipiece1}{ipiece2}') #ando
							elif i == (len(clean_domain.split('.')[1].split('-')) - 1):
								ipiece1 = clean_domain.split('.')[1].split('-')[i-1] #do
								ipiece2 = clean_domain.split('.')[1].split('-')[i] #ma
								res.append(f'{ipiece1}{ipiece2}') #doma
							else:
								ipiece1 = clean_domain.split('.')[1].split('-')[i] #do
								ipiece2 = clean_domain.split('.')[1].split('-')[i+1] #ma
								res.append(f'{ipiece1}{ipiece2}') #doma
								ipiece1 = clean_domain.split('.')[1].split('-')[i-1] #an
								ipiece2 = clean_domain.split('.')[1].split('-')[i] #do
								res.append(f'{ipiece1}{ipiece2}') #ando
				else: #onetw
					res.append(piece) #onetw
			save_result(res)
			return

def main() -> None:
	global domains
	global workers
	global res_path
	time_start = datetime.now().strftime("%Y.%m.%d_%H-%M")
	cwd = os.getcwd()
	res_path = f'{cwd}\\{time_start}\\'
	os.mkdir(res_path)
	create_files()
	if not get_input():
		print('Check input file (./input.txt for default). Exit')
		return
	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
		executor.map(process_domain, domains)
	clean_results()

if __name__ == "__main__":
	main()