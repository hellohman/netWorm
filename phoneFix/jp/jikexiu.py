# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def jikexiu():
	st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
	url1 = 'https://www.jikexiu.com/common/brands.json'
	url2 = 'https://www.jikexiu.com/order/selSolution'
	url3 = 'https://www.jikexiu.com/order/getDeviceAttributeList.json'
	url4 = 'https://www.jikexiu.com/order/getDeviceSolution.json'
	url5 = 'https://www.jikexiu.com/order/getSolutionMalfunction.json'
	try:
		js1 = hhnetworm.getRes(url1,method='p',result='j')
		for aa in js1['brandList']:

			sel2 = hhnetworm.getRes(url2,data={'brandId':aa['id'],'categoryId':12})
			for bb in sel2.css("#selectDevice ul li"):
				color = ''

				attributeId, color_id = '', ''
				js3 = hhnetworm.getRes(url3,method='p',result='j',data={'deviceId':bb.css("::attr(deviceid)").extract_first()})
				for cc in js3['deviceAttributeList']:
					color += cc['attributeValue'] + ","							# 颜色
					attributeId, color_id = cc['attributeId'], cc['id']

				js4 = hhnetworm.getRes(url4,method='p',result='j',data={'attrs[0].attributeId':attributeId,'attrs[0].valueId':color_id,'deviceId':bb.css("::attr(deviceid)").extract_first()})
				for dd in js4['malfunctionList']:

					js5 = hhnetworm.getRes(url5,method='p',result='j',data={'attrs[0].attributeId':attributeId,'attrs[0].valueId':color_id,'deviceId':bb.css("::attr(deviceid)").extract_first(),'malfunctionId':dd['id']})
					for ee in js5['solutionMalfunctionList']:
						dic = {
							'business': '极客修',
							'brand': aa['name'],
							'type': '手机',
							'model': bb.css("::text").extract_first(),
							'color': color[:-1],
							'malfunction': dd['name'],
							'plan': ee['method'],
							'price': ee['price'],
						}
						rt_arr.append(dic)
						print(dic)
		HhTime.costPrinter(st_time,pjName='极客修',dataArr=rt_arr)
		finish = True
	except:
		print("----------Wrong: {}".format('极客修'))
		traceback.print_exc()
	finally: return rt_arr if finish else []

jikexiu()