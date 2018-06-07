# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


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
                    ditn = dl.decode(encoding='utf-8').rstrip('\n').split('|')
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
                                         'nb': 1, 'version': version, 'modle': modle,
                                         'file': [i + '|' + str(con)]}
                        con += 1
                    else:
                        fid = sn_r[ditn[3]]['file']
                        fid.append(i + '|' + str(con))
                        sn_r[ditn[3]].update({'file': fid})
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
                    ditn = str(dl).rstrip('\n').split('|')
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
                    ditn = str(dl).rstrip('\n').split('|')
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
            with open(os.path.join(self.catalog, i), 'rb') as fo:
                for dl in fo.readlines():
                    ditn = str(dl).rstrip('\n').split('|')
                    if ditn[7] == '':
                        ditn[7] = 0						
                    if ditn[11] == '':
                        ditn[11] = 0

                    if ditn[3] not in infodic.keys():
                        infodic[ditn[3]] = {'st': int(ditn[7]), 'pt': int(ditn[11])}
                    else:
                        infodic[ditn[3]].update({'st': infodic[ditn[3]]['st'] + int(ditn[7])})
                        infodic[ditn[3]].update({'pt': infodic[ditn[3]]['pt'] + int(ditn[11])})
            fo.close()
        return infodic

    def calculate_aminfo_file(self):
        infodic = dict()
        for i in self.dl:
            with open(os.path.join(self.catalog, i), 'rb') as fo:
                for dl in fo.readlines():
                    ditn = str(dl).rstrip('\n').split('|')
                    if ditn[7] == '':
                        ditn[7] = 0						
                    if ditn[11] == '':
                        ditn[11] = 0

                    if ditn[3] not in infodic.keys():
                        infodic[ditn[3]] = {'st': int(ditn[7]), 'pt': int(ditn[11])}
                    else:
                        infodic[ditn[3]].update({'st': infodic[ditn[3]]['st'] + int(ditn[7])})
                        infodic[ditn[3]].update({'pt': infodic[ditn[3]]['pt'] + int(ditn[11])})
            fo.close()
        return infodic

