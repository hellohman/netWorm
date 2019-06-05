# coding=utf-8
import time
import xlrd
import xlsxwriter

from zzz_lib.HhTime import HhTime


# 读取  输入: 1.路径 2.标题行 3.存储方式 dict or arr   输出: { 'sheetName': [ ], 'sheetName': [ ] }
# 导出  输入: 1.文件名 2.字典数组     输出: { 'sheetName': [ ], 'sheetName': [ ] }

class HhExcel:

    @staticmethod  # 读取
    def reader(path, field_row=1, method='dict'):
        excel, rt_dic, st_time = xlrd.open_workbook(path), {}, time.time()
        # 读取方式:
        if method == 'dict':  # 1.字典方式
            for sheetName in excel.sheet_names():
                table = excel.sheet_by_name(sheetName)
                key_arr = table.row_values(field_row - 1)
                index_dic = {aa: key_arr.index(aa) for aa in key_arr}
                rt_dic[sheetName] = [{bb: str(table.row_values(i)[index_dic[bb]]) for bb in key_arr} for i in
                                     range(field_row, table.nrows)]
        elif method == 'arr':  # 2.数组方式
            for sheetName in excel.sheet_names():
                table = excel.sheet_by_name(sheetName)
                rt_dic[sheetName] = [[str(cell) for cell in table.row_values(i)] for i in
                                     range(field_row - 1, table.nrows)]
        HhTime.costPrinter(st_time, pjName='Excel读取完毕: {}'.format(method))
        return rt_dic

    @staticmethod  # 导出
    def writer(path, dicList):
        wb, st_time = xlsxwriter.Workbook(path), time.time()
        for dic in dicList:
            if dic['data']:
                sheet, title = wb.add_worksheet(dic['sheetName']), dic['fields']
                for aa in title: sheet.write(0, title.index(aa), aa)  # 标题
                for i, aa in enumerate(dic['data'], 1):  # 数据
                    for bb in title: sheet.write(i, title.index(bb), aa[bb])
        wb.close()
        HhTime.costPrinter(st_time, pjName='Excel输出完毕: {}'.format(path))
