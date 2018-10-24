# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def huawei():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = 'http://consumer.huawei.com/support/services/service/parts/product/list'
    url2 = 'http://consumer.huawei.com/support/services/service/parts/list'
    wrong_arr = ['None']
    try:
        js1 = hhnetworm.getRes(url1, result='j',
                               data={'json': 'jQuery111308920180139684155_1508484428667', 'productId': 4903, '_': 1508484428671, 'siteCode': 'cn'})
        for aa in js1:

            js2 = hhnetworm.getRes(url2, result='j',
                                   data={'json': 'jQuery111308920180139684155_1508484428667', 'productCode': aa['productCode'], '_': 1508484428672,
                                         'siteCode': 'cn'})
            for bb in js2:
                price = str(bb['price']).replace("￥", '')
                if price not in wrong_arr:
                    dic = {
                        'business': '官修',
                        'brand': '华为',
                        'type': '手机',
                        'model': aa['productTypeName'],
                        'color': '',
                        'malfunction': bb['partsType'],
                        'plan': '',
                        'price': price,
                    }
                    rt_arr.append(dic)
                    print(dic)
        HhTime.costPrinter(st_time, pjName='华为', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('华为'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


huawei()
