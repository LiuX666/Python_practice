#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/6/27 8:41
功能：日志时间相加减
"""
import datetime
import time


log = open('./file/info.log', encoding="utf-8")
list=[]
for line in log:
    log_data = ','.join(filter(lambda x: x, line.split(' ')))
    date = (log_data.split(',')[0])[-10:].replace('.', '-')
    times = (log_data.split(',')[1])[-10:].replace('.', '-')
    logtime = date + " " + times
    # logtime=time.strptime(logtime, '%Y-%m-%d %H:%M:%S')
    # y, m, d, H, M, S = logtime[:6]
    # q=(datetime.datetime(y, m, d, H, M, S)+datetime.timedelta(seconds=-10)).strftime("%Y-%m-%d %H:%M:%S")
    if logtime>(datetime.datetime.now()+datetime.timedelta(seconds=-120)).strftime("%Y-%m-%d %H:%M:%S") and logtime< datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        list.append(line)

dfTime = (datetime.datetime.now() + datetime.timedelta(seconds=30)).strftime("%Y-%m-%d %H:%M:%S")
