#!/usr/bin/python
# -*- coding: UTF-8 -*-
#get接口调用
import urllib
import urllib2
from flask import json



class httpUtil:
    def get(self,url,param,cookie):
        get_url = url + "?" + self.paramToUrlParamStr(param)
        cookie_headers = cookie
        print  get_url
        print  cookie_headers
        req = urllib2.Request(url=get_url, headers=cookie_headers)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return res
    def gettest(self):
        get_url = "https://pub.alimama.com/items/search.json?q=卫衣&toPage=1&shopTag=yxjh&perPageSize=50&pvid=10_101.47.18.228_535_1515482599171&"
        req = urllib2.Request(url=get_url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        print res

    def post(self,url,param,cookie):
        '''args_data = {
            'id': '321',
            'name': 'cba'
        }'''
        args_data = param
        args_data_urlencode = urllib.urlencode(args_data)
        post_url = url
        cookie_headers = cookie
        req = urllib2.Request(url=post_url, data=args_data_urlencode, headers=cookie_headers)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return res
        
    def paramToUrlParamStr(self,param):
        paramStr = ''
        for key in param:
            paramStr +=key+"="+param[key] + "&"
        return paramStr

    def StrToDict(self, str):
        return json.loads(str)
if __name__ == '__main__':
    hu = httpUtil()
    hu.gettest()