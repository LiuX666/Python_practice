#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/6/25 10:25
功能：测试oracle连接池代码
"""

#oracle连接池
import cx_Oracle
from DBUtils.PooledDB import PooledDB

"""
PooledDB的参数：
1. mincached，最少的空闲连接数，如果空闲连接数小于这个数，pool会创建一个新的连接,先打开一定数量的数据库连接，当使用的时候分配给调用者
2. maxcached，最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接
3. maxconnections，最大的连接数，
4. blocking，当连接数达到最大的连接数时，在请求连接的时候，如果这个值是True，请求连接的程序会一直等待，直到当前连接数小于最大连接数，如果这个值是False，会报错，
5. maxshared 当连接数达到这个数，新请求的连接会分享已经分配出去的连接

连接池对性能的提升表现在：
1.在程序创建连接的时候，可以从一个空闲的连接中获取，不需要重新初始化连接，提升获取连接的速度
2.关闭连接的时候，把连接放回连接池，而不是真正的关闭，所以可以减少频繁地打开和关闭连接     
"""
def OracleConn():
    try:
        oracle_pool = PooledDB(cx_Oracle,mincached=5,blocking=True, user='tjdsj', password='tjdsj', dsn='192.168.91.8:1521/bigdata')
        return  oracle_pool
    except Exception as e:
        print(e)

def getConn():
    conn = OracleConn().connection()
    cursor = conn.cursor()
    cursor.execute('select USERNAME from T_RMTJ_USER_INFO_TATT')
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()

import threading
for i in range(5):
    t = threading.Thread(target=getConn)
    t.start()