# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import json
import os
from src.str_ana import ReckonFramework

std = time.clock()
path = input('please enter the file path')
# sn_path = input('please enter file save path')
spd = path.split('/')
sn_path = path.replace(spd[2], 'rowdata')
if not os.path.isdir(sn_path):
	os.makedirs(sn_path)
filedate = ReckonFramework(path)
bast = filedate.calculate_info_file()
with open(os.path.join(sn_path,'sn_list'), 'ab') as fo:
	for i in bast.items():
		fo.write(bytes(json.dumps(i) + '\n', encoding="utf8"))
print(time.clock() - std)
