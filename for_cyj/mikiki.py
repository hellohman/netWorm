# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel


def mikiki():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "http://www.mikiki-mall.com.hk/tc/shopping/shopping_by_cat.php"
    url2 = 'http://www.mikiki-mall.com.hk/tc/dining/dining_shopList.php'
    try:
        sel1 = hhnetworm.getRes(url1)
        print(sel1.css(".paddingtop10px::text").extract())
        # for aa in sel1.css("body > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(1) > table > tr"):
        #     print(aa.css("td span a::text").extract_first())
            # dic = {
            #     '店名': aa.css("td:nth-child(1) a::text").extract_first().replace('\r\n\t\t\t\t\t           \t\t\t', ''),
            #     '分类': aa.css("td:nth-child(2)::text").extract()[1],
            #     '编号': aa.css("td:nth-child(3) a::text").extract_first().replace(' \r\n\t\t\t\t\t           \t\t\t', ''),
            #     '楼层': aa.css("td:nth-child(4)::text").extract_first().strip()
            # }
            # print(dic)
            # rt_arr.append(dic)
        HhTime.costPrinter(st_time, pjName='mikiki', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('mikiki'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []



this_data = mikiki()

# excel_1 = HhExcel()
# excel_1.writer(r'C:\Users\HH\Desktop\Mikiki.xlsx', [{'sheetName': 'Mikiki', 'fields': ['分类', '店名', '编号', '楼层'], 'data': this_data}])
