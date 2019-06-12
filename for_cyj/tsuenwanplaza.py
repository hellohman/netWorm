# coding=utf-8
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel
from zzz_lib.HhJson import HhJson



def tsuenwanplaza():
    hhJson, rt_arr = HhJson(), []
    data = hhJson.reader(r'C:\Users\HH\Desktop\myGit_pro\netWorm\for_cyj\tsuenwanplaza.json')['result']
    for aa in data:
        dic = {
            '店名': aa['name_sc'],
            '商铺号': aa['shop_no'],
            '位置': aa['floor'],
            '电话': aa['telphone'],
        }
        print(dic)
        rt_arr.append(dic)
    return rt_arr

this_data = tsuenwanplaza()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\荃湾广场.xlsx', [{'sheetName': '荃湾广场', 'fields': ['店名', '商铺号', '位置', '电话'], 'data': this_data}])
