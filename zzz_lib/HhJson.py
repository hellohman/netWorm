# coding=utf-8
import json
import time

from zzz_lib.HhTime import HhTime


# 读取
# 导出
# json转pyObj
# pyObj转json

class HhJson:

    # 读取
    def reader(self, path, encoding='utf-8'):
        try:
            st_time = time.time()
            with open(path, 'r', encoding=encoding) as f:
                pyObj = self.toPy(f.read())
                HhTime.costPrinter(st_time, pjName='json读取完毕: {}'.format(path))
                return pyObj
        except:
            return None

    # 导出
    def writer(self, path, pyObj, encoding='utf-8'):
        st_time = time.time()
        with open(path, 'w', encoding=encoding) as f: f.write(self.pyToJson(pyObj))
        HhTime.costPrinter(st_time, pjName='json输出完毕: {}'.format(path))

    @staticmethod  # json转pyObj
    def toPy(jsonStr):
        return json.loads(jsonStr)

    @staticmethod  # pyObj转json
    def pyToJson(pyObj):
        return json.dumps(pyObj, indent=2, ensure_ascii=False)
