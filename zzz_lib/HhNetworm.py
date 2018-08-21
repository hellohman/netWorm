# coding=utf-8
import json
import traceback
import requests
from parsel import Selector

netWorm_js = ''
try:
    with open(r'../zzz_lib/netWorm.json', 'r', encoding='utf-8') as f:
        netWorm_js = json.loads(f.read())
except:
    with open(r'../../zzz_lib/netWorm.json', 'r', encoding='utf-8') as f:
        netWorm_js = json.loads(f.read())
browsers, myStatus_code = netWorm_js['browsers'], netWorm_js['status_code']

class HhNetworm:

    sess = requests.session()
    sess.headers['User-Agent'] = browsers['Chrome']

    def getRes(self,url,method='g',result='c-s',data=None,verify=True,timeout=None,proxies=None,headers=None):
        if headers:
            self.sess.headers = headers
            self.sess.headers['User-Agent'] = browsers['Chrome']
        res, kwargs = None, {'verify':verify,'timeout':timeout,'proxies':proxies}
        try:
            if method == 'g': res = self.sess.get(url,params=data,**kwargs)
            elif method == 'p': res = self.sess.post(url,data=data,**kwargs)
        except (requests.exceptions.SSLError,requests.exceptions.ConnectionError) as e:
            print('-----------Warning----------- {}: {}'.format(type(e),e))
        except: traceback.print_exc()
        finally:
            if isinstance(res,requests.models.Response):
                status_code = res.status_code
                if status_code == 200: return self.dl_result(result,res)
                print('-----------Error----------- url: {}  状态码: {}  类型: {}'.format(url,status_code,self.status_type(res)))
            return self.dl_wrong_res(result)

    @staticmethod       # selector
    def getSel(text): return Selector(text)

    @staticmethod       # 辅助_结果处理
    def dl_result(result, res):
        if result == 'j': return res.json()
        elif result == 't': return res.text
        elif result == 't-s': return Selector(res.text)
        elif result == 'h': return res.headers                           # 请求头
        elif result == 'c': return res.content                           # 二进制响应内容
        elif result == 'c-d':
            try: return res.content.decode('utf-8')
            except: return res.content.decode('gb18030')
        elif result == 'c-s':                                             # selector
            try: return Selector(res.content.decode('utf-8'))
            except: return Selector(res.content.decode('gb18030'))

    @staticmethod       # 辅助_错误衔接
    def dl_wrong_res(result):
        if result in ('sel','text-sel'): return Selector("")
        elif result in ('json','headers'): return {}
        elif result in ('text','content'): return ""

    @staticmethod       # 辅助_状态码类型
    def status_type(response):
        for key,values in myStatus_code.items():
            if response.status_code in values: return key