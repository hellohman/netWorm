# coding=utf-8
import json
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def jihouhou():
	st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
	url1 = 'http://www.hohofast.com/api/web/order/create'
	url2 = "http://www.hohofast.com/api/web/brand/list"
	url3 = "http://www.hohofast.com/api/web/model/list"
	url4 = "http://www.hohofast.com/api/web/model/submit"
	url5 = "http://www.hohofast.com/api/web/order/other"
	url6 = "http://www.hohofast.com/api/web/order/otherSubmit"
	url7 = "http://www.hohofast.com/api/web/brief/appraisement/data"
	try:
		sel1 = hhnetworm.getRes(url1,method='p')
		for aa in sel1.css("#select_brand div"):
			brand_id = aa.css("::attr(data-brand)").extract_first()

			js2 = hhnetworm.getRes(url2,method='p',data={'uuid':brand_id},result='j')
			for bb in js2['items']:

				js3 = hhnetworm.getRes(url3,data={'type':brand_id,'uuid':bb['uuid']},result='j')
				for cc in js3['items']:

					color, color_id = '', ''
					for dd in json.loads(cc['info'])['colors']:
						color += dd['color'] + ","             										  # 颜色
						color_id = dd['uuid']

					hhnetworm.getRes(url4,method='p',data={'type':brand_id,'bUuid':bb['uuid'],'mUuid':cc['uuid'],'color':color_id})
					sel5 = hhnetworm.getRes(url5)

					for ee in sel5.css("#select_part div.item.malfunction-item"):

						hhnetworm.getRes(url6,method='p',data={'part':ee.css("::attr(data-part)").extract_first(),'service':1})
						js7 = hhnetworm.getRes(url7,result='j')

						js7 = js7['data']['commonTechItems']
						if js7:
							dic = {
							'business': '极吼吼',
							'brand': aa.css("::attr(data-name)").extract_first(),
							'type': bb['name'],
							'model': cc['name'],
							'color': color[:-1],
							'malfunction': ee.css("h5::text").extract_first(),
							'plan': js7[0]['solution']['showname'],
							'price': js7[0]['price'],
							}
							rt_arr.append(dic)
							print(dic)
		HhTime.costPrinter(st_time,pjName='极吼吼',dataArr=rt_arr)
		finish = True
	except:
		print("----------Wrong: {}".format('极吼吼'))
		traceback.print_exc()
	finally: return rt_arr if finish else []

jihouhou()