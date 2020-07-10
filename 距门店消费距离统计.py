#!/usr/bin/emv python
# -*- coding:utf-8 -*-
# author 7z time:2020/7/10
import pandas as pd
import  plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go

o2oOffline = pd.read_csv('o2o.csv')
userCounts = o2oOffline['Distance'].value_counts()
print(userCounts)
x = []
y = []
for i in range(0, len(userCounts)):
    x.append(userCounts.index[i]*500)
    y.append(userCounts.values[i])
# data = go.Scatter(x = x,y=y,mode='lines')
# fig = go.Figure(data)
# fig.show()
fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto', # 标注位置自动调整
        )])
fig.show()
