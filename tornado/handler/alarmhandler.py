#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
from handler.base import BaseHandler


class AlarmHandler(BaseHandler):
	def get(self):
		pass

	def post(self):
		city = self.get_arguments('city')
		date = self.get_arguments('date')
		data = self.get_arguments('data')
		wsd = list()
		dic_file = dict()
		for i in json.loads(data):
			list_file = i.split('|')
			if list_file[0] not in dic_file.keys():
				dic_file[list_file[0]] = [list_file[1]]
			else:
				tmp_val_ls = dic_file[list_file[0]]
				tmp_val_ls.append(list_file[1])
				dic_file.update({list_file[0]: tmp_val_ls})
		for i in dic_file.items():
			path = '/data/cleandata/%s/%s/ALARM' % (city, date)
			fh = os.path.join(path, i[0])
			if os.path.isfile(fh):
				with open(fh) as fin:
					afin = fin.readlines()
					for idtext in i[1]:
						wsd.append(afin[int(idtext)].rstrip('\n'))
		self.write(json.dumps(wsd))
