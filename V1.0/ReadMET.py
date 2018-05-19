# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:08:22 2018

@author: hasee
"""
########  Copyright 成都信息过程大学 丁虹鑫
########   Time    2018年4月25日
########  Function 读取.MET.ASC文件，获取该文件下的地面温湿压值


import numpy as np
import math

#例：FileName="H:/pycharm/D01/170201.BRT.ASC"
def ReadMET_day(FileName):
    # 读取数据
    file = open(FileName)
    row = len(file.readlines())                   # 文件行数 语句完成时，file指向文件最末尾
    rowdata = row-18
    file.seek(0, 0)                          # 将file指针重新定位到文件开头
    basedata = []                          # 初始化变量空间
#    min_data = []
#    finaldata = []
    for index in range(18):  # 跳过8行文件头
        result = file.__next__()
    while True:  # 循环读取数据 按行读：年/月/日/时/分/秒/降雨标识/14个通道/高度角/方位角
        result = file.__next__()
        basedata.append(result.split(','))  # type(basedata): list
        index += 1
        if index == row - 1:
            break
    basedata = np.array(basedata, dtype=float)  # list转数组(数据类型：float)
#    basedataneed = basedata[:,7:10]

    ############### 时间序列
    TimeColums = np.zeros((1440, 5))
    TimeColums[:, 0] = basedata[0:1440, 0]  # 年
    TimeColums[:, 1] = basedata[0:1440, 1]  # 月
    TimeColums[:, 2] = basedata[0:1440, 2]  # 日
    TimeHour = []  # 定义list  存小时数
    TimeMinute = [[0 for col in range(1)] for rowdata in range(60)]  # 定义60*1的list  存分钟数
    for i in range(24):
        for j in range(60):
            TimeHour.append(i)
    for i in range(60):
        TimeMinute[i] = i
    TimeMinute = TimeMinute * 24
    TimeColums[:, 3] = TimeHour
    TimeColums[:, 4] = TimeMinute
    #############数据列
#    METData = np.zeros((1440,3))
    # #######取分钟数据
    pending = np.zeros([1440,3])
    x = np.linspace(0, rowdata-1,num=1440)  # x=[  0.00000000e+00   5.24933982e+01   1.04986796e+02 ...,   7.54330132e+04  7.54855066e+04   7.55380000e+04]
    y = np.zeros(1440)
    for i in range(0,1440): 
        y[i] = math.floor(x[i])
        pending[i,:] = basedata[int(y[i]),7:10]
    Data = np.transpose(np.vstack((np.vstack((pending[:,0],pending[:,2])),pending[:,1]-273.15)))
    DataNeed = np.hstack((TimeColums,Data))
#    MET_Data = 
    return(DataNeed)
#M = ReadMET_day('170504.MET.ASC')
