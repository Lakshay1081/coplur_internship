import pandas as pd
import numpy as np

# data={'col1':[3,np.nan,np.nan,2],'col2':[1.0,pd.NA,pd.NA,2.0]}
# df=pd.DataFrame(data)
# print(df)
#
# f=df.fillna('-')
# print("\n",f)
#
# df=pd.DataFrame([[5,6,7],[8,9,10],[11,12,13]],
#                 index=['a','b','e'],columns=['one','two','three']
#                 )
# df=df.reindex(['a','b','c','d','e'])
# print(df)
#
# result=df.ffill()
# print("\n",result)
#
# result=df.bfill()
# print("\n",result)
#
# result=df.ffill(limit=1)
# print("\n",result)
#
# result=df.bfill(limit=1)
# print("\n",result)

# df=pd.DataFrame([[5,6,7],[8,9,10],[11,12,13]],
#                 index=['a','b','e'],columns=['one','two','three']
#                 )
# df=df.reindex(['a','b','c','d','e'])
# print(df)
# result=df.replace({5:6,7:0})
# print("\n",result)
#
# df=pd.DataFrame(['$40.000*','$40000 condition attached'],
#                 columns=['one']
#                 )
# print(df)
#
# df['one']=df['one'].str.replace(r'\D+','',regex=True).astype('int')
# print(df)
#
# """ GROUPBY """
# data = {
#     'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT'],
#     'Employee': ['A', 'B', 'C', 'D', 'E'],
#     'Salary': [30000, 35000, 25000, 26000, 40000]
# }
# df = pd.DataFrame(data)
# grouped=df.groupby('Employee')['Salary'].sum()
# print(grouped)
#
# grouped=df.groupby('Employee')['Salary'].count()
# print(grouped)
#
# data = {
#     'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT'],
#     'Employee': ['A', 'A', 'C', 'C', 'E'],
#     'Salary': [30000, 35000, 25000, 26000, 40000]
# }
# df = pd.DataFrame(data)
# grouped=df.groupby(['Employee','Department'])['Salary'].mean()
# print(grouped)


""" SORT """

# data={"Name":['LAK','LAK','JKL','BHA'],"Age":[21,20,22,19]}
# df=pd.DataFrame(data)
# result=df.sort_values(by='Name')
# print(result)
# result=df.sort_values(by=['Name','Age'],ascending=[True,True])
# print(result)
# result=df.sort_index(ascending=False)
# print(result)
# result=pd.date_range("6/1/25",periods=5) #print aage ki dates print karne ke kaam aata h n values tak
# print(result)

""" CSV in Dataframe"""
df=pd.read_csv('data.csv')
# print(df['First Name'].value_counts())
# print(df.to_string())
# print(df.head(5))
# print(df.tail(5))
# print(df.info(5))
# print(df.describe())
# print(df.shape)
# print(df.columns)
# print(df['First Name'])

# filrered_df=df[df['columns_column']]
# print(filrered_df,head())

# group_data=df.groupby('City')['Index'].count()
# print(group_data)
# group_data=df.groupby('City')['Index'].mean()
# print(group_data)

# pd.options.display.max_rows =999
# pd.options.display.max_columns =999
# df = pd.read_csv('data.csv')
# print(df)

df=pd.read_csv('data.csv')
x=df["index"].mean()
