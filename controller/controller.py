#coding:utf-8
import dao.mysqlDb
from flask import Flask
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
def findCoupon():
    return 'Hello World!'

#look for Coupons
# return json
#param:item_keyword shop_name
@app.route('/lfc/findCoupon')
def findCoupon2():
    
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)