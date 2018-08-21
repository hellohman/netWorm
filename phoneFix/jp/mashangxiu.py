# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def mashangxiu():
	st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
	url1 = 'https://www.mashangxiu.com/repair/repair'
	url2 = 'https://www.mashangxiu.com/device/acquireDeviceByBrandName'
	url3 = 'https://www.mashangxiu.com/device/acquireDeviceByBrandAndModel'
	try:
		sel1 = hhnetworm.getRes(url1)
		for aa in sel1.css(".mobileNav ul li a::attr('id')").extract():

			js2 = hhnetworm.getRes(url2,result='j',data={'needColor':'Y','productBrand':aa})
			for bb in js2['modelList']:

				js3 = hhnetworm.getRes(url3,result='j',data={'needColor':'Y','productBrand':aa,'productModel':bb})
				for cc in js3['materialTypeList']:
					dic = {
						'business': '马上修',
						'brand': aa,
						'type': '手机',
						'model': bb,
						'color': '',
						'malfunction': cc['materialName'],
						'plan': '',
						'price': cc['outerFee'],
					}
					rt_arr.append(dic)
					print(dic)
		HhTime.costPrinter(st_time,pjName='马上修',dataArr=rt_arr)
		finish = True
	except:
		print("----------Wrong: {}".format('马上修'))
		traceback.print_exc()
	finally: return rt_arr if finish else []

mashangxiu()