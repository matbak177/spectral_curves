import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from simpledbf import Dbf5
import os
%matplotlib inline

#change path
folder=r'C:\Users\mateusz.bak\Desktop\programs\spectral'
daty = [x for x in os.listdir(folder) if x.startswith('2020')] 

#names of variables
list=['data','las iglasty','las lisciasty','trawa','woda stojąca','woda płynąca','zabudowa']
nazwy=['trw','ws','wp','zab','igl','lisc']

col1=['data','obiekt','band','max','min','mean','max-min']
col2=['data','obiekt','band','max_after','min_after','mean_after','max-min_after']
band=['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12']
tab1=pd.DataFrame(columns=col1)
tab2=pd.DataFrame(columns=col2)

#load the files
def load(path):
    file=Dbf5(path)
    file=file.to_dataframe()
    file_c=file.copy()
    return file_c

#drop values -  5% of all , and create table
def nugget(df,cl1,cl2):#
    x=int(len(df)*5/200)#you can change how many values you want to drop (present 5%)
    df.drop(columns=df.columns[0],axis=1,inplace=True)
    
    tb1=pd.DataFrame(columns=col1)
    for i,b in zip(df.columns,band):
        value={cl1[0]:d,cl1[1]:p,cl1[2]:b,cl1[3]:df[i].max(),cl1[4]:df[i].min(),cl1[5]:df[i].mean(),cl1[6]:(df[i].max()-df[i].min())}
        tb1=tb1.append(value,ignore_index=True)
    
    for i in df.columns:
        df=df.sort_values(i)
        if (df[i].max()-df[i].min())>100: #you can change the value of the difference in which the deletion will not be performed 
            for j in df[-x:].index.values:
                df.loc[j,i]=np.nan
            for j in df[:x].index.values:
                df.loc[j,i]=np.nan
        else:
            print('in column {} the difference is below the given value'.format(i))
            
    tb2=pd.DataFrame(columns=col2)
    for i,b in zip(df.columns,band):
        value={cl2[0]:d,cl2[1]:p,cl2[2]:b,cl2[3]:df[i].max(),cl2[4]:df[i].min(),cl2[5]:df[i].mean(),cl2[6]:(df[i].max()-df[i].min())}
        tb2=tb2.append(value,ignore_index=True)
        
    return df,tb1,tb2

#Create bands with average values ​​on each of the dates 
def add(q,nr,li,ll,tr,ws,wp,zab):
    #nr - date position number
    q=q-1    
    for i,l,r,s,p,z in zip(li.columns[q:],ll.columns[q:],tr.columns[q:],ws.columns[q:],wp.columns[q:],zab.columns[q:]):
        dict={list[0]:daty[nr],list[1]:li[i].mean(),list[2]:ll[l].mean(),list[3]:tr[r].mean(),list[4]:ws[s].mean(),list[5]:wp[p].mean(),list[6]:zab[z].mean()}
        break
    return dict

#Run of functions
q=0
for d in daty:
    q+=1
    folder2=os.path.join(folder,d)
    files=[x for x in os.listdir(folder2) if x.endswith('p.dbf')]
    
    for o,p in zip(files,nazwy):

        path=(os.path.join(folder,d,o))
        exec('{}=load(path)'.format(p+str(q)))
        print('load file {}{}'.format(d,o))
        exec('{},tba1,tba2=nugget({},col1,col2)'.format(p+str(q),p+str(q)))
        tab1=tab1.append(tba1,ignore_index=True)
        tab2=tab2.append(tba2,ignore_index=True)            

    print('----------')

for q in range(1,13):
    exec('b{}=pd.DataFrame(columns=list)'.format(q))     

    for i in daty:
        i=daty.index(i)+1
        exec('dic=add(q,(i-1),igl{},lisc{},trw{},ws{},wp{},zab{})'.format(i,i,i,i,i,i))
        exec('b{}=b{}.append(dic,ignore_index=True)'.format(q,q))
    
#Joining the table and saving the DataFrame table to csv
tabela=tab1.merge(tab2)
tabela.to_csv((os.path.join(folder,"Tabela_wartosci.csv")),index=False,header=True)
              
#Creation of charts
list1=list[1:]

b1.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 1')
b2.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 2')
b3.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 3')
b4.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 4')

b5.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 5')
b6.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 6')
b7.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 7')
b8.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 8')

b9.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 9')
b10.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 10')
b11.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 11')
b12.plot(kind='line',x='data',y=list1,figsize=(15,8),title='Band 12')
               


 

             
