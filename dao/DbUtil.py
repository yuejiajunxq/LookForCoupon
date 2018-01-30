#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysqlDb
import MySQLdb

db_pool = {}
max_db_con = 20
db_info = {
    'huihex':{
        'host':"118.178.249.206",
        'user':"huihex",
        'password':"Koolma2010",
        'db':"huihex_test2",
        'port':3306
    }

}

def getDb(db_key):
    if(db_key not in db_pool):
        db_pool[db_key] = []
    key_db_list = db_pool[db_key]
    #result = getUnusedDb(key_db_list)
    if len(key_db_list) == 0:
        mydb = createDb(db_key)
        key_db_list.append(mydb)
    return  getUnusedDb(key_db_list)

def createDb(db_key):
    mymysql = mysqlDb.MyMysql(db_info[db_key]['host'], db_info[db_key]['user'], db_info[db_key]['password'],
                              db_info[db_key]['db'], db_info[db_key]['port'], )
    result = mymysql.init()
    return result

def getUnusedDb(db_list):
    result = ''
    if len(db_list) > 0 :
        result = db_list[0]
        db_list.pop(0)
    return result

def returnDB(key,db):
    db.commit()
    db_pool[key].append(db)

def getCursor(db):
    # 建立游标时，加上"MySQLdb.cursors.DictCursor"，让数据查询结果返回字典类型
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    return cur

#--------------------
def execute(cursor,sql):
    cursor.execute(sql)

def select(cursor,sql):
    results =''
    # SQL 查询语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
    except:
        print "Error: unable to fecth data"
    return results

if __name__ == '__main__':
    getDb('huihex')