# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm

# 模拟百度搜索

def baidu_search(wordArr,need_secondNet_title=False):
    st_time, rt_arr, finish = time.time(), [], False
    url1 = 'https://www.baidu.com/s'
    try:
        for word in wordArr:
            hhnetworm = HhNetworm()
            data1 = {'word':word,
                     'tn': '88093251_hao_pg',    # 定参 + 必传
                     # 'ie': 'utf-8',                # 定参 + 可不传
                     # 'srcqid': '2239491606901131802',       # 定参 + 可不传
                     # 'sc': 'UWY3rj04n1cdnNqCmyqxTAThIjYkPHnzPj6snW0kPWbdFhnqpA7EnHc1Fh7W5Hn1PWDkPjbYPs'     # 定参 + 可不传
                     }
            sel1 = hhnetworm.getRes(url1,data=data1,verify=False)
            for aa in sel1.css("#content_left div.result.c-container"):
                title_1 = aa.css("h3 a:nth-child(1) em::text").extract()
                title_2 = aa.css("h3 a:nth-child(1)::text").extract()
                brief_1 = aa.css("div.c-abstract em::text").extract()
                brief_2 = aa.css("div.c-abstract::text").extract()
                href = aa.css("h3 a:nth-child(1)::attr(href)").extract_first()      # 网址
                title = help_func_baidu(title_1,title_2)                                 # 标题
                brief = help_func_baidu(brief_1,brief_2)                                 # 简介

                dic = {
                    'word': word,           # 检索词
                    'title': title,         # 标题
                    'brief': brief,         # 简介
                    'href': href            # 网址
                }

                if need_secondNet_title:
                    sel2 = hhnetworm.getRes(href)
                    secondNet_title = sel2.css("head title::text").extract_first()      # 二级连接标题
                    dic['secondNet_title'] = secondNet_title

                rt_arr.append(dic)
                print(dic)
        HhTime.costPrinter(st_time,pjName='模拟百度搜索')
        finish = True
    except:
        print("----------Wrong: {}".format('模拟百度搜索'))
        traceback.print_exc()
    finally: return rt_arr if finish else []

def help_func_baidu(arr1,arr2):
    split_str = ''
    if len(arr1) == len(arr2):
        for aa,bb in zip(arr1,arr2): split_str += aa + bb
    else:
        if len(arr1) > len(arr2): short, long = arr2, arr1
        else: short, long = arr1, arr2
        for index in range(len(short)): split_str += long[index] + short[index]
        split_str += long[-1]
    return split_str

baidu_search(['斗鱼','python'],need_secondNet_title=False)