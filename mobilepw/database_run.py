# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import os
from common.redatasn import RecombinationData
from common.snlistinsert import ValuesInsertData

city = input('Please enter the province:')
date = input('Please enter the date(格式YYYYMMDD):')
st = time.clock()

pio_ph = '/data/rowdata/%s/%s/PROGRAMINFO/sn_list' % (city, date)

if os.path.isfile(pio_ph):
    pio = open(pio_ph, 'r')
    PROGRAMINFO = pio.readlines()
else:
    PROGRAMINFO = dict()

ios_ph = '/data/rowdata/%s/%s/INFO/sn_list' % (city, date)
if os.path.isfile(ios_ph):
    ios = open(ios_ph, 'r')
    INFO = ios.readlines()
else:
    INFO = dict()

alm_ph = '/data/rowdata/%s/%s/ALARM/sn_list' % (city, date)
if os.path.isfile(alm_ph):
    alm = open(alm_ph, 'r')
    ALARM = alm.readlines()
else:
    ALARM = dict()

pic_ph = '/data/rowdata/%s/%s/PERIODIC/sn_list' % (city, date)
if os.path.isfile(pic_ph):
    pic = open(pic_ph, 'r')
    PERIODIC = pic.readlines()
else:
    PERIODIC = dict()


data = RecombinationData(alarm=ALARM, info=INFO, periodic=PERIODIC,
                          programinfo=PROGRAMINFO, city=city, date=date)

fin = data.insert_sn_data()

insert_d = ValuesInsertData(fin, city, date)
insert_d.insert_sn_data()
insert_d.insert_city_data()
insert_d.insert_cpname_data()
insert_d.insert_modle_data()
insert_d.insert_asmd_data()
print(time.clock() - st)
