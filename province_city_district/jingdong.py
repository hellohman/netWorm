# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

# 京东地址库

def jingdong():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "http://psfw.jd.com/help/front/initArea.do?"
    url2 = "http://psfw.jd.com/help/front/initCity.do"
    url3 = "http://psfw.jd.com/help/front/initArea.do"
    url4 = "http://psfw.jd.com/help/front/initFouth.do"
    try:
        js1 = hhnetworm.getRes(url1,method='p',result='j')
        for aa in js1['result']['resultList']:
            province, province_id = aa['name'], str(aa['id'])

            js2 = hhnetworm.getRes(url2,method='p',data={'provinceId':province_id},result='j')
            for bb in js2['result']['resultList']:
                city, city_id = bb['name'], str(bb['id'])

                js3 = hhnetworm.getRes(url3,method='p',result='j',data={'provinceId':province_id,'cityId':city_id})
                for cc in js3['result']['resultList']:
                    district, district_id = cc['name'], str(cc['id'])

                    js4 = hhnetworm.getRes(url4,method='p',result='j',data={'provinceId':province_id,'cityId':city_id,'areaId':district_id})
                    if js4['result']['hasNext']:
                        for dd in js4['result']['resultList']:
                            dic = {'province':province,'city':city,'district':district,'area':dd['name']}
                            rt_arr.append(dic)
                            print(dic)
                    else:
                        dic = {'province':province,'city':city,'district':district,'area':''}
                        rt_arr.append(dic)
                        print(dic)
        HhTime.costPrinter(st_time,pjName='京东地址库',dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('京东地址库'))
        traceback.print_exc()
    finally: return rt_arr if finish else []

jingdong()