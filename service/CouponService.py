#!/usr/bin/python
# -*- coding: UTF-8 -*-
import dao.CouponDao
import utils.httpUtil
from dao import DbUtil


class CouponService:
	def __init__(self):
		self.Coupon = dao.CouponDao.CouponDao("huihex")
	def test(self):
		test = self.Coupon.test()
		print "dao:%s" % test
		return test
	
	def get(self,url,param,cookie):
	    hu = utils.httpUtil.httpUtil()
	    return hu.get(url,param,cookie)
	def insertEMPLOYEE(self,param):
		self.Coupon.insertEMPLOYEE(param)
		self.returnDb(self.Coupon.db)
	def returnDb(self,db):
		DbUtil.returnDB("huihex",db )
if __name__ == '__main__':
	#print "CouponService:%s" % CouponService().test()
	param = {"FIRST_NAME":"yue","LAST_NAME":"jiajun","AGE":"28","SEX":"M","INCOME":"1000"}
	cs = CouponService()
	cs.insertEMPLOYEE(param)
