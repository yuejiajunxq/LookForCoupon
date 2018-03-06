#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import dao.CouponDao
import utils.redisUtil
import utils.httpUtil
from dao import DbUtil


class CouponService:
	def __init__(self):
		self.Coupon = dao.CouponDao.CouponDao("local")
	def test(self):
		test = self.Coupon.test()
		print "dao:%s" % test
		return test
	def returnDb(self,db):
		DbUtil.returnDB("local",db )
	def get(self,url,param,cookie):
	    hu = utils.httpUtil.httpUtil()
	    return hu.get(url,param,cookie)
	def insertEMPLOYEE(self,param):
		self.Coupon.insertEMPLOYEE(param)
		self.returnDb(self.Coupon.db)
	def getItemInfoInDB(self,itemid):
		print itemid
		#data = self.Coupon.getItemInfoInDB(itemid)
		#self.returnDb(self.Coupon.db)
		#return data
		return None
	def saveItemInfo(self,itemid,data):
		print itemid
		#self.Coupon.saveItemInfo(data)
		#self.returnDb(self.Coupon.db)
	#查询cookie信息
	def getCookie(self):
		info = self.Coupon.getCookie()
		self.returnDb(self.Coupon.db)
		return info[0]

	def setItemInRedisList(self,itemid):
		r = utils.redisUtil.getRedis("xz",0)
		r.lpush("items",itemid)

	def getItemInRedisList(self):
		r = utils.redisUtil.getRedis("xz",0)
		itemid = r.lpop("items")
		return itemid

	def getItemInfoInRedis(self,itemid,t=3):
		r = utils.redisUtil.getRedis("xz",0)
		p = r.pubsub()
		p.subscribe(itemid)
		str = None
		t1 = time.time()
		t2 = time.time()
		while t2-t1<t:
			time.sleep(0.5)
			str = p.get_message()
			print str
			if str==None:
				t2 = time.time()
				continue
			elif (str is None or not isinstance(str,unicode)) and 1 :
				str = str["data"]
				print "else--------"+str
				print not isinstance(str,unicode)
		print "return ------------------"+str(str)
		return str


if __name__ == '__main__':
	#print "CouponService:%s" % CouponService().test()
	#param = {"FIRST_NAME":"yue","LAST_NAME":"jiajun","AGE":"28","SEX":"M","INCOME":"1000"}
	coupon_service = CouponService()
	coupon_service.setItemInRedisList("21055196067")
	data = coupon_service.getItemInfoInRedis("21055196067",t=10)
	print data

