#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('E:\\python\\LookForCoupon')
import dao.CouponDao


class CouponService:
    def __init__(self):
        self.Coupon = dao.CouponDao.CouponDao()
    def test(self):
        test = self.Coupon.test()
        print "dao:%s" % test
        return test

if __name__ == '__main__':
    print "CouponService:%s" % CouponService().test()