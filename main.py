from func import *
import os
folder = 'numass\\set_27'
try:
	os.remove('stat.txt')
except FileNotFoundError:
	pass

list_folders = os.listdir(folder)[1:]
dict_folders = {int(name_folder[1:-16]) : name_folder for name_folder in list_folders}
dict_keys = dict_folders.keys()
for p in sorted(dict_keys):
	path = dict_folders.get (p)
	print (path)
# # path = 'numass\\set_27\\p1(30s)(HV1=18600)'
	

	if path.find('1400') == -1:
		hv = path[-6:-1]
		lists_num_noiz = file_txt (folder + '\\' + path)
		counter (lists_num_noiz[0], lists_num_noiz[1], hv)

