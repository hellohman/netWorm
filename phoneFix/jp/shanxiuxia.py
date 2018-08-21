# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

def shanxiuxia():
	st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
	url1 = 'http://api.shanxiuxia.com/api/PhoneType/brand'
	url2 = 'http://api.shanxiuxia.com/api/PhoneType/brandPhone'
	url3 = 'http://api.shanxiuxia.com/api/PhoneType/malclass'
	url4 = 'http://api.shanxiuxia.com/api/PhoneType/maldetails'
	try:
		js1 = hhnetworm.getRes(url1,method='p',result='j')
		js2 = hhnetworm.getRes(url2,method='p',result='j')
		for aa in js2['data']:

			js3 = hhnetworm.getRes(url3,method='p',result='j',data={'id':aa['id']})
			for bb in js3['data']['malfunction']:
				js4 = hhnetworm.getRes(url4,method='p',result='j',data={'id':aa['id'],'type_id':bb['id']})
				for cc in js4['data']:
					for dd in js1['data']:
						if aa['brand_id'] == dd['id']:
							dic = {
							'business': '闪修侠',
							'brand': dd['name'],
							'type': aa['category'],
							'model': aa['name'],
							'color': aa['color'],
							'malfunction': cc['malfunction'],
							'plan': '',
							'price': cc['price_reference'],
							}
							rt_arr.append(dic)
							print(dic)
							break
		HhTime.costPrinter(st_time,pjName='闪修侠',dataArr=rt_arr)
		finish = True
	except:
		print("----------Wrong: {}".format('闪修侠'))
		traceback.print_exc()
	finally: return rt_arr if finish else []

shanxiuxia()