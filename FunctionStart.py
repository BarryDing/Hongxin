# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:12:36 2018

@author: hasee
"""
########  Copyright 成都信息过程大学 丁虹鑫
########   Time    2018年4月28日
########  Function 反演程序入口
#################### 画图，分别为0~10KM相对湿度，0~10KM温度，0~15KM反射率因子

def FunctionRet():
    import ReadCloudRadarReflect
    import numpy as np
    import Read_Brightdata_day
    import ReadMET
    import NeutalNet_RH
    import NeuralNet_TEMP
    #import matplotlib
    #import time
#    import matplotlib.pyplot as plt
    
    #FunctionSTarttime = time.time()
    
    ####################################读取毫米波云雷达数据
    A = ReadCloudRadarReflect.ReadCloudRadarReflect('20170619_120123_060_01.dat')
    Radar_Size = A[0]                       #云雷达产品个数(一个dat文件有Radar_Size分钟)
    Radar_Starttime = str(A[1])                   #云雷达探测开始时间 (北京时间BTC)
    Radar_endtime = str(A[2])                     #云雷达探测结束时间
    RadarSliceLine = np.arange(1,345,8)
    OriginalRadar_R_Height = np.arange(0, 30*(np.shape(A[3])[0]), 30)
    Radar_Extra = A[3][RadarSliceLine]       #切片好的云雷达数据
    
    ######找到云雷达对应国际时间所在的位置
    #因为云雷达存储的字符串
    def str_chuli(undealStr):
        if len(undealStr)==5:    
            Strtime = '000'+ undealStr[1:len(undealStr)-1]
        if len(undealStr)==6:
            Strtime = '00'+ undealStr[1:len(undealStr)-1]
        if len(undealStr)==7:
            Strtime = '0'+ undealStr[1:len(undealStr)-1]
        if len(undealStr)==8:
            Strtime = undealStr[1:len(undealStr)-1]
        return(Strtime)
    Starttime = str_chuli(Radar_Starttime)
    #Endtime = str_chuli(Radar_endtime)  
    
    startLine = ((int(Starttime[0:2]))-8) * 60 + int(Starttime[2:4])
    
    #print(startLine)
    
    
    ####################################读取微波辐射计亮度温度数据
    BRT_Data = Read_Brightdata_day.ReadBright_day('170619.BRT.ASC')   #微波辐射计数据
    
    ####################################读取微波辐射计地面温湿压数据
    MET_Data = ReadMET.ReadMET_day('170619.MET.ASC')
    
    ####################################将毫米波云雷达，亮温和地面温湿压，组成一个矩阵
    UnRetrieve_BRTData = np.transpose(BRT_Data[startLine:startLine+Radar_Size,5:19])
    UnRetrieve_METData = np.transpose(MET_Data[startLine:startLine+Radar_Size,5:8])
    UnRetrieve_RH_Data = np.vstack((np.vstack((UnRetrieve_BRTData,UnRetrieve_METData)), Radar_Extra))
    UnRetrieve_TEMP_Data = np.vstack((UnRetrieve_BRTData,UnRetrieve_METData))
    
    ###################################,将矩阵送入网络做计算，反演后的湿度(未插值和阈值处理)
    Z_RH = NeutalNet_RH.NeutalNet(UnRetrieve_RH_Data)
    Z_TEMP = NeuralNet_TEMP.NeutalNet(UnRetrieve_TEMP_Data)
    
    Height = [0,10,25,50,75,100,130,160,190,220,250,280,310,340,370,400,430,460,490,520,560,600,640,680,720,760,800,840,880,920,960,1000,1040,1080,1120,1160,1200,1260,1320,1380,1440,1500,1560,1620,1680,1740,1800,1890,1980,2170,2260,2350,2430,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3650,3800,3950,4100,4250,4400,4550,4600,4800,5000,5200,5400,5600,5800,6000,6300,6600,6900,7200,7500,7800,8100,8400,8700,9000,9300,9600,9800,10000]
    TIME = np.arange(0,Radar_Size)
    Height = np.array(Height)
    TIME = np.array(TIME)
    return(Z_RH,Z_TEMP,Height,TIME)


