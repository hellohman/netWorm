# coding=utf-8
import time
import traceback

from parsel import Selector

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

def oppo():
	st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
	url1 = 'https://www.oppo.com/cn/service/part'
	url2 = 'https://www.oppo.com/cn/service/productlist'
	wrong_arr = [' ']
	try:
		sel1 = hhnetworm.getRes(url1)
		for model in sel1.css("#part-select div.select-dropdown ul li span::text").extract():

			js2 = hhnetworm.getRes(url2,data={'isapp':0,'mobile':model},result='j')
			sel2 = Selector(js2['data'])
			for name,price in zip(sel2.css("div.part-list-name span::text").extract(),sel2.css("div.part-list-price::text").extract()[1:]):
				if price not in wrong_arr:
					price = int(float(price.strip().replace('¥','')))
					dic = {
					'business': '官修',
					'brand': 'oppo',
					'type': '手机',
					'model': model,
					'color': '',
					'malfunction': name,
					'plan': '',
					'price': price,
					}
					rt_arr.append(dic)
					print(dic)
		HhTime.costPrinter(st_time,pjName='oppo',dataArr=rt_arr)
		finish = True
	except:
		print("----------Wrong: {}".format('oppo'))
		traceback.print_exc()
	finally: return rt_arr if finish else []

oppo()