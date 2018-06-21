import pandas as pd
import numpy as np

df1=pd.read_excel('zhuanxian.xlsx')
'''df2=pd.read_excel('tasklist.xlsx')
df3=pd.read_excel('uselist.xlsx') '''
print(df1.groupby('备注').agg({'数量':np.sum}))
