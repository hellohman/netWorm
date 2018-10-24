# coding=utf-8
import json
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def xiaomi():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = 'https://www.mi.com/service/materialprice/'
    try:
        sel1 = hhnetworm.getRes(url1, result='t-s')
        text = sel1.css("body script:nth-child(3)").extract_first()
        js1 = json.loads(text[text.find("=") + 1:text.find("</script>")])
        for aa in js1:
            for bb in aa['child']:
                if 'child' in bb.keys():
                    try:
                        for cc in bb['child']: rt_arr.append(dicMaker(cc))
                    except:
                        for cc in bb['child']:
                            for dd in cc['child']: rt_arr.append(dicMaker(dd))
                else:
                    try:
                        rt_arr.append(dicMaker(bb))
                    except:
                        print(bb['child'])
        HhTime.costPrinter(st_time, pjName='小米', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('小米'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


def dicMaker(data):
    rt_dic = {
        'business': '官修',
        'brand': '小米',
        'type': '手机',
        'model': data['priceArr']['modelName'],
        'color': '',
        'malfunction': data['priceArr']['partName'],
        'plan': '',
        'price': str(data['priceArr']['partPrice'] + data['priceArr']['manualRepairPrice']),
    }
    print(rt_dic)
    return rt_dic


xiaomi()
