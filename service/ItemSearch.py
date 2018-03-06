#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import utils.redisUtil
import utils.httpUtil
import service.CouponService


class ItemSearch:

    def searchItem(self,itemid,siteid,adzoneid,cookie):
        url = "http://pub.alimama.com/common/code/getAuctionCode.json?auctionid=${itemid}&siteid=${siteid}&adzoneid=${adzoneid}&t=${t}&scenes=1&_input_charset=utf-8"
        t = time.time()*1000
        url = url.replace("${itemid}", itemid, 1).replace("${siteid}", str(siteid), 1).replace("${adzoneid}", str(adzoneid), 1).replace("${t}", str(t), 1)
        hu = utils.httpUtil.httpUtil()
        res = hu.get(url,{},cookie)
        print res
        return res
    def getItemInfo(self):
        while True :
            time.sleep(1)
            # 先从队列取出itemid   查出访问需要的cookie，itemid，siteid，adzoneid
            item = self.getItemInRedisList()
            itemid = item["itemid"]
            cookie = item["cookie"]
            siteid = item["siteid"]
            adzoneid = item["adzoneid"]
            print type(itemid)
            if itemid == None :
                continue
            print itemid
            # 将返回信息的消息发布出去
            res = self.searchItem(itemid,siteid,adzoneid,cookie)
            self.setItemInfoInRedis(itemid,res)
            print res
    #从redis取出cookie，itemid，siteid，adzoneid
    def getItemInRedisList(self):
        r = utils.redisUtil.getRedis("xz", 0)
        itemInfo = r.lpop("items")
        item_sp = itemInfo.split('!@#')
        itemid = item_sp[0]
        cookie = item_sp[1]
        siteid = item_sp[2]
        adzoneid = item_sp[3]
        item = {"itemid":itemid,"cookie":cookie,"siteid":siteid,"adzoneid":adzoneid}
        print item
        return item

    def setItemInfoInRedis(self,itemid,res):
        print itemid + "|" +res
        r = utils.redisUtil.getRedis("xz", 0)
        r.publish(itemid, res)


if __name__ == '__main__':
    ish = ItemSearch()
    ish.getItemInfo()


