# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:48:34 2018

@author: hasee
"""
########  Copyright 成都信息过程大学 丁虹鑫
########   Time    2018年5月4日
########  读取风廓线雷达6分钟的数据
########  pwd为文件夹名字 得到一天中的风廓线雷达的矩阵，包括，水平风速，风向，垂直风速，CN2指数
import numpy as np
import os
#import matplotlib.pyplot as plt
#pwd = os.getcwd()     #获取当前
def Get_Day_Cloud_Folder(pwd):
#pwd = os.getcwd()
    files = os.listdir(pwd)
#    rootdir = os.getcwd() 
    #################读取一个6分钟的文件
    def Get_sixMin_Cloud_Matrix(FileName):
        Height=np.array([150,270,390,510,630,750,870,990,1110,1230,1350,1470,1590,1710,1830,1950,2070,2190,2310,2430,2550,2670,2790,2910,3030,3150,3270,3390,3510,3630,3750,3870,3990,4110,4350,4590,4830,5070,5310,5550,5790,6030,6270,6510,6750,6990,7230,7470,7710,7950,8190,8430,8670,8910,9150,9390,9630,9870,10110])
        file = open(FileName)
        FileTime = FileName[15:27]
        i = 0                       #文件的行数
        lines = file.readlines()    #一次性读取所有的风廓线(6分钟)数据，以字符串的方式
        M_t = []
        for s in lines:
            m = s.replace('////////','-41').replace('//////','-41').replace('/////','-41').replace("\n", "")
            i = i+1
            M_t.append(m)
            M = M_t[3:i-1]
        X = np.zeros([59,7])
        for p in range(0,len(M)):
            J_t = M[p].split(' ')
            for p2 in range(0,7):
                X[p,p2] = float(J_t[p2])
        if len(M)<59:
            X[:,0] = Height
            X[len(M):59,1:7] = -41
        return(FileTime,X)
    #WDir (Wind direction) HWS  (Horizontal wind speed)
    #VHS  (Vertical wind speed) cn2指数
#    WHeight = np.zeros([59,1])
    WDir= np.zeros([59,240])
    HWS= np.zeros([59,240])
    VHS= np.zeros([59,240])
    Cn2 = np.zeros([59,240])
    
    C_line = []         
    for everyLines in files:
        if os.path.splitext(everyLines)[1]=='.TXT':
            A = Get_sixMin_Cloud_Matrix(pwd+'\\'+everyLines)
            #Cir 每天的文件中，某个文件对应的在这一天中的位置
            cir = int((int(everyLines[23:25])*60+int(everyLines[25:27]))/6)
            C_line.append(cir)
            WDir[:,cir] = A[1][:,1]
            HWS[:,cir] = A[1][:,2]
            VHS[:,cir] = A[1][:,3]
            Cn2[:,cir] = A[1][:,-1]
    C_line_all = range(0,240)          
    lack_time = list(set(C_line_all).difference(set(C_line)))  #找到无数据的位置
    for m in lack_time:
        WDir[:,m]=-41
        HWS[:,m]= -41
        VHS[:,m]= -41
        Cn2[:,m]= -41  #将无数据的位置用-41填充
    return(WDir,HWS,VHS,Cn2)
    
    

