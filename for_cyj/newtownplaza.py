# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel


def newtownplaza():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "https://www.newtownplaza.com.hk/zh-hans/"
    try:
        for zz, sort in zip(['shopping', 'dining'], ['购物', '美食']):
            sel1 = hhnetworm.getRes(url1 + zz)
            for aa in sel1.css("#shop-list > div.shop-list__list-holder.is-active > div > div.js-view-dom-id-35927955eb4bf75ba622622041b61868f0e65b17a25f5b85a3bec88ec4ab6594.shop-hidden-filter > a"):
                data = deal_arr(aa.css("::text").extract())
                dic = {
                    '店名': data[0],
                    '位置': data[1],
                    '营业时间': data[2] if len(data) >= 3 else '',
                    '电话': data[3] if len(data) == 4 else ''
                }
                print(dic)
                rt_arr.append(dic)
        HhTime.costPrinter(st_time, pjName='VCity', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('VCity'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []

def deal_arr(arr):
    rt_arr = []
    for aa in arr:
        aa = aa.replace('\n', '').replace('\t', '').replace(' ', '')
        if aa:
            rt_arr.append(aa)
    return rt_arr


this_data = newtownplaza()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\新城市广场_一期_三期.xlsx', [{'sheetName': '新城市广场_一期_三期', 'fields': ['店名', '位置', '营业时间', '电话'], 'data': this_data}])
