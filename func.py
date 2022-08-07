import copy
from math import * 
def file_txt (path):
	global list_num, list_noiz

	list_num = [[], [], [], [], [], [], [], []]
	list_noiz = []
	line = 0
	num = 0
	s_ch = 0

	with open(path, 'r') as f:
		print ('Чтение файла...')
		list_lines = f.readlines()
		print ('Перезапись файла...')
	while line < len(list_lines):
		for i in range(24):	
			# bol = list_lines[line].split(':')[1]
			# list_num[7].append(int(bol.split('.')[0] + bol.split('.')[1]) + (i * 8))
			# list_num[7].append(line+i)
			list_num[7].append(float(list_lines[line].split(':')[1][:-2]))
		for i in range(7):
			line += 2
			list_num[i] += [int(a) for a in list_lines[line].split()]
			line += 1
	with_noiz = copy.deepcopy(list_num)
	print ('Поиск шума...')
	del with_noiz[7]
	for n_ch in with_noiz:
		while s_ch < len(n_ch):
			if (max(n_ch[s_ch:s_ch+24])-min(n_ch[s_ch:s_ch+24])) > 100:
				del n_ch[s_ch:s_ch+24]
			s_ch += 24
		list_noiz.append(sum(n_ch)//len(n_ch))
	print ('Запись файла...')
	with open('file.txt', 'w') as f:
		while num < len(list_num[7]):
			for n_ch in range (len(list_num)-1):
				f.write(str(list_num[n_ch][num]-list_noiz[n_ch]) + ' ')
			f.write(str(list_num[7][num]) + '\n')
			num += 1
	return list_num, list_noiz

def counter (list_num, list_noiz, hv):
	list_chast = copy.deepcopy(list_num)
	num = 0
	nitr = 0
	print ('Подсчет частиц...')
	while num < len(list_chast[7]):
			for n_ch in range (len(list_chast)-1):
				if (list_chast[n_ch][num]-list_noiz[n_ch]) > 200:
					nitr += 1
					for i in range(8):
						del (list_chast[i][n_ch])
					num -= 1
			num += 1

	with open('stat.txt', 'a') as f:
		f.write(str(nitr) + ' ' + str(hv) + '\n')

# line = 0
# while line < len(list_lines)-3:
# 	list_num[7].append (float(list_lines[line][5:-2]))
# 	for i in range (7):
# 		list_num.append (list_num[7][-1] + 0.00000008)

# 	line = line + 2
# 	for i in range(7):
# 		print (line)
# 		print (list_lines[line].split())
# 		list_num[i].append ([int(a) for a in list_lines[line].split()])
		
# 		line = line + 3
# 	line = line + 1
# 	print (line, '--')

# with open('file.txt', 'r') as f:
# 	while i < len (list_lines[0]):
# 		for ch in range(8):
# 			print (str(list_lines[ch][i-ch] + ' '))
# 			f.write(str(list_lines[ch][i-ch] + ' '))
# 		i = i + 1
# 		f.write('\n')





# list_str_num = [a[:-2] for a in list_str[2::3]]
# list_ch_num = [[], [], [], [], [], [], []]
# list_ch_mid = [[], [], [], [], [], [], []]
# list_ch_noiz = []

# for i in range(7):
# 	for j in list_str_num[i::7]:
# 		list_ch_num[i] += [int(a) for a in j.split()]

# for i in range(7):
# 	for j in range((len(list_ch_num[i])//24)):
# 		if (max(list_ch_num[i][j*24:j*24+24]) - min(list_ch_num[i][j*24:j*24+24])) < 100:
# 			for n in list_ch_num[i][j*24:j*24+24]:
# 				list_ch_mid[i].append(n)
# 	list_ch_noiz.append(sum(list_ch_mid[i])//len(list_ch_mid[i]))

# with open('file.txt', 'w') as aboba:
# 	for i in range(len(list_ch_num[0])):
# 		for j in range(7):
# 			aboba.write(str(list_ch_num[j][i]-list_ch_noiz[j]) + ' ')
# 		aboba.write(str(i*0.00000008))
# 		aboba.write('\n')