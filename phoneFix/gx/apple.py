# coding=utf-8
import time
import traceback

from zzz_lib.HhBase import HhBase
from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def apple():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = 'https://support.apple.com/zh-cn/iphone/repair/service/pricing'
    try:
        sel1 = hhnetworm.getRes(url1)
        for aa in sel1.css("#faq-regular div:nth-child(4) #tableWraper table tr:nth-child(n+2)"):

            model = ''
            for bb in aa.css("td:nth-child(1)::text").extract(): model += bb.strip()

            price = HhBase.toInt(aa.css("td:nth-child(2)::text").extract_first().replace("RMB ", "").replace(",", ""))
            if not price: price = HhBase.toInt(aa.css("td:nth-child(3)::text").extract_first().replace("RMB ", "").replace(",", ""))

            for bb in model.split('、'):
                dic = {
                    'business': '官修',
                    'brand': '苹果',
                    'type': '手机',
                    'model': bb,
                    'color': '',
                    'malfunction': '内屏',
                    'plan': '',
                    'price': price,
                }
                rt_arr.append(dic)
                print(dic)
        HhTime.costPrinter(st_time, pjName='苹果', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('苹果'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


apple()
