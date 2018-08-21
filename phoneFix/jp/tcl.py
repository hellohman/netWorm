# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

def tcl():
	st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
	url1 = 'http://wechat-api.tclsfdj.com:88/ha-wechat/v1/repair/brands'
	url2 = 'http://wechat-api.tclsfdj.com:88/ha-wechat/v1/repair/models/%s'
	url3 = 'http://wechat-api.tclsfdj.com:88/ha-wechat/v1/repair/colours/%s'
	url4 = 'http://wechat-api.tclsfdj.com:88/ha-wechat/v1/repair/material/%s'
	url5 = 'http://wechat-api.tclsfdj.com:88/ha-wechat/v1/repair/fault/%s'
	try:
		js1 = hhnetworm.getRes(url1,method='p',result='j')
		for aa in js1['data']:
			if aa['brandName'] != '其它':

				js2 = hhnetworm.getRes(url2 % aa['brandId'],result='j')
				for bb in js2['data']:
					color = ''

					js3 = hhnetworm.getRes(url3 % bb['modelId'],method='p',result='j')
					for each in js3['data']:
						color += each['colourName'] + ","

					js4 = hhnetworm.getRes(url4 % js3['data'][0]['colourId'],method='p',result='j')
					for cc in js4['data']:

						js5 = hhnetworm.getRes(url5 % bb['modelId'],method='p',result='j')
						for dd in js5['data']['faultInfo']:
							if cc['faultId'] == dd['faultId']:
								dic = {
								'business': 'TCL',
								'brand': aa['brandName'],
								'type': '手机',
								'model': bb['mobileName'],
								'color': color[:-1],
								'malfunction': dd['faultName'],
								'plan': dd['faultPlan'],
								'price': cc['price'],
								}
								rt_arr.append(dic)
								print(dic)
		HhTime.costPrinter(st_time,pjName='tcl',dataArr=rt_arr)
		finish = True
	except:
		print("----------Wrong: {}".format('tcl'))
		traceback.print_exc()
	finally: return rt_arr if finish else []

tcl()