#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import threading
from handler.base import BaseHandler


class InfoHandler(BaseHandler):
	def get(self):
		pass

	def post(self):
		city = self.get_argument('city')
		date = self.get_argument('date')
		data = self.get_argument('data')
		wsd = list()
		date = date.replace('-','')
		fun_name_list = list()
		dic_file = dict()
		path = '/data/cleandata/%s/%s/INFO' % (city, date)
		for i in json.loads(data):
			list_file = i.split('|')
			if list_file[0] not in dic_file.keys():
				dic_file[list_file[0]] = [[list_file[1], list_file[2]]]
			else:
				tmp_val_ls = dic_file[list_file[0]]
				tmp_val_ls.append([list_file[1], list_file[2]])
				dic_file.update({list_file[0]: tmp_val_ls})
		
		def read_file_threa(file_name,value_list):
			nonlocal wsd
			fh = os.path.join(path, file_name)
			if os.path.isfile(fh):
				with open(fh, 'rb') as fin:
					for i in value_list:
						fin.seek(int(i[0]))
						try:
							wsd.append(fin.read(int(i[1])).decode(encoding='utf-8'))
						except UnicodeDecodeError:
							wsd.append(fin.read(int(i[1])).decode(encoding='gbk'))
						
		for key, values in dic_file.items():
			key = threading.Thread(target=read_file_threa, args=(key, values,))
			fun_name_list.append(key)
			
		for i in fun_name_list:
			i.start()
		for i in fun_name_list:
			i.join()
		wsd.sort(key = lambda x:(re.match('([0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{6})',x).group(1)),reverse = True)
		self.write(json.dumps(wsd))
