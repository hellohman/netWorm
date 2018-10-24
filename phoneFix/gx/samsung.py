# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm


def samsung(model_arr):
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "http://support-cn.samsung.com/supportcn/support/material_price/GetCailAjax.aspx"
    url2 = 'http://support-cn.samsung.com/supportcn/support/material_price/default.aspx'
    try:
        js1 = hhnetworm.getRes(url1, data={'pid': 1}, result='j')
        for model in model_arr:
            for aa in js1['Items']:
                sel1 = hhnetworm.getRes(url2, method='p',
                                        data={'__EVENTTARGET': '', 'btnSearch': '提交', 'ddlCail': aa['PName'], 'ddlProduct': 1, 'txtModel': model})
                mal_arr, price_arr = [], []  # 故障,价格
                for bb in sel1.css("div.table_box:nth-child(4) table:nth-child(1) tr:nth-child(n+2)"):
                    price = int(bb.css("td:nth-child(2)::text").extract_first().strip())
                    malfunction = bb.css("td:nth-child(1)::text").extract_first().strip()
                    malfunction = malfunction[malfunction.find(' ') + 1:]
                    mal_arr.append(malfunction), price_arr.append(price)
                # 辅料价格
                help_price = sum([price_arr[index] for index, bb in enumerate(mal_arr) if bb.find('辅料') != -1])
                for index, bb in enumerate(mal_arr):
                    if bb.find('辅料') == -1:
                        dic = {
                            'business': '官修',
                            'brand': '三星',
                            'type': '手机',
                            'model': model,
                            'color': '',
                            'malfunction': bb,
                            'plan': '',
                            'price': price_arr[index] + help_price,
                        }
                        rt_arr.append(dic)
                        print(dic)
        HhTime.costPrinter(st_time, pjName='三星', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('三星'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []


model_arr = [
    "SM-G9500",
    "SM-G9350",
    "SM-G9550"
]
samsung(model_arr)
