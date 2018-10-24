# coding=utf-8
import time


class HhTime:

    @staticmethod  # 耗时打印
    def costPrinter(st_time, type='s', pjName='', dataArr=None):
        if type == 's':
            print('{:<10}{:<}  耗时:{:^}秒'.format(pjName, '  数据量:{:>7}'.format(len(dataArr)) if dataArr else '', round((time.time() - st_time), 1)))
        elif type == 'm':
            print(
                '{:<10}{:<}  耗时:{:^}分'.format(pjName, '  数据量:{:>7}'.format(len(dataArr)) if dataArr else '', round((time.time() - st_time) / 60, 1)))
