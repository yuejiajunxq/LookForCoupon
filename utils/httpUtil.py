#!/usr/bin/python
# -*- coding: UTF-8 -*-
#get接口调用
import urllib
import urllib2



class httpUtil:
    def get(self,url,param,cookie):
        get_url = url + "?" + self.paramStr(param)
        cookie_headers = cookie
        req = urllib2.Request(url=get_url, headers=cookie_headers)
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
        print res
    def paramToUrlParamStr(self,param):
        return param

    def StrToDict(self, str):
        return str