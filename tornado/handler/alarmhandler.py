# !/usr/bin/env python3
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
		path = r'E:\数据\%s\%s\ALARM' % (city, date)
		fh = os.path.join(path, 'Thread-1')
		if os.path.isfile(fh):
			with open(fh) as fin:
				afin = fin.readlines()
				wsd.append(afin[1])

		self.write(json.dumps(wsd))