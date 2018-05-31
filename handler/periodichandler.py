# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import tornado.web


class PeriodicHandler(tornado.web.RequestHandler):
	def post(self):
		pass

	def get(self):
		self.write('hello, world')