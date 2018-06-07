# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from common.tools import CommonTool

path = input('please enter the file directory')
wp = input('please enter the file save directory')
if not os.path.isdir(wp):
    os.makedirs(wp)
file_q = CommonTool(path)
fq = file_q.file_queue()


class SyncopateTools(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global fq
        fo = open(os.path.join(wp, self.name), 'ab')
        while not fq.empty():
            for line in fq.get():
                fo.write(line)
        fo.close()


if __name__ == "__main__":
    import time

    threads = []
    starttime = time.clock()
    for i in range(0, 20):
        thread = SyncopateTools(i)
        threads.append(thread)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(time.clock() - starttime)
