# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import json
import os
import threading
from src.str_ana import ReckonFramework


city = input('Please enter the province:')
date = input('Please enter the date(格式YYYYMMDD):')


def sn_merge_clean_file(tn):
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
    std = time.clock()
    T1 = threading.Thread(target=sn_merge_clean_file, args=('INFO',))
    T2 = threading.Thread(target=sn_merge_clean_file, args=('ALARM',))
    T3 = threading.Thread(target=sn_merge_clean_file, args=('PERIODIC',))
    T4 = threading.Thread(target=sn_merge_clean_file, args=('PROGRAMINFO',))
    T1.start()
    T2.start()
    T3.start()
    T4.start()
    T1.join()
    T2.join()
    T3.join()
    T4.join()
    print(time.clock() - std)
