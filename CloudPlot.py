# -*- coding: utf-8 -*-
"""
Created on Tue May  8 11:08:33 2018

@author: hasee
"""

# -*- coding: utf-8 -*-
#####随意修改版本
"""
Created on Fri May  4 14:23:36 2018

@author: hasee
"""

import matplotlib
import numpy as np
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QAction, QFileDialog
import matplotlib.pyplot as plt
import sys
import fengyu
import FunctionStart
import math

import FunctionStart

class My_Main_window(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(My_Main_window,self).__init__(parent)
        # 重新调整大小
        self.resize(1280, 720)
        # 添加菜单中的按钮
        self.huitu = QtWidgets.QMenu("温度")
        self.huitu_action = QtWidgets.QAction("温度",self.huitu)
        self.huitu.addAction(self.huitu_action)
        self.menuBar().addMenu(self.huitu)
        
        self.shidu = QtWidgets.QMenu("湿度")
        self.shidu_action = QtWidgets.QAction("湿度",self.shidu)
        self.shidu.addAction(self.shidu_action)
        self.menuBar().addMenu(self.shidu)
        
        self.fengxiang = QtWidgets.QMenu("风向")
        self.fengxiang_action = QtWidgets.QAction("风向",self.fengxiang)
        self.fengxiang.addAction(self.fengxiang_action)
        self.menuBar().addMenu(self.fengxiang)
        
        self.shuiping = QtWidgets.QMenu("水平风速")
        self.shuiping_action = QtWidgets.QAction("水平风速",self.shuiping)
        self.shuiping.addAction(self.shuiping_action)
        self.menuBar().addMenu(self.shuiping)
        
        self.chuizhi = QtWidgets.QMenu("垂直风速")
        self.chuizhi_action = QtWidgets.QAction("垂直风速",self.chuizhi)
        self.chuizhi.addAction(self.chuizhi_action)
        self.menuBar().addMenu(self.chuizhi)
        
        self.zhishu = QtWidgets.QMenu("CN2指数")
        self.zhishu_action = QtWidgets.QAction("CN2指数",self.zhishu)
        self.zhishu.addAction(self.zhishu_action)
        self.menuBar().addMenu(self.zhishu)
        
        
        
        # 添加事件
        
#        self.menu_action.triggered.connect(self.plot_Cloud)
        
        self.huitu_action.triggered.connect(self.plot_TEMP)
        
        self.shidu_action.triggered.connect(self.plot_RH)
        
        self.fengxiang_action.triggered.connect(self.plot_WDir)
        
        self.shuiping_action.triggered.connect(self.plot_HWS)
        
        self.chuizhi_action.triggered.connect(self.plot_VHS)
        
        self.zhishu_action.triggered.connect(self.plot_CN2)
        
        self.setCentralWidget(QtWidgets.QWidget())

    # 绘图方法
    def plot_WDir(self):
        # 清屏
        plt.cla()
        # 获取绘图并绘制
        dir_path=QFileDialog.getExistingDirectory()  #打开文件夹
        #A1 = fengyu.Get_Day_Cloud_Folder('D:\\try_matlab_to_C++\\robs - 副本')
        A1 = fengyu.Get_Day_Cloud_Folder(dir_path)
#        print(A1[0])
        fig = plt.figure()
        fig.add_axes([0.1,0.1,0.8,0.8])        
        TIME = range(0,240)
        Height = np.array([150,270,390,510,630,750,870,990,1110,1230,1350,1470,1590,1710,1830,1950,2070,2190,2310,2430,2550,2670,2790,2910,3030,3150,3270,3390,3510,3630,3750,3870,3990,4110,4350,4590,4830,5070,5310,5550,5790,6030,6270,6510,6750,6990,7230,7470,7710,7950,8190,8430,8670,8910,9150,9390,9630,9870,10110])
#        fig = plt.figure()
        im2 = plt.pcolor(TIME,Height,A1[0],cmap=plt.cm.jet)
        #im2.set_clim(vmin=1.8e-21,vmax=5.7e-17) #(cn2)
        #im2.set_clim(vmin=-2,vmax=2) #(VHS)
        #im2.set_clim(vmin=0,vmax=35) #(HWS)
        im2.set_clim(vmin=0,vmax=360)
        plt.title('Wind direction')
        plt.colorbar(im2)
#plt.show()
        
        cavans = FigureCanvas(fig)
        # 将绘制好的图像设置为中心 Widget
        self.setCentralWidget(cavans)
        
            # 绘图方法
    def plot_HWS(self):
        # 清屏
        plt.cla()
        # 获取绘图并绘制
        dir_path=QFileDialog.getExistingDirectory()  #打开文件夹
        #A1 = fengyu.Get_Day_Cloud_Folder('D:\\try_matlab_to_C++\\robs - 副本')
        A1 = fengyu.Get_Day_Cloud_Folder(dir_path)
#        print(A1[0])
        fig = plt.figure()
        fig.add_axes([0.1,0.1,0.8,0.8])        
        TIME = range(0,240)
        Height=np.array([150,270,390,510,630,750,870,990,1110,1230,1350,1470,1590,1710,1830,1950,2070,2190,2310,2430,2550,2670,2790,2910,3030,3150,3270,3390,3510,3630,3750,3870,3990,4110,4350,4590,4830,5070,5310,5550,5790,6030,6270,6510,6750,6990,7230,7470,7710,7950,8190,8430,8670,8910,9150,9390,9630,9870,10110])
#        fig = plt.figure()
        im2 = plt.pcolor(TIME,Height,A1[1],cmap=plt.cm.jet)
        #im2.set_clim(vmin=1.8e-21,vmax=5.7e-17) #(cn2)
        #im2.set_clim(vmin=-2,vmax=2) #(VHS)
        im2.set_clim(vmin=0,vmax=35) #(HWS)
#        im2.set_clim(vmin=0,vmax=360)
        plt.title('Horizontal Wind Speed(m/s)')
        plt.colorbar(im2)
     
        cavans = FigureCanvas(fig)
        # 将绘制好的图像设置为中心 Widget
        self.setCentralWidget(cavans)
        
                    # 绘图方法
    def plot_VHS(self):
        # 清屏
        plt.cla()
        # 获取绘图并绘制
        dir_path=QFileDialog.getExistingDirectory()  #打开文件夹
        #A1 = fengyu.Get_Day_Cloud_Folder('D:\\try_matlab_to_C++\\robs - 副本')
        A1 = fengyu.Get_Day_Cloud_Folder(dir_path)
#        print(A1[0])
        fig = plt.figure()
        fig.add_axes([0.1,0.1,0.8,0.8])        
        TIME = range(0,240)
        Height=np.array([150,270,390,510,630,750,870,990,1110,1230,1350,1470,1590,1710,1830,1950,2070,2190,2310,2430,2550,2670,2790,2910,3030,3150,3270,3390,3510,3630,3750,3870,3990,4110,4350,4590,4830,5070,5310,5550,5790,6030,6270,6510,6750,6990,7230,7470,7710,7950,8190,8430,8670,8910,9150,9390,9630,9870,10110])
#        fig = plt.figure()
        im2 = plt.pcolor(TIME,Height,A1[2],cmap=plt.cm.jet)
        #im2.set_clim(vmin=1.8e-21,vmax=5.7e-17) #(cn2)
        im2.set_clim(vmin=-5,vmax=5) #(VHS)
        #im2.set_clim(vmin=0,vmax=35) #(HWS)
#        im2.set_clim(vmin=0,vmax=360)
        
        plt.title('Vertical Wind Speed(m/s)')
        plt.colorbar(im2)
     
        cavans = FigureCanvas(fig)
        # 将绘制好的图像设置为中心 Widget
        self.setCentralWidget(cavans)
        
    def plot_CN2(self):
        # 清屏
        plt.cla()
        # 获取绘图并绘制
        dir_path=QFileDialog.getExistingDirectory()  #打开文件夹
        #A1 = fengyu.Get_Day_Cloud_Folder('D:\\try_matlab_to_C++\\robs - 副本')
        A1 = fengyu.Get_Day_Cloud_Folder(dir_path)
#        print(A1[0])
        fig = plt.figure()
        fig.add_axes([0.1,0.1,0.8,0.8])        
        TIME = range(0,240)
        Height=np.array([150,270,390,510,630,750,870,990,1110,1230,1350,1470,1590,1710,1830,1950,2070,2190,2310,2430,2550,2670,2790,2910,3030,3150,3270,3390,3510,3630,3750,3870,3990,4110,4350,4590,4830,5070,5310,5550,5790,6030,6270,6510,6750,6990,7230,7470,7710,7950,8190,8430,8670,8910,9150,9390,9630,9870,10110])
#        fig = plt.figure()
        im2 = plt.pcolor(TIME,Height,np.log(A1[-1]),cmap=plt.cm.jet)
#        im2.set_clim(vmin=1e-21,vmax=6e-17) #(cn2)
        
#        im2.set_clim(vmin=1e-21*math.exp(-17),vmax=6e-17*math.exp(-17)) 
        
        #im2.set_clim(vmin=-2,vmax=2) #(VHS)
        #im2.set_clim(vmin=0,vmax=35) #(HWS)
#        im2.set_clim(vmin=0,vmax=360)
        plt.title('CN2 Index')
        plt.colorbar(im2)
#plt.show()
        
        cavans = FigureCanvas(fig)
        # 将绘制好的图像设置为中心 Widget
        self.setCentralWidget(cavans)
        
        
    def plot_RH(self):
        plt.cla()
        A = FunctionStart.FunctionRet()
        Z_RH = A[0]
#        Z_TEMP = A[1]
        TIME = A[3]
        Height = A[2]
        fig = plt.figure()
        fig.add_axes([0.1,0.1,0.8,0.8])
        
        im1 = plt.pcolor(TIME,Height,Z_RH,cmap=plt.cm.jet)
        im1.set_clim(vmin=0,vmax=100) 
        Colorbarsetting1 = plt.colorbar(im1)
        Colorbarsetting1.set_label('%')
        plt.xlabel('TIME')
        plt.ylabel('Height/m')
        plt.title('Relative Humidity Profile')
#        plt.show()
        cavans = FigureCanvas(fig)
        # 将绘制好的图像设置为中心 Widget
        self.setCentralWidget(cavans)
        
    def plot_TEMP(self):
        plt.cla()
        A = FunctionStart.FunctionRet()
#        Z_RH = A[0]
        Z_TEMP = A[1]
        TIME = A[3]
        Height = A[2]
        fig = plt.figure()
        fig.add_axes([0.1,0.1,0.8,0.8])
        
        im1 = plt.pcolor(TIME,Height,Z_TEMP,cmap=plt.cm.jet)
        im1.set_clim(vmin=-60,vmax=40) 
        Colorbarsetting1 = plt.colorbar(im1)
        Colorbarsetting1.set_label('℃')
        plt.xlabel('TIME')
        plt.ylabel('Height/m')
        plt.title('Temperature Profile')
#        plt.show()
        cavans = FigureCanvas(fig)
        # 将绘制好的图像设置为中心 Widget
        self.setCentralWidget(cavans)       
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_Main_window()
    main_window.show()
    app.exec()