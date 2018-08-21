# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

# 车牌归属地 - tcmap

def tcmap():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "http://www.tcmap.com.cn/list/car_list.html"
    try:
        # 除 上海 海南 重庆 新疆 青海
        sel1 = hhnetworm.getRes(url1)
        for aa in sel1.css("#list360 table"):
            pro = aa.css("tr:nth-child(1) td:nth-child(1) strong a::text").extract_first()

            for bb in aa.css("tr:nth-child(n+2)"):
                dic = {
                    'source':'tcmap',
                    "province":pro,
                    "city":bb.css("td:nth-child(1) a::text").extract_first(),
                    "code":bb.css("td:nth-child(2)::text").extract_first()
                }
                rt_arr.append(dic)
                print(dic)
        HhTime.costPrinter(st_time,pjName='tcmap')
        finish = True
    except:
        print("----------Wrong: {}".format('tcmap'))
        traceback.print_exc()
    finally: return dlData_tcmap(rt_arr) if finish else []

def dlData_tcmap(array):
    rt_arr, keys = [], ['province','city','code']
    for each in array:
        for key in keys: each[key] = each[key].strip().upper()
        if each['code'] and len(each['code']) != 1 and each not in rt_arr: rt_arr.append(each)
    return rt_arr

tcmap()