# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

def jinli():
	st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
	url1 = 'https://www.gionee.com/id-478_op-productPart.shtml'
	url2 = 'https://www.gionee.com/'
	wrong_arr = ['one', '智能机']
	try:
		sel1 = hhnetworm.getRes(url1)
		for aa in sel1.css(".xl_phone a"):

			sel2 = hhnetworm.getRes(url2 + aa.css("::attr('href')").extract_first())
			for bb in sel2.css(".peijian_list li"):

				sel3 = hhnetworm.getRes(url2 + bb.css("bt a::attr('href')").extract_first())
				for cc in sel3.xpath("//table[@class='MsoNormalTable']/tbody/tr[position()>2 and position()<last()]"):
					price = str(cc.css("td:nth-child(2) p span span::text").extract_first()).strip() if cc.css("td:nth-child(2) p span span::text").extract_first() else str(cc.css("td:nth-child(2) p span::text").extract_first())[1:].strip()
					price = price.strip().replace('￥','').replace(',','')
					if price and price not in wrong_arr:
						dic = {
						'business': '官修',
						'brand': '金立',
						'type': '手机',
						'model': bb.css("bt a::text").extract_first(),
						'color': '',
						'malfunction': str(cc.css("td:nth-child(1) p span::text").extract_first()).strip(),
						'plan': '',
						'price': price,
						}
						rt_arr.append(dic)
						print(dic)
		HhTime.costPrinter(st_time,pjName='金立',dataArr=rt_arr)
		finish = True
	except:
		print("----------Wrong: {}".format('金立'))
		traceback.print_exc()
	finally: return rt_arr if finish else []

jinli()