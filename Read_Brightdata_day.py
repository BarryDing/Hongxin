#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import numpy as np
#from scipy import interpolate
#import math

#例：FileName="H:/pycharm/D01/170201.BRT.ASC"
########  Copyright 成都信息过程大学 丁虹鑫
########   Time    2018年4月25日
########   Function 读取.BRT.ASC亮温数据(一天24小时，国际时间)，并获得14个通道的亮温



#例：FileName="H:/pycharm/D01/170201.BRT.ASC"
def ReadBright_day(FileName):
    import numpy as np
#from scipy import interpolate
    import math
    # 读取数据
    file = open(FileName)
    rowdata = len(file.readlines())                   # 文件行数 语句完成时，file指向文件最末尾
    file.seek(0, 0)                          # 将file指针重新定位到文件开头
    basedata = []                          # 初始化变量空间

    for index in range(8):  # 跳过8行文件头
        result = file.__next__()
    while True:  # 循环读取数据 按行读：年/月/日/时/分/秒/降雨标识/14个通道/高度角/方位角
        result = file.__next__()
        basedata.append(result.split(','))  # type(basedata): list
        index += 1
        if index == rowdata - 1:
            break
    basedata = np.array(basedata, dtype=float)  # list转数组(数据类型：float)

    ############### 时间序列
    TimeColums = np.zeros((1440, 5))
    TimeColums[:, 0] = basedata[0:1440, 0]  # 年
    TimeColums[:, 1] = basedata[0:1440, 1]  # 月
    TimeColums[:, 2] = basedata[0:1440, 2]  # 日
    TimeHour = []  # 定义list  存小时数
    TimeMinute = [[0 for col in range(1)] for row in range(60)]  # 定义60*1的list  存分钟数
    for i in range(24):
        for j in range(60):
            TimeHour.append(i)
    for i in range(60):
        TimeMinute[i] = i
    TimeMinute = TimeMinute * 24
    TimeColums[:, 3] = TimeHour
    TimeColums[:, 4] = TimeMinute
    # #######取分钟数据
    x = np.linspace(0, rowdata - 9,num=1440)  # x=[  0.00000000e+00   5.24933982e+01   1.04986796e+02 ...,   7.54330132e+04  7.54855066e+04   7.55380000e+04]
    y = []
    pending = []
    for i in x:
        y.append(math.floor(i))  # print(np.array(y).shape)              #y=[0, 52, 104, 157, 209, 262,   ,75538]    1440*1
    for i in y:
        pending.append(basedata[i, 7:21])
    pending = np.array(pending)  # print(pending.shape)                           #pending  1440*14         # print(f(np.transpose(y)))     # pl.show()
    finaldata = np.hstack((TimeColums, pending))
    file.close
    return finaldata