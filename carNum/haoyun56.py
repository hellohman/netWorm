# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

# 车牌归属地 - haoyun56

def haoyun56():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = 'http://www.haoyun56.com/xue/chepaihao/'
    try:
        sel1 = hhnetworm.getRes(url1)
        for aa in sel1.css("#dlProvince tr td div a"):
            pro = aa.css("::text").extract_first().strip()

            sel2 = hhnetworm.getRes(url1+"?province={}".format(aa.css("::attr(href)").extract_first()[-6:]))
            for bb in sel2.css("#div_Provice table tr:nth-child(n+2)"):
                dic = {
                    'source': 'haoyun56',
                    "province":pro,
                    "city":bb.css("td:nth-child(2) a::text").extract_first().strip(),
                    "code":bb.css("td:nth-child(3)::text").extract_first().strip()
                }
                rt_arr.append(dic)
                print(dic)
        HhTime.costPrinter(st_time,pjName='haoyun56')
        finish = True
    except:
        print("----------Wrong: {}".format('haoyun56'))
        traceback.print_exc()
    finally: return dlData_haoyun56(rt_arr) if finish else []

def dlData_haoyun56(array):
    rt_arr, keys = [], ['province','city','code']
    for each in array:
        for key in keys: each[key] = each[key].strip().upper()
        each['code'] = each['code'].replace("……",",")
        for aa in each['code'].split(mark=','):
            dic = {'source':each['source'],'province':each['province'],'city':each['city'],'code':aa}
            if dic not in rt_arr: rt_arr.append(dic)
    return rt_arr

haoyun56()