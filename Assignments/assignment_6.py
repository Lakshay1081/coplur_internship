import pandas as pd


""" Convert series of date string to time series """

date = pd.Series(['2025-06-25 14:30:00', '2025-06-26 15:45:00', '2025-06-27 09:15:00'])
s = pd.to_datetime(date)
print(s)

""" Create two DataFrames, df1 and df2, with a common column (e.g., 'ID').
Perform an inner merge on this common column and display the resulting DataFrame.
Perform a left join of df1 and df2 on the 'ID' column. 
Explain how missing values are handled in the resulting DataFrame. Right Join and Index-Based Join"""

df1=pd.DataFrame({'id':[1,2,3,4,5],
      'name':['a','b','c','d','e']
      })
print(df1)

df2=pd.DataFrame({'id':[1,2,6,7,8],
      'name':['f','g','h','i','j']
      })
print("\n",df2)
print("\n------------INNER MERGE--------------")
result=df1.merge(df2,on='id',how='inner')
print("Inner merge:\n",result)

print("\n------------LEFT JOIN--------------")

result=df1.merge(df2,on='id',how='left')
print(result)

print("\n------------RIGHT JOIN--------------")

result=df1.merge(df2,on='id',how='left')
print(result)

print("\n------------RIGHT JOIN--------------")
result=df1.join(df2,rsuffix='_right',lsuffix='_left')
print(result)

"""Create three DataFrames. Vertically concatenate two of them using pd.concat(), 
then merge the resulting DataFrame with the third DataFrame on a common key. 
T Understand join() vs. merge()."""

df1 = pd.DataFrame({'ID': [1, 2], 'Marks': [88, 92]})
df2 = pd.DataFrame({'ID': [3, 4], 'Marks': [76, 85]})
df3 = pd.DataFrame({'ID': [1, 2, 3, 4], 'Grade': ['A', 'A', 'B', 'B']})
result = pd.concat([df1, df2],ignore_index=True)
print("\nConcatenated DataFrame:\n",result)
result = pd.merge(result, df3, on='ID')
print("\nFinal Merged Result:\n",result)
