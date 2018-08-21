# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

# 猫眼100

def maoyan100():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = 'http://maoyan.com/board/4'
    try:
        for offset in range(0,100,10):
            sel1 = hhnetworm.getRes(url1,data={'offset':offset})
            for aa in sel1.css("#app div div div.main dl dd:nth-child(n+1)"):
                actors = aa.css("p.star::text").extract_first()
                year = aa.css("p.releasetime::text").extract_first()
                year = year[year.find('：')+1:]

                dic = {
                    'source':'猫眼',                                                                                              # 商家
                    "name": aa.css("a::attr(title)").extract_first(),                                                          #　名称
                    "sorce" :float(aa.css("i.integer::text").extract_first() + aa.css("i.fraction::text").extract_first()),  #　评分
                    "type": '',                                                                                                   #  类型
                    "country": year[year.find('(')+1:year.find(')')] if year.find('(') != -1 and year.find(')') != -1 else '',#  国家
                    "year": year[:year.find('(')] if year.find('(') != -1 and year.find(')') != -1 else year,                  #  年份
                    "director": '',                                                                                              #　导演
                    "actors": actors[actors.find('：')+1:].strip(),                                                         #  主演
                    "pictureUrl": aa.css("a img::attr(data-src)").extract_first(),                                           # 图片url
                    'have_watched':'N'                                                                                          # 是否观看过
                }
                rt_arr.append(dic)
                print(dic)
        HhTime.costPrinter(st_time,pjName='猫眼100',dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('猫眼100'))
        traceback.print_exc()
    finally: return rt_arr if finish else []

maoyan100()