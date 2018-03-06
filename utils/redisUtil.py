#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import time

redis_cfg ={
    "xz":{
        "host":"192.168.31.86",
        "port":"6379",
        "user":""
    }
}
def getRedis(redisName,db_int):
    pool = redis.ConnectionPool(host=redis_cfg[redisName]["host"], port=redis_cfg[redisName]["port"], decode_responses=True,db=db_int)
    r = redis.Redis(connection_pool=pool)
    return r
def getredisdd(self):
    self.mysql.daaaa()

if __name__ == '__main__':
    r = getRedis("xz",0)
    p = r.pubsub()
    p.subscribe("redischat")
    str = p.get_message()
    print str
    r.publish("redischat","redischat test")
    time.sleep(2)
    str = p.get_message()
    print(str)
    str = p.get_message()
    print(str)
    #str = p.get_message()
    #print(str)
    r.publish("redischat","redischat test")
    time.sleep(2)
    str = p.get_message()
    print(str)
    str = p.get_message()
    print(str)
    r.publish("redischat","redischat test")
    time.sleep(2)
    str = p.get_message()
    print(str)
    str = p.get_message()
    print(str)
