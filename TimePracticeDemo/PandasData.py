#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/8/2 11:03
功能：pandas 数据分析
"""


import pandas as pd
from scipy import stats
import os

PATH=os.getcwd()

df = pd.read_csv(PATH+'/file/person.csv')

def easyTest():
    # 最后5行数据
    print(df.tail())

    #取出从11到16行的前3列数据
    print(df.ix[10:15, 0:3])

    #舍弃数据中的列,axis 参数告诉函数到底舍弃列还是行。如果axis等于0，那么就舍弃行。
    print(df.drop(df.columns[[0]], axis = 1).head())

    #数缺失值
    # print(df.isnull().sum(axis=1).reset_index())

    #重新指定索引及NaN填充值
    #print(df.reindex(range(100), fill_value=0))
    #重新指定column
    # states = ['A', 'B', 'C', 'D']
    # x = x.reindex(columns=states, fill_value=0)





