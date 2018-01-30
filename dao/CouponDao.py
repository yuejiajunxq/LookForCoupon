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
