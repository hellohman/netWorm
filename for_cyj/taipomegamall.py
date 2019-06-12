# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel


def taipomegamall():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "https://taipomegamall.shkp.com/tc/"
    try:
        for zz, sort in zip(['shoppingall.php', 'dining.php?zone=ALL'], ['商店', '美食']):
            sel1 = hhnetworm.getRes(url1 + zz)
            for aa in sel1.css("#main > div.content > div.shop_item > div > a"):
                sel2 = hhnetworm.getRes(url1 + aa.css("::attr(href)").extract_first())
                for bb in sel2.css("#zoom_container > div.landmarks > div > div > div > ul"):
                    data = bb.css("li::text").extract()
                    dic = {
                        '类型': sort,
                        '店名': data[0].replace('\n', '').replace('\t', ''),
                        '商铺号': data[2].replace('店號 :', '').replace('\n', '').replace('\t', ''),
                        '区域': data[3].replace('Zone :', '').replace('\n', '').replace('\t', ''),
                        '电话': data[4].replace('電話 :', '').replace('\n', '').replace('\t', ''),
                        '营业时间': data[5].replace('營業時間 : ', '').replace('\n', '').replace('\t', '')
                    }
                    print(dic)
                    rt_arr.append(dic)
        HhTime.costPrinter(st_time, pjName='大埔超级城', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('大埔超级城'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []

this_data = taipomegamall()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\大埔超级城.xlsx', [{'sheetName': '大埔超级城', 'fields': ['类型', '店名', '商铺号', '区域', '电话', '营业时间'], 'data': this_data}])
