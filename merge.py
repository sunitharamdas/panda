import pandas as pd
from pandas import *
import numpy as np
import csv
from tabulate import tabulate
import matplotlib.pyplot as plt

#data = pd.read_csv('file11.csv',sep='|',parse_dates=True,index_col=1)
#tabdata = tabulate(data,['Date-Time','Field_userid','product_name','Platform','App_type','Search_term','Pageurl','Region','Additional_info'],tablefmt="grid")
#print(tabdata)
# print(table)
# qa
# qa qa qa qa qa
print("this is qa")
print("yes it is")
print("from here i want new branch")
print("add logging")






data0 = pd.read_csv('file0.csv',sep='|',index_col=1,parse_dates=True)
data1 = pd.read_csv('file1.csv',sep='|',index_col=1,parse_dates=True)
data2 = pd.read_csv('file2.csv',sep='|',index_col=1,parse_dates=True)
data3 = pd.read_csv('file3.csv',sep='|',index_col=1,parse_dates=True)
data4 = pd.read_csv('file4.csv',sep='|',index_col=1,parse_dates=True)
data5 = pd.read_csv('file5.csv',sep='|',index_col=1,parse_dates=True)
data6 = pd.read_csv('file6.csv',sep='|',index_col=1,parse_dates=True)
data7 = pd.read_csv('file7.csv',sep='|',index_col=1,parse_dates=True)
#print(data1)
#print(tabulate(data1.head()))
#print(data1.head())

df0 = pd.DataFrame({'UESRID':data0.UESRID,'PLATFORM':data0.PLATFORM,'APPTYPE':data0.APPTYPE,'PRODUCT':data0.PRODUCT,'NAME':data0.NAME,'PAGEURL':data0.PAGEURL,'REGION':data0.REGION})
df1 = pd.DataFrame({'UESRID':data1.UESRID,'PLATFORM':data1.PLATFORM,'APPTYPE':data1.APPTYPE,'PRODUCT':data1.PRODUCT,'NAME':data1.NAME,'PAGEURL':data1.PAGEURL,'REGION':data1.REGION})
df2 = pd.DataFrame({'UESRID':data2.UESRID,'PLATFORM':data2.PLATFORM,'APPTYPE':data2.APPTYPE,'PRODUCT':data2.PRODUCT,'NAME':data2.NAME,'PAGEURL':data2.PAGEURL,'REGION':data2.REGION})
df3 = pd.DataFrame({'UESRID':data3.UESRID,'PLATFORM':data3.PLATFORM,'APPTYPE':data3.APPTYPE,'PRODUCT':data3.PRODUCT,'NAME':data3.NAME,'PAGEURL':data3.PAGEURL,'REGION':data3.REGION})
df4 = pd.DataFrame({'UESRID':data4.UESRID,'PLATFORM':data4.PLATFORM,'APPTYPE':data4.APPTYPE,'PRODUCT':data4.PRODUCT,'NAME':data4.NAME,'PAGEURL':data4.PAGEURL,'REGION':data4.REGION})
df5 = pd.DataFrame({'UESRID':data5.UESRID,'PLATFORM':data5.PLATFORM,'APPTYPE':data5.APPTYPE,'PRODUCT':data5.PRODUCT,'NAME':data5.NAME,'PAGEURL':data5.PAGEURL,'REGION':data5.REGION})
df6 = pd.DataFrame({'UESRID':data6.UESRID,'PLATFORM':data6.PLATFORM,'APPTYPE':data6.APPTYPE,'PRODUCT':data6.PRODUCT,'NAME':data6.NAME,'PAGEURL':data6.PAGEURL,'REGION':data6.REGION})
df7 = pd.DataFrame({'UESRID':data7.UESRID,'PLATFORM':data7.PLATFORM,'APPTYPE':data7.APPTYPE,'PRODUCT':data7.PRODUCT,'NAME':data7.NAME,'PAGEURL':data7.PAGEURL,'REGION':data7.REGION})



#print(df3)
#frames = [df0,df1,df2,df3,df4,df5,df6,df7]
#all_data = pd.concat(frames,join='outer')
#print(all_data.head())


#print(df2.head())

frames = [df0,df1,df2,df3,df4,df5,df6,df7]
all_data = pd.concat(frames)
#print('Total number of records in all files is :' + str(len(all_data)))

#groupby
#x = all_data.groupby('Product_name').size()
#print(x)

#a = all_data.groupby('Search_term').size()
#print(a.head)

#b = all_data.groupby('Region')['Product_name'].describe()
#print(b)

#c = all_data['Region'].describe()
#print( c )

#sorting
#d = all_data[all_data.Region == 'south east'].sort_values(by='platform',ascending=True)
#print(d.platform)


#e = data1.groupby('Region')['platform'].describe()
#f = data1.groupby('Region')['product_name'].describe()
#g = all_data.groupby('Region')['Search_term'].describe()
#h = all_data.groupby('Region')['pageurl '].describe()
#print(h)

