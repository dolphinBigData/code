#!/usr/bin/emv python
# -*- coding:utf-8 -*-
# author 7z time:2020/7/9
import pandas as pd
import  plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go



o2oOnline = pd.read_csv('ccf_online_stage1_train.csv')
o2oOffline = pd.read_csv('o2o.csv')
o2oOfflineTest = pd.read_csv('ccf_offline_stage1_test_revised.csv')
# print(o2oOffline)
# print(o2oOnline.shape)
# print(o2oOffline.shape)
# print(o2oOfflineTest.shape)
print(o2oOffline.shape)
o2oOffline = o2oOffline.dropna(subset=['Coupon_id'])
print(o2oOffline.shape)
# o2oOffline['Date'] = o2oOffline['Date'].fillna('20200000')
# o2oOffline.to_csv('o2o.csv')
print(o2oOffline.head(10))
print(o2oOffline.loc[1]['Date'])
day1 = 0
day2 = 0
day3 = 0
day4 = 0
day5 = 0
day6 = 0
day7 = 0
day8 = 0
day9 = 0
day10 = 0
day11= 0
day12= 0
day13= 0
day14= 0
day15= 0
day16= 0
day17= 0
day18 = 0
day19 = 0
day20 = 0
day21 = 0
day22 = 0
day23 = 0
day24 = 0
day25 = 0
day26 = 0
day27 = 0
day28 = 0
day29 = 0
day30 = 0
mouth = 0
wan = 0
#print(int(o2oOffline.loc[5]['Date']) - int(o2oOffline.loc[5]['Date_received']))
for i in range(1, len(o2oOffline)):
    #print(i)
    count = int(o2oOffline.loc[i]['Date']) - int(o2oOffline.loc[i]['Date_received'])
    if count >=30 and count<170:
        count = count-70
    elif count >=170 and count<500:
        mouth = mouth+1
    elif count >10000:
        wan = wan+1
    if count == 1:
        day1 = day1 + 1
    elif count == 2:
        day2 = day2 + 1
    elif count == 3:
        day3 = day3 + 1
    elif count == 4:
        day4 = day4 + 1
    elif count == 5:
        day5 = day5 + 1
    elif count == 6:
        day6 = day6 + 1
    elif count == 7:
        day7 = day7 + 1
    elif count == 8:
        day8 = day8 + 1
    elif count == 9:
        day9 = day9 + 1
    elif count == 10:
        day10 = day10 + 1
    elif count == 11:
        day11 = day11 + 1
    elif count == 12:
        day12 = day12 + 1
    elif count == 13:
        day13 = day13 + 1
    elif count == 14:
        day14 = day14 + 1
    elif count == 15:
        day15 = day15 + 1
    elif count == 16:
        day16 = day16 + 1
    elif count == 17:
        day17 = day17 + 1
    elif count == 18:
        day18 = day18 + 1
    elif count == 19:
        day19 = day19 + 1
    elif count == 20:
        day20 = day20 + 1
    elif count == 21:
        day21 = day21 + 1
    elif count == 22:
        day22 = day22 + 1
    elif count == 23:
        day23 = day23 + 1
    elif count == 24:
        day24 = day24 + 1
    elif count == 25:
        day25 = day25 + 1
    elif count == 26:
        day26 = day26 + 1
    elif count == 27:
        day27 = day27 + 1
    elif count == 28:
        day28 = day28 + 1
    elif count == 29:
        day29 = day29 + 1
    elif count == 30:
        day30 = day30 + 1


    print('day1:'+str(day1))
    print('day2:'+str(day2))
    print('day3:' + str(day3))
    print('day4:' + str(day4))
    print('day5:' + str(day5))
    print('day6:' + str(day6))
    print('day7:' + str(day7))
    print('当前循环：'+str(i))
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,]
y = [day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13,day14,day15,day16,day17,day18,day19,day20,day21,day22,day23,day24,day25,day26,day27,day28,day29,day30]
data = go.Scatter(x = x,y=y,mode='lines')
fig = go.Figure(data)
fig.show()

