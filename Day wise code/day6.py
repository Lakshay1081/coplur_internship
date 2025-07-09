import pandas as pd

from Assignments.assignment_5 import result

# data={'A':[1,2,3],'B':[4,5,6]}
# df=pd.DataFrame(data)
# print(df)
# result=df*2
# print("Multiplication: \n",result)
# print("Addition: \n",df+2)
# print("Division: \n",df/2)
# print("Subtraction: \n",df-2)
# result=df['A']+df['B']
# print("Addition of A and B \n",result)
# df['C']=df['A']+df['B']
# print("C = \n",df)
#
#
# df2=pd.DataFrame({'A':[1,2,3,4],'B':[4,5,6,7]})
# df3=pd.DataFrame({'A':[51,52,53,54],'B':[54,55,56,57]})
# print(df2)
# print(df3)
# print("\nAddition of 2 DataFrames is : \n",df2+df3)
# print("\nSubtraction of 2 DataFrames is : \n",df2-df3)
# print("\nMultiplication of 2 DataFrames is : \n",df2*df3)
# print("\nDividion of 2 DataFrames is : \n",df2/df3)


# one= pd.DataFrame({
#     'Name':['K1','K2','K3','K4','K5'],
#     'Subject':['M','J','P','D','C'],
#     'Marks':[89,90,91,92,93]},
#     index=[1,2,3,4,5]
# )
# two= pd.DataFrame({
#     'Name':['L1','L2','L3','L4','L5'],
#     'Subject':['M','J','P','D','C'],
#     'Marks':[81,82,83,84,85]},
#     index=[1,2,3,4,5]
# )
# result=pd.concat([one,two])
# print(result)
# result=pd.concat([one,two],keys=['a','b'])
# print("\n",result)
# result=pd.concat([one,two],keys=['a','b'],ignore_index=True)
# print(result)
# result=pd.concat([one,two],keys=['a','b'],axis=1)
# print("\n",result)

# right= pd.DataFrame({
#     'Id':[1,2,3,4,5],
#     'Name':['K1','K2','K3','K4','K5'],
#     'Subject':['M','J','P','D','C'],
#     'Marks':[89,82,91,92,93]},
# )
# left= pd.DataFrame({
#     'Id':[1,2,3,4,5],
#     'Name':['L1','L2','L3','L4','L5'],
#     'Subject':['M','J','P','D','C'],
#     'Marks':[81,82,83,84,85]},
# )
#
# result=left.merge(right,on='Id')
# print("\n",result)
# result=left.merge(right,on='Subject')
# print("\n",result)
# result=left.merge(right,on=['Subject','Id'])
# print("\n",result)
# result=left.merge(right,on='Marks',how='left')
# print("\n",result)
# result=left.merge(right,on='Marks',how='right')
# print("\n",result)
# result=left.merge(right,on='Marks',how='outer')
# print("\n",result)
# result=left.merge(right,on='Marks',how='inner')
# print("\n",result)
# result=left.merge(right,how='cross')
# print("\n",result)
#
# result=left.join(right,rsuffix="_right",lsuffix="_left")
# print("\n",result)
#
# '''Pivot'''
# df=pd.DataFrame({"col1":range(12),"col2":['A','A','A','B','B','B','C','C','C','D','D','D']
#                  , "date":pd.to_datetime(["2025-06-20","2025-06-21","2025-06-22"]*4)
#                  })
# print(df)
# result=df.pivot(index="date",columns="col2",values="col1")
# print("\n",result)
# result=df.pivot(index="date",columns="col1",values="col2")
# print("\n",result)

Data={
    'Course':['civil','cs','civil','cs','civil'],
    'Year':[1,2,1,1,1],
    'student':[100,200,100,100,500]}
df=pd.DataFrame(Data)
print(df)
result=df.pivot_table(
    index='Course',columns='Year',values='student',aggfunc='sum'
)
print("\n",result)