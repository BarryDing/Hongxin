# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:56:42 2018

@author: hasee
"""
########  Copyright 成都信息过程大学 李方平 丁虹鑫
########   Time    2018年5月15日
############## Function 读取微波辐射计自身反演，ReadTPC(读取一天的温度(1440个时刻点))
####################### ReadHPC(读取一天的湿度(1440个时刻点))
################(国际时)
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:56:42 2018

@author: hasee
"""
##############读取微波辐射计自身反演，TPC(温度)，HPC(湿度)
import numpy as np

def ReadTPC(FileName):
    file = open(FileName)
    lines = file.readlines()
    line = lines[9:-1]
    p=[]
    M = np.zeros([len(line), 100])
    for i1 in range(len(line)):
        p.append(line[i1].split(','))
    M = np.array(p, dtype=float)
    M_need = np.delete(M,[5,6],axis=1)
    
    temp = np.zeros([1440,98])
    
    for i in range(24):
        hour0 = np.argwhere(M_need[:,3]==i)
        for index in hour0:
            temp[int(M_need[index,4]+60*i-1 ),:] = M_need[index, :]
            
    P = np.argwhere(temp[:,5]==0)    #### P为0所在的行
    data = temp[:,5:98]
         
    j=0
    for i in P:
        data[i, :] = data[P[j]-1, :]
        j = j+1
    return(data-273.15)    #开尔文温度变为摄氏度    
    
#B = ReadTPC('160721.TPC.ASC')     #脚本内测试

#plt.plot(M_need[:,6],)   #插值前的点
#plt.plot(data[:,1])     #插值后的点
#plt.legend('插值前的画图')



#######读取HPC湿度数据
#############HPC数据分为二部分，第一部分为绝对湿度，第二部分为相对湿度,只需要读取相对湿度
#FileName_HPC = '160514.HPC.ASC'
def ReadHPC(FileName_HPC):
    file = open(FileName_HPC)
    lines = file.readlines()
    lineSTart = lines.index('   # Maximum relative Humidity in File\n') + 2  #找到相对湿度开始的位置
    line = lines[lineSTart:-1]
    p=[]

    for i1 in range(len(line)):
        p.append(line[i1].split(','))
    M = np.array(p, dtype=float)
    M_need = np.delete(M,[5,6],axis=1)
    
    temp = np.zeros([1440,98])
    
    for i in range(24):
        hour0 = np.argwhere(M_need[:,3]==i)
        for index in hour0:
            temp[int(M_need[index,4]+60*i-1 ),:] = M_need[index, :]
            
    P = np.argwhere(temp[:,5]==0)    #### P为0所在的行
    data = temp[:,5:98]      
    
    j=0
    for i in P:
        data[i, :] = data[P[j]-1, :]
        j = j+1
    return(data)
       
#C = ReadHPC('160514.HPC.ASC')    #脚本内测试   




  
        
        