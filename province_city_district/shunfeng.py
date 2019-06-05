# coding=utf-8
import time
import traceback

from zzz_lib.HhExcel import HhExcel
from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


# 顺丰地址库

def shunfeng():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "http://www.sf-express.com/sf-service-owf-web/service/region/A000086000/subRegions"
    url2 = "http://www.sf-express.com/sf-service-owf-web/service/region/%s/subRegions"
    try:
        js1 = hhnetworm.getRes(url1, data={'lang': 'sc'}, result='j')
        for aa in js1:
            province = aa['name']

            js2 = hhnetworm.getRes(url2 % str(aa['code']), data={'level': 2, 'lang': 'sc'}, result='j')
            for bb in js2:
                city = bb['name']

                if str(bb['level']).strip() == "4":
                    dic = {'province': province, 'city': city, 'district': ''}
                    rt_arr.append(dic)
                    print(dic)
                else:
                    js3 = hhnetworm.getRes(url2 % str(bb['code']), data={'level': 3, 'lang': 'sc', 'region': 'cn'}, result='j')
                    for cc in js3:
                        dic = {'province': province, 'city': city, 'district': cc['name']}
                        rt_arr.append(dic)
                        print(dic)
        HhTime.costPrinter(st_time, pjName='顺丰地址库', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('顺丰地址库'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


this_data = shunfeng()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\za-huanghai\Desktop\xxx.xlsx', [{'sheetName': 'xxx', 'fields': ['province', 'city', 'district'], 'data': this_data}])
