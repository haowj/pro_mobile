# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re


class ReckonFramework:
    def __init__(self, catalog):
        self.catalog = catalog
        self.dl = os.listdir(catalog)

    def calculate_sn_file(self):
        sn_r = dict()
        version = ''
        modle = ''
        for i in self.dl:
            con = 0
            with open(os.path.join(self.catalog, i), 'rb') as fo:
                for dl in fo.readlines():
                    try:
                        ditn = dl.decode(encoding='utf-8').rstrip('\n').split('|')
                    except UnicodeDecodeError:
                        ditn = dl.decode(encoding='gbk').rstrip('\n').split('|')
                    if len(ditn) >= 65:
                        version = ditn[63]
                        modle = ditn[64]
                    if ditn[10] == '':
                        ditn[10] = 0
                    if ditn[11] == '':
                       ditn[11] = 0
                    if ditn[21] == '':
                       ditn[21] = 0
                    if ditn[22] =='':
                       ditn[22] = 0

                    if ditn[3] not in sn_r.keys():
                        sn_r[ditn[3]] = {'pc': int(ditn[10]),
                                         'psc': int(ditn[11]),
                                         'et': int(ditn[21]),
                                         'ert': int(ditn[22]),
                                         'nb': 1,
                                         'version': version,
                                         'modle': modle,
                                         'city': ditn[2],
                                         'cpname': ditn[33],
                                         'asmd': ditn[30],
                                         'pcfile': [i + '|' + str(con)]}
                        con += 1
                    else:
                        fid = sn_r[ditn[3]]['pcfile']
                        fid.append(i + '|' + str(con))
                        sn_r[ditn[3]].update({'pcfile': fid})
                        sn_r[ditn[3]].update({'pc': sn_r[ditn[3]]['pc'] + int(ditn[10])})					
                        sn_r[ditn[3]].update({'psc': sn_r[ditn[3]]['psc'] + int(ditn[11])})
                        sn_r[ditn[3]].update({'et': sn_r[ditn[3]]['et'] + int(ditn[21])})
                        sn_r[ditn[3]].update({'ert': sn_r[ditn[3]]['ert'] + int(ditn[22])})
                        sn_r[ditn[3]].update({'nb': sn_r[ditn[3]]['nb'] + 1})
                        con += 1
            fo.close()
        return sn_r

    def calculate_alarm_file(self):
        infodic = dict()
        for i in self.dl:
            con = 0
            with open(os.path.join(self.catalog, i), 'rb') as fo:
                for dl in fo.readlines():
                    try:
                        ditn = dl.decode(encoding='utf-8').rstrip('\n').split('|')
                    except UnicodeDecodeError:
                        ditn = dl.decode(encoding='gbk').rstrip('\n').split('|')
                    if ditn[3] not in infodic.keys():
                        infodic[ditn[3]] = [i + '|' + str(con)]
                        con += 1
                    else:
                        fid = infodic[ditn[3]]
                        fid.append(i + '|' + str(con))
                        infodic.update({ditn[3]: fid})
                        con += 1
            fo.close()
        return infodic

    def calculate_info_file(self):
        infodic = dict()
        for i in self.dl:
            con = 0
            with open(os.path.join(self.catalog, i), 'rb') as fo:
                for dl in fo.readlines():
                    try:
                        ditn = dl.decode(encoding='utf-8').rstrip('\n').split('|')
                    except UnicodeDecodeError:
                        ditn = dl.decode(encoding='gbk').rstrip('\n').split('|')
                    if ditn[5] not in infodic.keys():
                        infodic[ditn[5]] = [i + '|' + str(con)]
                        con += 1
                    else:
                        fid = infodic[ditn[5]]
                        fid.append(i + '|' + str(con))
                        infodic.update({ditn[5]: fid})
                        con += 1
            fo.close()
        return infodic

    def calculate_aminfo_file(self):
        infodic = dict()
        for i in self.dl:
            con = 0			
            with open(os.path.join(self.catalog, i), 'rb') as fo:
                for dl in fo.readlines():
                    try:
                        ditn = dl.decode(encoding='utf-8').rstrip('\n').split('|')
                        s_file = re.search('\|([a-zA-Z]{2,8}:\/\/.*?)\|([0-9]{10}|[0-9]{13})\|([0-9]*)', dl.decode(encoding='utf-8'))     
                    except UnicodeDecodeError:
                        ditn = dl.decode(encoding='gbk').rstrip('\n').split('|')
                        s_file = re.search('\|([a-zA-Z]{2,8}:\/\/.*?)\|([0-9]{10}|[0-9]{13})\|([0-9]*)', dl.decode(encoding='gbk'))     
                    if ditn[7] == '':
                        ditn[7] = 0						
                    if s_file:
                        ditn[9] = s_file.group(1)
                        if s_file.group(3) == '':
                            ditn[11] = 0
                        else:
                            ditn[11] = int(s_file.group(3))
                
                    else:
                        if ditn[11] == '':
                            ditn[11] = 0
                        else:
                            ditn[11] = int(ditn[11])

                    if ditn[3] not in infodic.keys():
                        infodic[ditn[3]] = {'st': int(ditn[7]), 'pt': ditn[11], 'plurl': ditn[9],'aifile': [i + '|' + str(con)]}
                        con += 1
                    else:
                        fid = infodic[ditn[3]]['aifile']
                        fid.append(i + '|' + str(con))
                        infodic[ditn[3]].update({'aifile': fid})
                        infodic[ditn[3]].update({'st': infodic[ditn[3]]['st'] + int(ditn[7])})
                        infodic[ditn[3]].update({'pt': infodic[ditn[3]]['pt'] + ditn[11]})
                        con += 1
            fo.close()
        return infodic


