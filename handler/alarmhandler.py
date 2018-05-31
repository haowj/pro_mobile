# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import tornado.web
import json

class AlarmHandler(tornado.web.RequestHandler):
	def post(self):
		pass

	def get(self):
		city = self.get_arguments('city')
		date = self.get_arguments('date')
		data = self.get_arguments('data')
		dl = json.loads(data)
		path = r'E:\数据\%s\%s\ALARM' % (city, date)
		for i in data:
			pass
		file_w = open(path)
		fin = file_w.readlines()

		self.write('hello, world!')