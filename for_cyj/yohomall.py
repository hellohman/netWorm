# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel


def yohomall():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "https://www.yohomall.hk/"
    try:
        sel1 = hhnetworm.getRes(url1 + 'sch/dining/DiningList')
        for aa in sel1.css("#allCategories > div > div > div:nth-child(n+2)"):
            url2 = url1 + aa.css("a::attr(href)").extract_first()
            sel2 = hhnetworm.getRes(url2)
            this_ttt = ''
            try:
                this_ttt = sel2.css("#container > div.details-page > div > div.content-wrap > p:nth-child(13)::text").extract_first().strip()
            except: pass
            dic = {
                '店名': sel2.css("#container > div.details-page > div > h2::text").extract_first().strip(),
                '位置': sel2.css("#container > div.details-page > div > div.content-wrap > p:nth-child(3) > a::text").extract_first().strip(),
                '营业时间': sel2.css("#container > div.details-page > div > div.content-wrap > p:nth-child(5)::text").extract_first().strip(),
                '电话': sel2.css("#container > div.details-page > div > div.content-wrap > p:nth-child(7) > a::text").extract_first().strip(),
                '简介': this_ttt,
            }
            print(dic)
            rt_arr.append(dic)
        HhTime.costPrinter(st_time, pjName='YOHO MALL形点', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('YOHO MALL形点'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []

this_data = yohomall()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\YOHO MALL形点.xlsx', [{'sheetName': 'YOHO MALL形点', 'fields': ['店名', '位置', '营业时间', '电话', '简介'], 'data': this_data}])
