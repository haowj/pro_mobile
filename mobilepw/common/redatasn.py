# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


class RecombinationData:
    def __init__(self, alarm, info, periodic, programinfo, city, date):
        self.info = info
        self.alarm = alarm
        self.periodic = periodic
        self.programinfo = programinfo
        self.city = city
        self.date = date

    def insert_sn_data(self):
        sn_r = dict()
        for i in self.periodic:
            dl = json.loads(i)
            sn_r[dl[0]] = dl[1]
            sn_r[dl[0]].update({'iofile': ''})
            sn_r[dl[0]].update({'amfile': ''})
            sn_r[dl[0]].update({'plurl': ''})
            sn_r[dl[0]].update({'aifile':''})
            sn_r[dl[0]].update({'pt': 0})
            sn_r[dl[0]].update({'st': 0})
        for dt in self.programinfo:
            dlb = json.loads(dt)
            if dlb[0] in sn_r.keys():
                sn_r[dlb[0]].update(dlb[1])
        for dt in self.info:
            dlb = json.loads(dt)
            if dlb[0] in sn_r.keys():
                sn_r[dlb[0]].update({'iofile': dlb[1]})
        for dt in self.alarm:
            dlb = json.loads(dt)
            if dlb[0] in sn_r.keys():
                sn_r[dlb[0]].update({'amfile': dlb[1]})

        return sn_r
