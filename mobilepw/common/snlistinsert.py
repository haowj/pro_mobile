# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from common.tools import CommonTool


class ValuesInsertData:
	"""
		0: 城市分布
		1: 牌照方分布
		2: 终端分布
		3: 接入分布
		4: 播放方式分布
		sn_id: sn编码
		uptimes: 数据写入时间
		对应SN_MAPPING表数据分布
		表名  时间_SN_MAPPING_DATA
		字段 sn_id 0, 1, 2, 3, 4, uptimes

	"""

	def __init__(self, data, city, date):
		self.data = data
		self.city = city
		self.date = date

	def insert_sn_data(self):
		db = CommonTool.db_mysql_connect()
		cursor = db.cursor()
		sql = u"""
        insert into T_SN_LIST_DATA (startdate, province, sn_id, 
        equipmentmodel, Probeversionnumber, Boot, STBPERIODIC, 
        STBALARM, Successfulplaybackrate, Cartonoccupationratio, EPGsuccessrate, 
        asmd, cpname, city_code, plurl, Programinfo)
        values ('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, %s, 
        '%s', '%s', '%s', '%s', '%s')
      """
		for dl in self.data.items():
			if dl[1]['pc'] == 0:
				num1 = 'null'
			else:
				num1 = dl[1]['psc'] / dl[1]['pc']
			if dl[1]['pt'] == 0:
				num2 = 'null'
			else:
				num2 = dl[1]['st'] / dl[1]['pt']
			if dl[1]['et'] == 0:
				num3 = 'null'
			else:
				num3 = dl[1]['ert'] / dl[1]['et']
			cursor.execute(sql % (self.date, self.city, dl[0],
			                      dl[1]['modle'],
			                      dl[1]['version'],
			                      json.dumps(dl[1]['iofile']),
			                      json.dumps(dl[1]['pcfile']),
			                      json.dumps(dl[1]['amfile']),
			                      num1, num2, num3,
			                      dl[1]['asmd'],
			                      dl[1]['cpname'],
			                      dl[1]['city'],
			                      dl[1]['plurl'],
                                  json.dumps(dl[1]['aifile'])))
			db.commit()
		cursor.close()
		db.close()

	def insert_city_data(self):
		db = CommonTool.db_mysql_connect()
		cursor = db.cursor()
		sql_c = u"""
                insert into T_CITY_CARTONOCCUPATIONRATIO_DATA (startdate, 
                province, citycode, Successfulplaybackrate, Terminalnumber)VALUES 
                ('%s', '%s', '%s', %s, %s)
            """
		sql_e = u"""
                        insert into T_CITY_EPGSUCCESSRATE_DATA (startdate, 
                        province, citycode, Successfulplaybackrate, Terminalnumber) VALUES 
                        ('%s', '%s',' %s', %s, %s)
                    """
		sql_s = u"""
                        insert into T_CITY_SUCCESSFULPLAYBACKRATE_DATA (startdate, 
                        province, citycode, Successfulplaybackrate, Terminalnumber)VALUES 
                        ('%s', '%s', '%s', %s, %s)
                    """
		for i in self.__city_data().items():
			if i[1]['pt'] == 0:
				num1 = 'null'
			else:
				num1 = i[1]['st'] / i[1]['pt']
			if i[1]['et'] == 0:
				num2 = 'null'
			else:
				num2 = i[1]['ert'] / i[1]['et']
			if i[1]['pc'] == 0:
				num3 = 'null'
			else:
				num3 = i[1]['psc'] / i[1]['pc']

			cursor.execute(sql_c % (self.date, self.city, i[0],
			                        num1, i[1]['nbs']))

			cursor.execute(sql_e % (self.date, self.city, i[0],
			                        num2, i[1]['nbs']))

			cursor.execute(sql_s % (self.date, self.city, i[0],
			                        num3, i[1]['nbs']))
			db.commit()
		cursor.close()
		db.close()

	def insert_cpname_data(self):
		db = CommonTool.db_mysql_connect()
		cursor = db.cursor()
		sql_c = u"""
                insert into T_CPNAME_CARTONOCCUPATIONRATIO_DATA (startdate, 
                province, cpname, Successfulplaybackrate, Terminalnumber) VALUES 
                ('%s', '%s', '%s', %s, %s)
            """
		sql_e = u"""
                        insert into T_CPNAME_EPGSUCCESSRATE_DATA (startdate, province, 
                        cpname, Successfulplaybackrate, Terminalnumber) VALUES 
                        ('%s', '%s', '%s', %s, %s)
                    """
		sql_s = u"""
                        insert into T_CPNAME_SUCCESSFULPLAYBACKRATE_DATA (startdate, province,
                         cpname, Successfulplaybackrate, Terminalnumber) VALUES 
                        ('%s', '%s', '%s', %s, %s)
                    """
		for i in self.__cpname_data().items():
			if i[1]['pt'] == 0:
				num1 = 'null'
			else:
				num1 = i[1]['st'] / i[1]['pt']
			if i[1]['et'] == 0:
				num2 = 'null'
			else:
				num2 = i[1]['ert'] / i[1]['et']
			if i[1]['pc'] == 0:
				num3 = 'null'
			else:
				num3 = i[1]['psc'] / i[1]['pc']
			cursor.execute(sql_c % (self.date, self.city, i[0],
			                        num1, i[1]['nbs']))

			cursor.execute(sql_e % (self.date, self.city, i[0],
			                        num2, i[1]['nbs']))
			
			cursor.execute(sql_s % (self.date, self.city, i[0],
			                        num3, i[1]['nbs']))
			db.commit()
		cursor.close()
		db.close()

	def insert_modle_data(self):
		db = CommonTool.db_mysql_connect()
		cursor = db.cursor()
		sql_c = u"""
                insert into T_DEVICEID_CARTONOCCUPATIONRATIO_DATA (startdate, province,
                deviceid, Successfulplaybackrate, Terminalnumber) VALUES 
                ('%s', '%s', '%s', %s, %s)
            """
		sql_e = u"""
                        insert into T_DEVICEID_EPGSUCCESSRATE_DATA (startdate, province, 
                        deviceid, Successfulplaybackrate, Terminalnumber) VALUES 
                        ('%s', '%s', '%s', %s, %s)
                    """
		sql_s = u"""
                        insert into T_DEVICEID_SUCCESSFULPLAYBACKRATE_DATA (startdate, province, 
                        deviceid, Successfulplaybackrate, Terminalnumber) VALUES 
                        ('%s', '%s', '%s', %s, %s)
                    """

		for i in self.__modle_data().items():
			if i[1]['pt'] == 0:
				num1 = 'null'
			else:
				num1 = i[1]['st'] / i[1]['pt']
			if i[1]['et'] == 0:
				num2 = 'null'
			else:
				num2 = i[1]['ert'] / i[1]['et']
			if i[1]['pc'] == 0:
				num3 = 'null'
			else:
				num3 = i[1]['psc'] / i[1]['pc']
			cursor.execute(sql_c % (self.date, self.city, i[0],
			                        num1, i[1]['nbs']))

			cursor.execute(sql_e % (self.date, self.city, i[0],
			                        num2, i[1]['nbs']))

			cursor.execute(sql_s % (self.date, self.city, i[0],
			                        num3, i[1]['nbs']))
			db.commit()
		cursor.close()
		db.close()

	def insert_asmd_data(self):
		db = CommonTool.db_mysql_connect()
		cursor = db.cursor()
		sql_c = u"""
                insert into T_ACCESSMETHOD_CARTONOCCUPATIONRATIO_DATA (startdate, province, 
                accessmethod, Successfulplaybackrate, Terminalnumber) VALUES 
                ('%s', '%s', '%s', %s, %s)
            """
		sql_e = u"""
                        insert into T_ACCESSMETHOD_EPGSUCCESSRATE_DATA (startdate, province, 
                        accessmethod, Successfulplaybackrate, Terminalnumber) VALUES 
                        ('%s', '%s', '%s', %s, %s)
                    """
		sql_s = u"""
                        insert into T_ACCESSMETHOD_SUCCESSFULPLAYBACKRATE_DATA (startdate, province, 
                        accessmethod, Successfulplaybackrate, Terminalnumber) VALUES 
                        ('%s', '%s', '%s', %s, %s)
                    """
		for i in self.__asmd_data().items():
			if i[1]['pt'] == 0:
				num1 = 'null'
			else:
				num1 = i[1]['st'] / i[1]['pt']
			if i[1]['et'] == 0:
				num2 = 'null'
			else:
				num2 = i[1]['ert'] / i[1]['et']
			if i[1]['pc'] == 0:
				num3 = 'null'
			else:
				num3 = i[1]['psc'] / i[1]['pc']
			cursor.execute(sql_c % (self.date, self.city, i[0],
			                        num1, i[1]['nbs']))

			cursor.execute(sql_e % (self.date, self.city, i[0],
			                        num2, i[1]['nbs']))

			cursor.execute(sql_s % (self.date, self.city, i[0],
			                        num3, i[1]['nbs']))
			db.commit()
		cursor.close()
		db.close()

	def __city_data(self):
		sn_city = dict()
		con = 1
		for i in self.data.items():
			if i[1]['city'] not in sn_city.keys():
				sn_city[i[1]['city']] = {'sn': [i[0]],
				                         'nbs': con,
				                         'psc': i[1]['psc'],
				                         'pc': i[1]['pc'],
				                         'st': i[1]['st'],
				                         'pt': i[1]['pt'],
				                         'ert': i[1]['ert'],
				                         'et': i[1]['et']}
			else:
				fid = sn_city[i[1]['city']]['sn']
				fid.append(i[0])
				sn_city[i[1]['city']].update({'sn': fid})
				sn_city[i[1]['city']].update({'nbs': sn_city[i[1]['city']]['nbs'] + 1})
				sn_city[i[1]['city']].update({'psc': sn_city[i[1]['city']]['psc'] + i[1]['psc']})
				sn_city[i[1]['city']].update({'pc': sn_city[i[1]['city']]['pc'] + i[1]['pc']})
				sn_city[i[1]['city']].update({'st': sn_city[i[1]['city']]['st'] + i[1]['st']})
				sn_city[i[1]['city']].update({'pt': sn_city[i[1]['city']]['pt'] + i[1]['pt']})
				sn_city[i[1]['city']].update({'ert': sn_city[i[1]['city']]['ert'] + i[1]['ert']})
				sn_city[i[1]['city']].update({'et': sn_city[i[1]['city']]['et'] + i[1]['et']})

		return sn_city

	def __cpname_data(self):
		sn_city = dict()
		con = 1
		for i in self.data.items():
			if i[1]['cpname'] not in sn_city.keys():
				sn_city[i[1]['cpname']] = {'sn': [i[0]],
				                           'nbs': con,
				                           'psc': i[1]['psc'],
				                           'pc': i[1]['pc'],
				                           'st': i[1]['st'],
				                           'pt': i[1]['pt'],
				                           'ert': i[1]['ert'],
				                           'et': i[1]['et']}
			else:
				fid = sn_city[i[1]['cpname']]['sn']
				fid.append(i[0])
				sn_city[i[1]['cpname']].update({'sn': fid})
				sn_city[i[1]['cpname']].update({'nbs': sn_city[i[1]['cpname']]['nbs'] + 1})
				sn_city[i[1]['cpname']].update({'psc': sn_city[i[1]['cpname']]['psc'] + i[1]['psc']})
				sn_city[i[1]['cpname']].update({'pc': sn_city[i[1]['cpname']]['pc'] + i[1]['pc']})
				sn_city[i[1]['cpname']].update({'st': sn_city[i[1]['cpname']]['st'] + i[1]['st']})
				sn_city[i[1]['cpname']].update({'pt': sn_city[i[1]['cpname']]['pt'] + i[1]['pt']})
				sn_city[i[1]['cpname']].update({'ert': sn_city[i[1]['cpname']]['ert'] + i[1]['ert']})
				sn_city[i[1]['cpname']].update({'et': sn_city[i[1]['cpname']]['et'] + i[1]['et']})

		return sn_city

	def __modle_data(self):
		sn_city = dict()
		con = 1
		for i in self.data.items():
			if i[1]['modle'] not in sn_city.keys():
				sn_city[i[1]['modle']] = {'sn': [i[0]],
				                          'nbs': con,
				                          'psc': i[1]['psc'],
				                          'pc': i[1]['pc'],
				                          'st': i[1]['st'],
				                          'pt': i[1]['pt'],
				                          'ert': i[1]['ert'],
				                          'et': i[1]['et']}
			else:
				fid = sn_city[i[1]['modle']]['sn']
				fid.append(i[0])
				sn_city[i[1]['modle']].update({'sn': fid})
				sn_city[i[1]['modle']].update({'nbs': sn_city[i[1]['modle']]['nbs'] + 1})
				sn_city[i[1]['modle']].update({'psc': sn_city[i[1]['modle']]['psc'] + i[1]['psc']})
				sn_city[i[1]['modle']].update({'pc': sn_city[i[1]['modle']]['pc'] + i[1]['pc']})
				sn_city[i[1]['modle']].update({'st': sn_city[i[1]['modle']]['st'] + i[1]['st']})
				sn_city[i[1]['modle']].update({'pt': sn_city[i[1]['modle']]['pt'] + i[1]['pt']})
				sn_city[i[1]['modle']].update({'ert': sn_city[i[1]['modle']]['ert'] + i[1]['ert']})
				sn_city[i[1]['modle']].update({'et': sn_city[i[1]['modle']]['et'] + i[1]['et']})

		return sn_city

	def __asmd_data(self):
		sn_city = dict()
		con = 1
		for i in self.data.items():
			if i[1]['asmd'] not in sn_city.keys():
				sn_city[i[1]['asmd']] = {'sn': [i[0]],
				                         'nbs': con,
				                         'psc': i[1]['psc'],
				                         'pc': i[1]['pc'],
				                         'st': i[1]['st'],
				                         'pt': i[1]['pt'],
				                         'ert': i[1]['ert'],
				                         'et': i[1]['et']}
			else:
				fid = sn_city[i[1]['asmd']]['sn']
				fid.append(i[0])
				sn_city[i[1]['asmd']].update({'sn': fid})
				sn_city[i[1]['asmd']].update({'nbs': sn_city[i[1]['asmd']]['nbs'] + 1})
				sn_city[i[1]['asmd']].update({'psc': sn_city[i[1]['asmd']]['psc'] + i[1]['psc']})
				sn_city[i[1]['asmd']].update({'pc': sn_city[i[1]['asmd']]['pc'] + i[1]['pc']})
				sn_city[i[1]['asmd']].update({'st': sn_city[i[1]['asmd']]['st'] + i[1]['st']})
				sn_city[i[1]['asmd']].update({'pt': sn_city[i[1]['asmd']]['pt'] + i[1]['pt']})
				sn_city[i[1]['asmd']].update({'ert': sn_city[i[1]['asmd']]['ert'] + i[1]['ert']})
				sn_city[i[1]['asmd']].update({'et': sn_city[i[1]['asmd']]['et'] + i[1]['et']})

		return sn_city
