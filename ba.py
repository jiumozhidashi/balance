import pandas as pd

df=pd.read_excel('zhuanxian.xlsx')
print(df.head())
print(df.columns)
print(df['数量'].max())
print(df['数量'].min())
print(df['数量'].mean())