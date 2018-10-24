# coding=utf-8
import time
import traceback

from bs4 import BeautifulSoup

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def wuyixiu():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url2 = 'http://www.51xiu.cc/fi/choosePlans'
    url3 = 'http://www.51xiu.cc/fi/select'
    url4 = 'http://www.51xiu.cc/fi/getPlan'
    try:
        sel1 = hhnetworm.getRes('http://www.51xiu.cc/repair')
        for aa in sel1.css("div.big-box div div:nth-child(2) div div"):
            bId = aa.css("::attr('brandid')").extract_first().strip()
            tId = aa.css("::attr('tid')").extract_first().strip()

            js2 = hhnetworm.getRes(url2, method='p', data={'bId': bId, 'tId': tId}, result='j')
            for bb in js2['versionList']:
                versionName = bb['versionName']  # 型号

                color, cId = '', ''
                text3 = hhnetworm.getRes(url3, data={'bId': bId, 'tId': tId, 'versionName': versionName, 'versionId': bb['id']}, result='t')
                for index, each in enumerate(BeautifulSoup(text3, 'lxml').find('div', class_='clear')):
                    if index % 2:
                        color += each.text + ','
                        cId = each['colorid']

                js4 = hhnetworm.getRes(url4, method='p', result='j', data={'cId': cId})
                for cc in js4['result']:
                    dic = {
                        'business': '51修',
                        'brand': aa.css("::text").extract_first().strip(),
                        'type': '手机',
                        'model': versionName,
                        'color': color[:-1],
                        'malfunction': cc['detail'],
                        'plan': cc['plan'],
                        'price': cc['price'],
                    }
                    rt_arr.append(dic)
                    print(dic)
        HhTime.costPrinter(st_time, pjName='51修', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('51修'))
        traceback.print_exc()
    finally:
        return dl_wuyixiu_data(rt_arr) if finish else []


def dl_wuyixiu_data(array):  # dic预处理
    rt_arr, ascii_array = [], range(48, 59)

    for aa in array:
        if aa['malfunction'].find("保修期内") == -1 and aa['malfunction'].find("保修内") == -1:
            for index in range(len(aa['plan'])):
                if ord(aa['plan'][index]) in ascii_array:
                    aa['plan'] = aa['plan'][:index]
                    break
            rt_arr.append(aa)
    return rt_arr


wuyixiu()
