# -*- coding: utf-8 -*-

import pandas as pd

data=pd.read_excel('F:/lnmhack/Online Retail.xlsx')
print('a')
no_of_cust=data.CustomerID.unique()
data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
pd.to_datetime(data.InvoiceDate)
data.drop(['UnitPrice', 'Country'], axis = 1,inplace=True) 
data.sort_values('InvoiceDate',inplace=True,ascending=False)
print('a')

null_columns=data.columns[data.isnull().any()]
data[null_columns].isnull().sum()

print('a')
data=data[['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','Status','Complaint','CustomerID']]
new_data={}
for i in range(len(data)):
    lis=list(data.iloc[i,:])
    lst=new_data.get(lis[-1],[])
    lst.append(lis[:-1])
    new_data[lis[-1]]=lst
data3=data.iloc[:100000,:]
data3.to_csv('file2.csv') 

order_status=['Order recieved','Order packed and ready to be shipped','In transit','Out for delivery','Delivered']
new_col=[]
import random
for x in range(406829):
  i=random.randint(0,4)
  new_col.append(order_status[i])

complaint=['Return','Replaced','Wrong product delivered','Product faulty','None']
new_col_2=[]
from random import choices
population = [0, 1, 2, 3, 4]
weights = [0.2, 0.033, 0.033, 0.034, 0.7]
for x in range(406829):
    i=choices(population, weights)
    #print(i)
    i=i[0]
    new_col_2.append(complaint[i])
    

data['Status'] = new_col
data['Complaint']=new_col_2



names=pd.read_csv('baby-names.csv')
names_lst=names.name.unique()
data['CustomerID']=data['CustomerID'].astype('int')
no_of_cust=no_of_cust.sort()
name_dict={}
for i in range(len(no_of_cust)):
    name_dict[no_of_cust[i]]=names_lst[i]
mob_lst=[]
mob=''
for x in range(4372):
    mob=''
    for j in range(10):
        i=random.randint(0,9)
        mob+=str(i)
    print(mob)
    
    mob_lst.append(int(mob))


phone_dict={}
for i in range(len(no_of_cust)):
    phone_dict[no_of_cust[i]]=mob_lst[i]



import pickle
with open('filename.pickle', 'wb') as handle:
    pickle.dump(new_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)

#
#for x in range(1000):
#  i=random.randint(0,)
#  new_col.append(order_status[i])



data2=pd.DataFrame(no_of_cust[:1000],columns=['CustID'])
data2['Names'] = names_lst[:1000]















