# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import threading
from src.str_ana import ReckonFramework


city = input('Please enter the province:')
date = input('Please enter the date(格式YYYYMMDD):')

t_l = ['INFO', 'ALARM', 'PERIODIC', 'PROGRAMINFO']

class SyncopateTools(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global tn
        global city
        global date
        global t_l
        if t_l:
            tn = t_l.pop(0)
            path = '/data/cleandata/%s/%s/%s' % (city, date, tn)
            spd = path.split('/')
            sn_path = path.replace(spd[2], 'rowdata')
            if not os.path.isdir(sn_path):
                os.makedirs(sn_path)
            filedate = ReckonFramework(path)
            if tn == 'INFO':
                bast = filedate.calculate_info_file()
            elif tn == 'ALARM':
                bast = filedate.calculate_alarm_file()
            elif tn == 'PERIODIC':
                bast = filedate.calculate_sn_file()
            elif tn == 'PROGRAMINFO':
                bast = filedate.calculate_aminfo_file()

            with open(os.path.join(sn_path, 'sn_list'), 'ab') as fo:
                for i in bast.items():
                    fo.write(bytes(json.dumps(i) + '\n', encoding="utf8"))


if __name__ == "__main__":
    import time
    threads = []
    starttime = time.clock()
    for i in range(4):
        thread = SyncopateTools(i)
        threads.append(thread)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(time.clock() - starttime)



