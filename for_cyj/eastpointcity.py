# coding=utf-8
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel
from zzz_lib.HhJson import HhJson



def eastpointcity():
    hhJson, rt_arr = HhJson(), []
    data = hhJson.reader(r'C:\Users\HH\Desktop\myGit_pro\netWorm\for_cyj\eastpointcity.json')
    for aa in data:
        dic = {
            '店名': aa['shop_name_sc'],
            '商铺号': aa['shop_no'],
            '电话': aa['shop_telephone'],
            '营业时间': aa['shop_opening_hour_sc'],
            '简介': aa['shop_description_sc']
        }
        print(dic)
        rt_arr.append(dic)
    return rt_arr

this_data = eastpointcity()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\东港城.xlsx', [{'sheetName': '东港城', 'fields': ['店名', '商铺号', '营业时间', '电话', '简介'], 'data': this_data}])
