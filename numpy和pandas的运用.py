import pandas as pd
import numpy as np
a = np.random.random((3,4))#形成3行4列0到1之间的小数
print(a)
aa = np.copy(a)

b = np.arange(24)#0到23按顺序生成一列
c = a.reshape((4,3))
print(c)
d = a.dot(c) #矩阵相乘
print(d.shape)
f = np.vstack((a,aa))
print(f)

# axios 0 行 1 列
dates = pd.date_range('20190517',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns = ['A','B','C','D'])
print(df)
# loc 利用名字来筛选， 行列的名字
print('loc:')
print(df.loc['20190517'])
print('loc:2')
print(df.loc['20190517',['A','B']])

# iloc 利用index来筛选，行列的数字

print(df.iloc[[1,3,5],1:3])

df.C[df.A>16] = np.nan
print(df)

df_drop = df.dropna(axis = 0,how='any')#how可以为any或者all，all为整一行或列的为NaN的时候才会删除，any的话是有一个即会删除整列或行

print(df)#由此可以说明，df.dropna是不会改变原来的df的,应该要接收返回值
print(df_drop)

print(np.any(df.isnull())==True) #可以把整个数据查一次看看有没有NaN的值，可以用df.fillna(value = )来对NaN的值进行填充
#df.fillna(method = 'ffill',axis=) 向前一列或者前一行取值来填充NaN ，method = 'backfill'时向后 ，method = 'linear'的时候为取上下的平均值 ，这函数都不会改变原有的df，必须要有一个返回值接受
df_null = df.isnull()
df.C[df_null.C==True]=0
print(df.isnull())
print(df)
df_2 = pd.DataFrame(np.ones((3,4)),columns=['A','B','C','D'])
df_3 = pd.DataFrame(np.ones((3,4)),columns=['B','C','D','P'])
ronhe = pd.concat([df_2,df],axis = 0,ignore_index=True)#ignore_index为true时重新排列index
print(ronhe)

ronhe = pd.concat([df_2,df_3],axis=0,join='inner')#m默认是outer，outer的话会全部合并并且把没有的部分用nan来替代，inner的话就只保留相同的来合并

print(ronhe)