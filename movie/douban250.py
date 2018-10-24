# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


# 豆瓣250

def douban250():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "https://movie.douban.com/top250?start=%d&filter="
    try:
        for myindex in range(10):
            sel = hhnetworm.getRes(url1 % (myindex * 25))
            for zzz in sel.css("#content div div.article ol.grid_view li div.item"):
                for aa in zzz.css("div.info"):
                    name = ""
                    for bb in aa.css("div.hd a span"):
                        name += bb.css("::text").extract_first()
                    body = aa.css("div.bd p:nth-child(1)::text").extract()
                    introduction1 = body[0].replace(" ", "").replace(" ", "")
                    introduction2 = body[1].replace(" ", "").replace(" ", "")
                    director = introduction1[introduction1.find("导演:") + len("导演:"):introduction1.find("主演:")].replace("'", "~")  # 导演
                    actors = introduction1[introduction1.find("主演:") + len("主演:"):].replace("'", "~")  # 主演
                    year = int(introduction2[:introduction2.find("/")].replace("\n", "")[:4])  # 年份
                    introduction2 = introduction2[introduction2.find("/") + 1:]
                    country = introduction2[:introduction2.find("/")].replace(" ", "").replace(" ", "")  # 国家
                    introduction2 = introduction2[introduction2.find("/") + 1:]

                    dic = {
                        'source': '豆瓣',  # 商家
                        "name": name.replace(" ", "").replace(" ", "").replace("'", "~"),  # 名称
                        "sorce": float(aa.css("div.bd div span.rating_num::text").extract_first()),  # 评分
                        "type": introduction2[:introduction2.find("/")].replace(" ", "").replace(" ", ""),  # 类型
                        "country": country,  # 国家
                        "year": year,  # 年份
                        "director": director,  # 导演
                        "actors": actors,  # 主演
                        "pictureUrl": zzz.css("div.pic a img::attr(src)").extract_first(),  # 图片url
                        'have_watched': 'N'  # 是否观看过
                    }
                    rt_arr.append(dic)
                    print(dic)
        HhTime.costPrinter(st_time, pjName='豆瓣250', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('豆瓣250'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


douban250()
