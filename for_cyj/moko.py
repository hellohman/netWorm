# coding=utf-8
from zzz_lib.HhExcel import HhExcel
from zzz_lib.HhJson import HhJson


def moko():

    hhJson, rt_arr = HhJson(), []
    data = hhJson.reader(r'C:\Users\HH\Desktop\myGit_pro\netWorm\for_cyj\moko.json')
    for shop in data['shops']:
        dic = {
            '店名': shop['shop_name'],
            '营业时间': shop['opening_hours'][0]['date'] + '：' + shop['opening_hours'][0]['time'],
            '位置': shop['shop_floor'] + ' ' + shop['shop_number'],
            '电话': shop['phone']
        }
        print(dic)
        rt_arr.append(dic)

    return rt_arr

this_data = moko()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\新世纪广场.xlsx', [{'sheetName': '新世纪广场', 'fields': ['店名', '营业时间', '位置', '电话'], 'data': this_data}])