#a = all_data[all_data.Field == '1a1cc07ac4f2daa629a8e2e77c269126']
#print(len(a))

#Product_name = all_data.groupby('Product_name').size()
#platform = all_data.groupby('platform').size()
#Search_term = all_data.groupby('Search_term').size()
#App_type = all_data.groupby('App_type').size()
#Products = all_data.groupby('Product_name').size()
#print(Product_name)
#print('THE INDIVIDUAL COUNT OF ' + str(b))


'''
print('TOTAL NUMBER OF DIFFERENT  USERS  ' + str(len(users)))
print('TOTAL NUMBER OF DIFFERENT PRODUCTS  ' + str(len(Products)))
print('TOTAL NUMBER OF DIFFERENT  SEARCH TERMS  ' + str(len(Search_term)))
print('TOTAL NUMBER OF DIFFERENT  APPS  ' + str(len(App_type)))
print('TOTAL NUMBER OF DIFFERENT  PRODUCTS  ' + str(len(Products)))
'''

#print(Products)
#print(Search_term)
#df = pd.DataFrame({'Search_term':all_data.Search_term,'User_id':all_data.Userids})
#h = df[df.Search_term == 'weather.page']
#print('weather.page is present in  ' + str(len(h)) + '   records.')
#print(h)
'''
------------------------------------------------------------------------------------------------------
'''
'''
UESRID = all_data.groupby('UESRID').size()
PLATFORM = all_data.groupby('PLATFORM').size()
APPTYPE = all_data.groupby('APPTYPE').size()
PRODUCT = all_data.groupby('PRODUCT').size()
NAME = all_data.groupby('NAME').size()
PAGEURL = all_data.groupby('PAGEURL').size()
REGION = all_data.groupby('REGION').size()


print('TOTAL NUMBER OF DIFFERENT  USERS  ' + str(len(UESRID)))
print('TOTAL NUMBER OF DIFFERENT  PLATFORMS  ' + str(len(PLATFORM)))
print('TOTAL NUMBER OF DIFFERENT  APPS  ' + str(len(APPTYPE)))
print('TOTAL NUMBER OF DIFFERENT PRODUCTS  ' + str(len(PRODUCT)))
print('TOTAL NUMBER OF DIFFERENT  NAMES ' + str(len(NAME)))
print('TOTAL NUMBER OF DIFFERENT  PAGE URLS ' + str(len(PAGEURL)))
print('TOTAL NUMBER OF DIFFERENT  REGIONS  ' + str(len(REGION)))
---------------------------------------------------------------------------------------------------
'''
#a = all_data[all_data.USERID]
#print(a)
'''
c = all_data['NAME'].describe()
print('1 . COUNT OF VIEWED PAGES , UNIQUE PAGES , MAXIMUM VIEWED PAGE , FREQUENCY:')
print(c)
print('\n')
d = all_data['APPTYPE'].describe()
print('2 . COUNT OF APPTYPE , UNIQUE APPTYPE , CONTENT IS DELIVERED TO THE BROWSER MOSTLY , FREQUENCY:')
print(d)
print('\n')
e = all_data['UESRID'].describe()
print('3. COUNT OF USERIDS , UNIQUE USERIDS , USERID OF MAXIMUM REQUESTS ,FREQUENCY :')
print(e)
print('\n')
f = all_data['PLATFORM'].describe()
print('4. COUNT OF PLATFORMS , UNIQUE PLATFORMS , MAXIMUM USED PLATFORM TO ACCESS THE CONTENTS ,FREQUENCY :')
print(f)

g = all_data['PRODUCT'].describe()
print('5 . COUNT OF PRODUCTS  , UNIQUE PRODUCTS , MAXIMUM THE CONTENT IS PART OF BBC PRODUCT  , FREQUENCY:')
print(g)
print('\n')
g = all_data['PAGEURL'].describe()
print('6 . COUNT OF PAGEURLS  , UNIQUE PAGEURLS , WEB ADDRESS OF THE MAXIMUM VIEWED PAGE  , FREQUENCY:')
print(g)
print('\n')
g = all_data['REGION'].describe()
print('7 . COUNT OF REGIONS  , UNIQUE REGIONS , GEOGRAPHICAL REGION WHERE THE BROWSER APPEARS TO HAVE ARRIVED FROM MOSTLY  , FREQUENCY:')
print(g)
print('\n')
'''

#b = all_data.groupby('REGION')['APPTYPE'].describe()
#print(b)
#b = all_data.groupby('APPTYPE')['PLATFORM'].describe()
#print(b)
#d = all_data[all_data.REGION == 'south east'].sort_values(by='PLATFORM',ascending=True)
#print(d.PLATFORM)
df = pd.DataFrame({'NAME':all_data.NAME,'UESRID':all_data.UESRID})
h = df[df.NAME == 'weather.page']
print('\'weather.page \' IS PRESENT IN   ' + str(len(h)) + '  RECORDS.')
print(h)
