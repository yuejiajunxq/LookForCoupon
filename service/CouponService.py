#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('D:\test\LookForCoupon')
import dao.CouponDao
import utils.httpUtil

class CouponService:
	def __init__(self):
		self.Coupon = dao.CouponDao.CouponDao()
	def test(self):
		test = self.Coupon.test()
		print "dao:%s" % test
		return test
	
	def get(self,url,param,cookie):
	    hu = httpUtil.httpUtil
	    return hu.get(url,param,cookie)
		

if __name__ == '__main__':
	print "CouponService:%s" % CouponService().test()
