# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import tornado.httpserver
import tornado.web
import tornado.ioloop
from tornado.options import options, define

tornado.options.define("port", default=8888, help="Run server on a specific port", type=int)
tornado.options.define("host", default="localhost", help="Run server on a specific host")
tornado.options.define("url", default=None, help="Url to show in HTML")
tornado.options.define("config", default="./config.yaml", help="config file's full path")
tornado.options.parse_command_line()

setting = {

}

application = tornado.web.Application(
	[
		(r'/alarm', 'handler.alarmhandler.AlarmHandler'),
		(r'/info', 'handler.infohandler.InfoHandler'),
		(r'/periodic', 'handler.periodichnadler.PeriodicHandler')
	], **setting
)


if __name__ == "__main__":
	try:
		application.listen(tornado.options.options.port)
		tornado.ioloop.IOLoop.instance().start()
	except:
		import traceback

		print(traceback.print_exc())
	finally:
		sys.exit(0)