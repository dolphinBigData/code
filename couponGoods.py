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
userCounts = o2oOffline['Merchant_id'].value_counts()
x = userCounts.index[1]
print(userCounts.values)
OneL = 0
TwoL = 0
ThreeL = 0
FourL = 0
for i in userCounts.values:
    if i >= 10000:
        OneL += i
    if i>=5000 and i<10000:
        TwoL += i
    if i>=1000 and i<5000:
        ThreeL +=i
    if i<1000:
        FourL +=i

idCount = len(o2oOffline['Merchant_id'])
print(OneL, TwoL, ThreeL, FourL)
OneL = 75382/1754884
TwoL = 977900/1754884
ThreeL = 701602/1754884
FourL = 0/1754884
userL = ['有优惠券，购买商品', '有优惠券，未购商品', '无优惠券，购买商品', '有优惠券，未购商品']
values = [OneL, TwoL, ThreeL, FourL]
fig = px.pie(
            values=values,  # 饼状图大小
            names=userL,  # 饼状图label
            title='优惠券对购买商品分析图' # 图名
)
fig.show()