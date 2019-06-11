# coding=utf-8
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel
from zzz_lib.HhJson import HhJson


def metroplaza():
    hhJson, rt_arr = HhJson(), []
    data = hhJson.reader(r'C:\Users\HH\Desktop\myGit_pro\netWorm\for_cyj\metroplaza.json')
    for aa in data['result']:
        dic = {
            '店名': aa['name_sc'],
            '楼层': aa['floor'],
            '商铺号': aa['shop_no'],
            '电话': aa['telphone']
        }
        print(dic)
        rt_arr.append(dic)
    return rt_arr


this_data = metroplaza()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\新都会广场.xlsx', [{'sheetName': '新都会广场', 'fields': ['店名', '楼层', '商铺号', '电话'], 'data': this_data}])
