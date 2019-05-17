import pandas as pd
import numpy as np
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