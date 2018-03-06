#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DbUtil
import DbUtil

class CouponDao:
    def __init__(self,dbkey):
        self.db =  DbUtil.getDb(dbkey)
    def test(self):
        return "test"

    def insertEMPLOYEE(self,param):
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
                    LAST_NAME, AGE, SEX, INCOME)
                    VALUES ('${FIRST_NAME}', '${LAST_NAME}', ${AGE}, '${SEX}', ${INCOME})"""
        for key in param:
            sql = sql.replace("${"+key+"}",param[key],1)
        print sql
        DbUtil.getCursor(self.db).execute(sql)
    def saveItemInfo(self,param):
        sql = """INSERT INTO item_coupon(tao_token,coupon_short_link_url,qr_code_url,click_url,coupon_link_tao_token
                    ,coupon_link,type,item_id,short_link_url,coupon_start_time
                    ,coupon_end_time,coupon_amount,coupon_info,biz30day,tk_comm_fee
                    ,coupon_left_count,coupon_total_count,coupon_start_fee,reserve_price)
                    VALUES (${taoToken},${couponShortLinkUrl},${qrCodeUrl},${clickUrl},${couponLinkTaoToken},
                    ${couponLink},${type},${itemid},${shortLinkUrl},${couponEffectiveStartTime},
                    ${couponEffectiveEndTime},${couponAmount},${couponInfo},${biz30day},${tkCommFee}
                    ,${couponLeftCount},${couponTotalCount},${couponStartFee},${reservePrice})"""
        for key in param:
            value = ''
            if param[key]==None:
                value = 'Null'
            else:
                value = "'"+param[key]+"'"
            sql = sql.replace("${"+key+"}",value,1)
        print sql
        DbUtil.getCursor(self.db).execute(sql)
    def getCookie(self):
        sql = "SELECT site_id,menber_id,adzone_id,cookies FROM  cookie_info "
        cur = DbUtil.getCursor(self.db)
        cur.execute(sql)
        return cur.	fetchall()
    def getItemInfoInDB(self):
        sql = """SELECT tao_token as taoToken,
                        click_url as clickUrl,
                        coupon_link_tao_token as couponLinkTaoToken,
                        coupon_link as couponLink,
                        short_link_url as shortLinkUrl,
                        coupon_short_link_url as couponShortLinkUrl
                        FROM  item_coupon 
                        where item_id = ${itemid}"""
        cur = DbUtil.getCursor(self.db)
        cur.execute(sql)
        return cur.	fetchone()
