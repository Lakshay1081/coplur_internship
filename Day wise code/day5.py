import pandas as pd

# a=[10,20,30,40,50]
# s=pd.Series(a)
# print(s)
# print(type(s))

# a=[10,20,30,40,50]
# s=pd.Series(a)
# print(s[1])
#
# a=[10,20,30,40,50]
# s=pd.Series(a,index=['a','b','c','d','e'])
# print(s)
# print(s["b"])


# ds={"num":[10,20,30,40,50],
#     "alpha":["a","b","c","d","e"]
#     }
# df=pd.DataFrame(ds)
# print(df)
# print(df.loc[1])
# print(df.loc[[0,1]])
# print(df.columns)
# df.columns=["cup","cake"]
# print(df)
# # print(pd.__version__)
#
# marks={"day1":583,"day2":483,"day3":390}
# var=pd.Series(marks,dtype=float,index=['day1','day2','day3'])
# print(var["day2"])

# df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']], columns=['col1', 'col2'],index=["r1","r2","r3","r4"])
# print(df)
# print("\n")
# result=df.loc["r1":"r3","col1"]
# print(result)

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print(df)
col_A=df.loc[1:,'A'] #idhar colon index ki range ke liye h
print(col_A)
col_A=df.loc[1:,'A':'B']
print(col_A)


df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']],columns=['col1', 'col2'])
print(df)
# df.iloc[1:3]=['x','y']
# print(df)
# df.iloc[1:3,0]=['x','y']
# print(df)
# df.iloc[1:3,1]=['x','y']
# print(df)
# result=df.drop(1)
# print(result)
# result=df.drop([0,1])
# print(result)
# result=df.drop(df.index[2])
# print(result)
result=df.drop(df.index[1:3])
print(result)
