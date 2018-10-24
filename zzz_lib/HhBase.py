# coding=utf-8

class HhBase:

    @staticmethod  # 转int
    def toInt(inputStr):
        try:
            return int(inputStr)
        except ValueError as e:
            print('-----------Warning----------- {}: {}'.format('ValueError', e))
        return False
