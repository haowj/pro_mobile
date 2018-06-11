# -*- coding: utf-8 -*-
"""
Created on 2018-5-8
@author: wj
"""
import os
import gzip
import pymysql
import redis
from queue import Queue


class CommonTool:
    def __init__(self, catalog):
        # 探针版本--,设备类型,设备SN
        self.catalog = catalog
        self.equipment = Queue()

    def file_list(self):
        for data in self.__get_summary_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    try:
                        yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                    except UnicodeError:
                        yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_queue(self):
        filename_list = os.listdir(self.catalog)
        for i in range(len(filename_list)):
            if filename_list[i][-2:] == 'gz':
                path = os.path.join(self.catalog, filename_list[i])
                if os.path.isfile(path):
                    self.equipment.put(self.__read_log_file(path))
        return self.equipment

    def __get_summary_file(self):
        filename_list = os.listdir(self.catalog)
        for i in range(len(filename_list)):
            if filename_list[i][-2:] == 'gz':
                path = os.path.join(self.catalog, filename_list[i])
                if os.path.isfile(path):
                    yield self.__read_log_file(path)

    # 读取文件数据
    def __read_log_file(self, path):
        if os.path.exists(path):
            with gzip.open(path, 'r') as f:
                for line in f:
                    yield line
        else:
            print('the path [{}] is not exist!'.format(path))

    @staticmethod
    def db_mysql_connect():
        return pymysql.connect("192.168.1.222", "root", "cmcc123", "mobile_application", charset="utf8")

    @staticmethod
    def db_redis_connect():
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        return redis.Redis(connection_pool=pool)
