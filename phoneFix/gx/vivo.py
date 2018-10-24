# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def vivo():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = 'http://www.vivo.com.cn/service/accessory/product/list'
    url2 = "http://www.vivo.com.cn/service/accessory/query"
    try:
        js1 = hhnetworm.getRes(url1, method='p', result='j')
        for aa in js1['data']:

            for bb in aa['products']:

                js2 = hhnetworm.getRes(url2, method='p', data={'productId': bb['id']}, result='j')
                for cc in js2['data']:
                    price = int(float(str(cc['price'])))
                    dic = {
                        'business': '官修',
                        'brand': 'vivo',
                        'type': '手机',
                        'model': bb['name'],
                        'color': '',
                        'malfunction': cc['name'],
                        'plan': '',
                        'price': price,
                    }
                    rt_arr.append(dic)
                    print(dic)
        HhTime.costPrinter(st_time, pjName='vivo', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('vivo'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


vivo()
