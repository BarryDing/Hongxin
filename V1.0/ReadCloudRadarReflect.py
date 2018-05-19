# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:04:49 2018

@author: hasee
"""
########  Copyright 成都信息过程大学 丁虹鑫
########   Time    2018年4月24日
########   Function 读取毫米波云雷达的程序
########  返回一个元组，分别为：云雷达数据个数，雷达反射率因子开始时间 结束时间 反射率因子矩阵
def ReadCloudRadarReflect(fname):
#    fname = 'UTC20170504_180138_060_01.dat'
    import struct
    import numpy as np
    f = open(fname,'rb')

    Size_of_Product = list(struct.unpack('I',f.read(4))) #Size_of_Product[0],文件个数
    starttime = list(struct.unpack('I',f.read(4)))       #开始时间
    endtime = list(struct.unpack('I',f.read(4)))         #结束时间

    EverySizeOfProduct = f.read(Size_of_Product[0]*4)
    SizeEveryDataByte = struct.unpack('I',EverySizeOfProduct[0:4])[0]

    HeadInformatin = f.read(156)                         #先读取文件头的156个字节
    DistNums = struct.unpack('I',HeadInformatin[16:20])[0] #找到距离库个数是多少
    f.seek(-156,1)                                          #文件指针再向前滑到156个字节前

    X = np.zeros([DistNums,Size_of_Product[0]])             #定义一个大小规定的0矩阵

    for i in range(Size_of_Product[0]):            #range函数，默认从0开始  range(1,5) 1,2,3,4  range(5) 0,1,2,3,4
        Data = f.read(SizeEveryDataByte)
    
        Datahead = Data[0:156]                           #文件头数据，156个字节
        DataBase = Data[156:SizeEveryDataByte]          #数据正文部分，SizeEveryDataByte-156个字节
        NumofBins1 = struct.unpack('I',Datahead[16:20])[0] #，每个文件头中，距离库的位置的数据
        Ptr1 = struct.unpack('I',Datahead[64:68])[0]        #每个文件头中，偏移量的位置的数据
    
        OneMinReflect = np.zeros([NumofBins1])              #定义一个0矩阵，存放单条廓线上的反射率因子
    
        for MM in range(0,DistNums):
            pp = chr(DataBase[Ptr1-1+MM])               
            pp = ord(pp)
            pp = (pp-2)*0.5 - 40.0                          #pp为单条廓线上的每个反射率因子
            OneMinReflect[MM] = pp
            X[:,i] = OneMinReflect

    f.close
    return(Size_of_Product[0],starttime,endtime,X)        #开始时间 结束时间 反射率因子矩阵