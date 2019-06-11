# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel


def VCity():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "http://www.vcity.com.hk/tch/shop/search.do"
    try:
        sel1 = hhnetworm.getRes(url1)
        for aa in sel1.css("#thisForm div.main_content table tr:nth-child(n+2)"):
            dic = {
                '店名': aa.css("td:nth-child(1) a::text").extract_first().replace('\r\n\t\t\t\t\t           \t\t\t', ''),
                '分类': aa.css("td:nth-child(2)::text").extract()[1],
                '编号': aa.css("td:nth-child(3) a::text").extract_first().replace(' \r\n\t\t\t\t\t           \t\t\t', ''),
                '楼层': aa.css("td:nth-child(4)::text").extract_first().strip()
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



this_data = VCity()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\VCity.xlsx', [{'sheetName': 'VCity', 'fields': ['分类', '店名', '编号', '楼层'], 'data': this_data}])
