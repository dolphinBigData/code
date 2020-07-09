#!/usr/bin/emv python
# -*- coding:utf-8 -*-
# author 7z time:2020/7/9
import pandas as pd
import  plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go

def dropNull(file):
    file = file.dropna(subset=['Coupon_id'])
    return


o2oOnline = pd.read_csv('ccf_online_stage1_train.csv')
o2oOffline = pd.read_csv('ccf_offline_stage1_train.csv')
o2oOfflineTest = pd.read_csv('ccf_offline_stage1_test_revised.csv')
# print(o2oOffline)
# print(o2oOnline.shape)
# print(o2oOffline.shape)
# print(o2oOfflineTest.shape)
dropNull(o2oOffline)
print(o2oOffline.shape)
userCounts = o2oOffline['User_id'].value_counts()
x = userCounts.index[1]
print(userCounts.values)
OneL = 0
TwoL = 0
ThreeL = 0
FourL = 0
for i in userCounts.values:
    if i >= 70:
        OneL += i
    if i>=30 and i<70:
        TwoL += i
    if i>=10 and i<30:
        ThreeL +=i
    if i<10:
        FourL +=i
print(OneL, TwoL, ThreeL, FourL)
OneL = OneL/len(o2oOffline['User_id'])
TwoL = TwoL/len(o2oOffline['User_id'])
ThreeL = ThreeL/len(o2oOffline['User_id'])
FourL = FourL/len(o2oOffline['User_id'])
userL = ['一级用户', '二级用户', '三级用户', '四级用户']
values = [OneL, TwoL, ThreeL, FourL]
fig = px.pie(
            values=values,  # 饼状图大小
            names=userL,  # 饼状图label
            title='用户消费分析图' # 图名
)
fig.show()