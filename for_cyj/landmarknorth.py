# coding=utf-8
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel
from zzz_lib.HhJson import HhJson


def landmarknorth():
    hhnet = HhNetworm()
    hhJson, rt_arr = HhJson(), []
    data = hhJson.reader(r'C:\Users\HH\Desktop\myGit_pro\netWorm\for_cyj\landmarknorth.json')
    print(data['html'])
    sel1 = hhnet.getSel(data['html'])
    name_arr, floor_arr, number_arr, phone_arr = [], [], [], []
    for aa in sel1.css("tr.shoplist_tr td:nth-child(4n+2)"):
        floor_arr.append(aa.css("::text").extract_first())

    for aa in sel1.css("tr.shoplist_tr td:nth-child(4n+3)"):
        number_arr.append(aa.css("::text").extract_first())

    for aa in sel1.css("tr.shoplist_tr td:nth-child(4n+4)"):
        phone_arr.append(aa.css("::text").extract_first())

    for aa in sel1.css("tr.shoplist_tr td"):
        name = aa.css("td a::text").extract_first()
        if name:
            name_arr.append(name)

    for name, floor, number, phone in zip(name_arr, floor_arr, number_arr, phone_arr):
        dic = {
            '店名': name,
            '楼层': floor,
            '商铺号码': number,
            '电话': phone
        }
        print(dic)
        rt_arr.append(dic)
    return rt_arr

this_data = landmarknorth()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\上水广场.xlsx', [{'sheetName': '上水广场', 'fields': ['店名', '楼层', '商铺号码', '电话'], 'data': this_data}])
