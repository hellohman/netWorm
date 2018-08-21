# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

# 手机号码归属地

def haocc():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    try:
        sel1 = hhnetworm.getRes("http://www.51hao.cc/")
        for i,aa in enumerate(sel1.css("div.fkt:nth-child(n+3)"),1):
            province = aa.css("div.fkbj p a::text").extract_first().replace(" ","")
            print("{0} :{1}".format(i,province))

            for url,city in zip(aa.css("div.fklk p a::attr(href)").extract(),aa.css("div.fklk p a::text").extract()):

                sel2 = hhnetworm.getRes(url)
                for bb in sel2.css("div.all ul:nth-child(n+2)"):
                    for number in bb.css("li a::text").extract():
                        number = str(number).replace(" ","")
                        if len(number) == 7:
                            dic = {'province':province,'city':city.replace(" ",""),'number':number}
                            rt_arr.append(dic)
                            print(dic)
                        else: print("错误号码 :",number)

        HhTime.costPrinter(st_time,pjName='手机号码归属地')
        finish = True
    except:
        print("----------Wrong: {}".format('手机号码归属地'))
        traceback.print_exc()
    finally: return rt_arr if finish else []

haocc()