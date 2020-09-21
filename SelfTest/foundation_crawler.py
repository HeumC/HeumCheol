# 没有bs4 的要自己下载安装 ，大名鼎鼎的BeautifulSoup 好用

# -*- coding: utf-8 -*-

"""

Created on Tue Nov 8 09:23:43 2016

@author: kingsun unix.cn@126.com

"""

import pandas as pd

from urllib.request import urlopen

from bs4 import BeautifulSoup

import datetime

#from io import StringIO

#import time

#import re

#col_name = ['A','B','C','D','E']

col_name = ['日期','基金代码','基金名称','当日净值','上日净值']

# 生成前一天时间戳字符串

date_time= datetime.datetime.now()-datetime.timedelta(days=1)

#print(date_time)

str_date_file_http = date_time.strftime('%Y%m%d')

str_date_file_found = date_time.strftime('%Y%m%d-%H-%M-%S')

#print(str_date_file_nmae)

str_http = "http://data.chinafund.cn/kf/"+str_date_file_http+".html"

#print(str_http)

html = urlopen(str_http)

bsObj = BeautifulSoup(html)

#print(bsObj.prettify())

nameList = bsObj.findAll("div", {"id":"content"}) #抓取内容定位，要人工分析网页原始代码

for name in nameList:

    yuanshistr = name.get_text(",") # 原始文件用‘，’逗号分割。

#print(yuanshistr)

##原始串整形,为了将来将字符数字变换为数字做准备

yuanshistr = yuanshistr.replace('--','0.0')

###返回原始串的行

yuanshistr_row = yuanshistr.splitlines()

data1=[]

for line in yuanshistr_row:

    line_split = line.split(',') #依据逗号切分从文件中读取的行

#print(line_split[:6])

    data1+=[line_split[1:6]] #取每一行的前5咧，不断累加到 data[]中

df = pd.DataFrame(data1,columns =col_name)

df = df[4:] #截取有效数据,前面几行有无效数据

#转换为数字类型

for i in range(3,5):

    df[[col_name[i]]]=df[[col_name[i]]].astype(float)

print(df[0:6])

writerfile = ('f:/found_day_value/'+str_date_file_found+'.xlsx')

df[0:].to_excel(writerfile,'Sheet1')