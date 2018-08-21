# coding=utf-8
import json
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def hiweixiu():
	st_time, n, rt_arr, finish, hhnetworm = time.time(), 0, [], False, HhNetworm()
	url1 = 'https://www.hiweixiu.com/step/selectInfo'
	url2 = 'https://www.hiweixiu.com/step/getMouldlistsByBrandid'
	url3 = 'https://www.hiweixiu.com/step/detailInfo'
	try:
		sel1 = hhnetworm.getRes(url1)
		for aa in sel1.css("div.brand_list ul li"):
			brand = aa.css("a::text").extract_first().strip()

			js2 = hhnetworm.getRes(url2,result='j',data={'brand_id':aa.css("::attr(data-id)").extract_first()})['data']['mould']
			for key in js2.keys():
				for bb in js2[key]:

					sel3 = hhnetworm.getRes(url3,data={'mid':bb['MouldId']})

					rp_info = json.loads(sel3.css("input.rp_info::attr(value)").extract_first())
					for cc in rp_info.keys():
						for dd in rp_info[cc].keys():
							for ee in rp_info[cc][dd].keys():
								data = rp_info[cc][dd][ee]
								dic = {
								'business': 'Hi维修',
								'brand': brand,
								'type': bb['ProductName'],
								'model': bb['MouldName'],
								'color': data['ColorName'].replace("/",","),
								'malfunction': data['faulttype_detail_name'],
								'plan': data['RepairType'],
								'price': data['Price'],
								}
								rt_arr.append(dic)
								print(dic)
		HhTime.costPrinter(st_time,pjName='Hi维修',dataArr=rt_arr)
		finish = True
	except:
		print("----------Wrong: {}".format('Hi维修'))
		traceback.print_exc()
	finally: return rt_arr if finish else []

hiweixiu()