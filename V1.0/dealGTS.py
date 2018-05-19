# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:17:03 2018

@author: hasee
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:56:42 2018

@author: hasee
"""
##############读取微波辐射计自身反演，TPC(温度)，HPC(湿度)
import numpy as np
from scipy import interpolate
from skimage import transform
import cv2
import matplotlib.pyplot as plt

FileName = '160721.TPC.ASC'
file = open(FileName)
lines = file.readlines()
line = lines[9:-1]
p=[]
M = np.zeros([len(line), 100])
for i1 in range(len(line)):
    p.append(line[i1].split(','))
M = np.array(p, dtype=float)
M_need = np.delete(M,[5,6],axis=1)
# M_need = np.hstack((M[:,0:5],M[:, 7:])) ###读取数据所得到的温度
Time_colum = M[:, 0:6]
finaldata = np.zeros([1440,98])
##构造时间列，以对应一天中的每分钟的数据
TIM = np.zeros([1440, 1])
A = len(M_need)

temp = np.zeros([1440,98])

for i in range(24):
    hour0 = np.argwhere(M_need[:,3]==i)
    for index in hour0:
        temp[int(M_need[index,4]+60*i-1),:] = M_need[index, :]