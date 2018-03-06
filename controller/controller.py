#coding:utf-8
#import dao.mysqlDb
from flask import Flask
from flask import request
import sys
sys.path.append('E:\python\LookForCoupon')
import service.CouponService
import json

reload(sys)

sys.setdefaultencoding('utf8')
app = Flask(__name__)

# Hello World test
@app.route('/lfc/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
#look for Coupons
# return json
#param:item_keyword shop_name
@app.route('/lfc/test')
def test():
    return 'Hello World!'

#look for Coupons
# return json
#param:item_keyword shop_name
@app.route('/lfc/findCoupon')
def findCoupon():
    couponService = service.CouponService.CouponService()
    #https://pub.alimama.com/items/search.json?q=%E5%8D%AB%E8%A1%A3&_t=1515482317280&toPage=1&
    #准备参数 auctionId q  perPageSize toPage
    url = 'https://pub.alimama.com/items/search.json'
    param = {}
    req_param = getParam(request)
    for key in req_param:
        param[key] = req_param.get(key)
    param['q'] = '卫衣'
    param['perPageSize'] = '50'
    param['shopTag'] = 'yxjh%2Cdpyhq'
    param['toPage'] = '1'
    param['dpyhq'] = '1'
    param['pvid'] = '10_101.47.18.228_535_1515482599171'
    #访问阿里妈妈接口
    data = couponService.get(url,param,{})
    return data
#look for Coupons
# return json
#param:item_keyword shop_name
@app.route('/lfc/getTKInfoByItemid')
def getTKInfoByItemid():
    coupon_service = service.CouponService.CouponService()
    param = {}
    req_param = getParam(request)
    for key in req_param:
        param[key] = req_param.get(key)
    itemid = param["itemid"]
    print itemid
    # 查询数据库是否有订单的
    item_info = coupon_service.getItemInfoInDB(itemid)
    if item_info != None :
        return item_info
    # 如果没有订单把itemid放进redis
    coupon_service.setItemInRedisList(itemid)
    # 从redis读取返回的订单数据
    data = coupon_service.getItemInfoInRedis(itemid, t=3)
    # 把数据replacein订单表
    coupon_service.saveItemInfo(itemid,data)
    print data
    return data
def getParam(req):
    method = req.method
    param = None
    if method=='POST':
        param = req.form
    elif method=="GET" :
        param = req.args
    if param is None :
        param = {}
    return param
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
