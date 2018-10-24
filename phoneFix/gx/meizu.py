# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def meizu():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = 'https://mwx-api.meizu.com/metter-price/get-cat'
    url2 = 'https://mwx-api.meizu.com/metter-price/get-metter'
    try:
        js1 = hhnetworm.getRes(url1, result='j')
        for aa in js1['data']:

            js2 = hhnetworm.getRes(url2, data={'mobile_cat': {aa['id']}}, result='j')
            for bb in js2['data']:
                price = int(float(bb['price']))
                dic = {
                    'business': '官修',
                    'brand': '魅族',
                    'type': '手机',
                    'model': aa['name'],
                    'color': '',
                    'malfunction': bb['repair_name'],
                    'plan': '',
                    'price': price,
                }
                rt_arr.append(dic)
                print(dic)
        HhTime.costPrinter(st_time, pjName='魅族', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('魅族'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


meizu()
