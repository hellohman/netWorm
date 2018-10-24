# coding=utf-8
import requests
import time
import traceback

from parsel import Selector

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


# 身份证户籍编号

def tcmap():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "http://www.tcmap.com.cn/list/daima_list.html"
    con_url = "http://www.tcmap.com.cn"
    try:
        sel = hhnetworm.getRes(url1)
        for i, aa in enumerate(sel.css("#list360"), 1):
            province = aa.css("strong a::text").extract_first().replace(" ", "")  # 省
            print("{0} :{1}".format(i, province))

            sel = hhnetworm.getRes(con_url + aa.css("strong a::attr(href)").extract_first())
            for bb in sel.css("#page_left table:nth-child(5) tr:nth-child(n+2)"):
                for cc in bb.css("td:nth-child(6) a::attr(href)").extract():
                    res = requests.get(con_url + str(cc)).content

                    # 编码匹配
                    sel = False
                    try:
                        sel = Selector(res.decode("gb18030"))
                    except:
                        try:
                            sel = Selector(res.decode("utf-8"))
                        except:
                            print("decode all failed!")

                    if sel:
                        for dd in sel.css("#page_left div:nth-child(4) div:nth-child(2) table"):
                            dic = {
                                'province': province,  # 省
                                'id1': aa.css("::text").extract_first().replace(" ", ""),  # 身份证编号1
                                'city': bb.css("td strong a::text").extract_first().replace(" ", ""),  # 市
                                'id2': bb.css("td:nth-child(5)::text").extract_first().replace(" ", ""),  # 身份证编号2
                                'district': dd.css("tr:nth-child(1) td:nth-child(1)::text").extract_first().replace(" ", "")[1:],  # 区
                                'id3': dd.css("tr:nth-child(2) td:nth-child(2)::text").extract_first().replace(" ", "")[1:],  # 身份证编号3
                                'phoneAreaCode': bb.css("td:nth-child(4)::text").extract_first().replace(" ", ""),  # 电话区号
                                'postCode': dd.css("tr:nth-child(3) td:nth-child(2)::text").extract_first().replace(" ", "")[1:],  # 邮政编码
                                'carCode': dd.css("tr:nth-child(4) td:nth-child(1)::text").extract_first().replace(" ", "")[1:],  # 车牌
                                'population': check_1(dd.css("tr:nth-child(5) td:nth-child(1)::text").extract_first()),  # 人口
                                's_area': check_1(dd.css("tr:nth-child(6) td::text").extract_first())  # 区域面积
                            }
                            rt_arr.append(dic)
                            print(dic)
        HhTime.costPrinter(st_time, pjName='身份证户籍编号')
        finish = True
    except:
        print("----------Wrong: {}".format('身份证户籍编号'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


def check_1(string):
    return string.replace(" ", "")[1:] if string else ''


tcmap()
