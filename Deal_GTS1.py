# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:50:28 2018

@author: hasee
"""
########  Copyright 成都信息过程大学 李方平 丁虹鑫
########   Time    2018年5月12日
#######  Function   读取探空数据，得到插值后的温度，压强，湿度，高度，原始10KM以下的数据
#####################返回值为一个元组，元祖内[0]为93个高度层的温度 [1]为压强 [2]为湿度 [3]为高度 [4]为探空原始数据
def Deal_GTS1(FileName):
    import numpy as np
    from scipy import interpolate
    #FileName = 'Z_UPAR_I_54511_20160106231520_O_TEMP-L.txt'
    file = open(FileName)
    i = 0 
    lines = file.readlines()
    startline = lines.index('ZCZC SECOND\n') + 1
    endline = lines.index('ZCZC MINUTE\n') - 2
    M = []
    linesneed = lines[startline:endline]
    for s in linesneed:
        lack_line = s.find('/')
        if lack_line == -1:
            p1 = s.split(' ')
            M.append(p1)
    A = np.zeros([len(M),12])
    for i in range(len(M)):
        for j in range(12):
            A[i,j] = M[i][j]
    x1 = np.where(A[:,-1]<10032)        ##找到高度小于10KM的位置  元祖
    x = x1[0][-1] + 1                     ##所在位置的数
    A1 = A[0:x,:]
    A1[:,1] = A1[:,1]+273.15            ##将温度行变为开尔文，以免插值出现错误，(在0℃左右可能出现)
    Height = [0,10,25,50,75,100,130,160,190,220,250,280,310,340,370,400,430,460,490,520,560,600,640,680,720,760,800,840,880,920,960,1000,1040,1080,1120,1160,1200,1260,1320,1380,1440,1500,1560,1620,1680,1740,1800,1890,1980,2170,2260,2350,2430,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3650,3800,3950,4100,4250,4400,4550,4600,4800,5000,5200,5400,5600,5800,6000,6300,6600,6900,7200,7500,7800,8100,8400,8700,9000,9300,9600,9800,10000]
    for i in range(93):
        Height[i] = Height[i] + 32
    #####插值操作
    tck_RH = interpolate.splrep(A1[:,-1],A1[:,3])
    tck_TEMP = interpolate.splrep(A1[:,-1],A1[:,1])
    tck_P = interpolate.splrep(A1[:,-1],A1[:,2])
    y_bs_RH = interpolate.splev(Height,tck_RH)   #将10KM的B-spline插值（湿度）
    y_bs_TEMP = interpolate.splev(Height,tck_TEMP)   #将10KM的B-spline插值(温度)
    y_bs_P = interpolate.splev(Height,tck_P)   #将10KM的B-spline插值(温度)
    
    #####返回的温湿压和高度
    return(y_bs_TEMP-273.15,y_bs_P,y_bs_RH,Height,A1)
    
#A = Deal_GTS1('Z_UPAR_I_54511_20160106231520_O_TEMP-L.txt')  #脚本内测试
