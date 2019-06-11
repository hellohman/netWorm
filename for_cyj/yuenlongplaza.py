# coding=utf-8
import time
import traceback

from zzz_lib.HhTime import HhTime
from zzz_lib.HhNetworm import HhNetworm
from zzz_lib.HhExcel import HhExcel


def yuenlongplaza():
    st_time, rt_arr, finish, hhnetworm = time.time(), [], False, HhNetworm()
    url1 = "http://www.yuenlongplaza.com/"
    try:
        sel1 = hhnetworm.getRes(url1 + 'index.php?option=com_content&view=category&id=18&Itemid=123&lang=cn')
        for aa in sel1.css("#content div div.rightcol div div div a:nth-child(-n+9)"):
            url2 = url1 + aa.css("::attr(href)").extract_first()
            sort = deal_url(url2)
            sel2 = hhnetworm.getRes(url2)
            for bb in sel2.css("ul.category li"):
                sel3 = hhnetworm.getRes(url1 + bb.css("div a::attr(href)").extract_first())
                dic = {
                    '分类': sort,
                    '商店編號': '',
                    '商店名稱': '',
                    '電話': '',
                    '網址': ''
                }
                this_sel = []
                if sort in ['潮流坊', '美容/药房/个人护理', '家居用品/影音/电子产品', '珠宝钟表', '超级市场', '礼品/书籍/生活品位']:
                    this_sel = sel3.css("#content div.item-page div.shopinfo table tbody tr:nth-child(1) td:nth-child(1) table tbody tr")
                else:
                    this_sel = sel3.css("#content div.maincol div.maincol_w_right div.nopad div.shopinfo table tbody tr:nth-child(1) td:nth-child(1) table tbody tr")
                for cc in this_sel:
                    # #content div.item-page div.shopinfo table tbody tr:nth-child(1) td:nth-child(1) table tbody tr
                    xxx = cut_same(cc.css("::text").extract())
                    if xxx:
                        if len(xxx) == 1:
                            if '電話:' not in xxx and '網址:' not in xxx and '商店編號:' not in xxx and '商店名稱:' not in xxx:
                                if xxx[0] != dic['商店名稱']:
                                    dic['商店名稱'] += '-' + xxx[0]
                        if len(xxx) >= 2:
                            if '認受商戶' not in xxx:
                                if xxx[0] == '商店編號:':
                                    dic['商店編號'] = xxx[1]
                                elif xxx[0] == '商店名稱:':
                                    dic['商店名稱'] = xxx[1]
                                elif xxx[0] == '電話:':
                                    dic['電話'] = xxx[1]
                                elif xxx[0] == '網址:':
                                    dic['網址'] = xxx[1]
                print(dic)
                rt_arr.append(dic)
        HhTime.costPrinter(st_time, pjName='元朗广场', dataArr=rt_arr)
        finish = True
    except:
        print("----------Wrong: {}".format('元朗广场'))
        traceback.print_exc()
    finally:
        return rt_arr if finish else []

def cut_same(arr):
    rt_arr = []
    for aa in arr:
        if aa not in rt_arr and aa != '\r\n':
            rt_arr.append(aa)
    return rt_arr


def deal_url(url):
    if url == 'http://www.yuenlongplaza.com/index.php?option=com_content&view=category&id=15':
        return '潮流服饰'
    elif url == 'http://www.yuenlongplaza.com/index.php?option=com_content&view=category&id=16':
        return '潮流坊'
    elif url == 'http://www.yuenlongplaza.com/index.php?option=com_content&view=category&id=12':
        return '美容/药房/个人护理'
    elif url == 'http://www.yuenlongplaza.com/index.php?option=com_content&view=category&id=18':
        return '餐饮美食'
    elif url == 'http://www.yuenlongplaza.com/index.php?option=com_content&view=category&id=11':
        return '家居用品/影音/电子产品'
    elif url == 'http://www.yuenlongplaza.com/index.php?option=com_content&view=category&id=14':
        return '珠宝钟表'
    elif url == 'http://www.yuenlongplaza.com/index.php?option=com_content&view=category&id=19':
        return '超级市场'
    elif url == 'http://www.yuenlongplaza.com/index.php?option=com_content&view=category&id=13':
        return '礼品/书籍/生活品位'


this_data = yuenlongplaza()

excel_1 = HhExcel()
excel_1.writer(r'C:\Users\HH\Desktop\元朗广场.xlsx', [{'sheetName': '元朗广场', 'fields': ['分类', '商店編號', '商店名稱', '電話', '網址'], 'data': this_data}])
