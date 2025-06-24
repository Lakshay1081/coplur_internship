""" PANDAS SERIES"""
import pandas as pd

print("Pandas Series from Dictionary")
l={'a':10,'b':20,'c':30,'d':40,'e':50}
series=pd.Series(l)
print(series)
print(series['a'])
print((series['a'], series['c']))

print("\nPandas Series from List")
l=[10,20,30,40,50]
series=pd.Series(l)
print(series)
print(series[1])
print(series[[1,3]])

""" PANDAS DATAFRAME """

print("\nPandas DataFrame with a two-dimensional Python list")
data = [['Lakshay', 20], ['Shivam', 21], ['Suchitra', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

print("\nDataFrame from Python dict")
data = {'Name': ['Lakshay', 'Shivam', 'Suchitra'],
        'Age': [20, 21, 22]}
df = pd.DataFrame(data)
print(df)

print("\nPandas DataFrame using list of lists")
data = [['Lakshay', 20], ['Shivam', 21], ['Suchitra', 22]]
df = pd.DataFrame(data, columns=['Name', 'age'])
print(df)

print("\nPandas DataFrame using list of tuples")
data = [('Lakshay', 20), ('Shivam', 21), ('Suchitra', 22)]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

print("\nPandas DataFrame from List of Dicts")
data = [{'Name': 'Lakshay', 'Age': 20},
        {'Name': 'Shivam', 'Age': 21},
        {'Name': 'Suchitra', 'Age': 22}]
df = pd.DataFrame(data)
print(df)

""" DATA ITERATION """

data={'Name':['Lakshay','Shivam','Sanidhya','Suchitra','Yash'],
      'Marks':[80,85,89,98,88]}
df=pd.DataFrame(data)
print("\n",df)
print("\n",df.loc[0])
print("\n",df.loc[[0,1]])
data={'Name':['Lakshay','Shivam','Sanidhya','Suchitra','Yash'],
      'Marks':[80,85,89,98,88]}
df=pd.DataFrame(data,index=['a','b','c','d','e'])
print("\n",df)
print("\n",df.loc['a'])
print("\nSelecting rows in pandas DataFrame based on conditions")
print(df[df['Marks']>85])
print("\nSelect any row from a Dataframe using iloc[]")
print(df.iloc[[1,2]])
print("\nLimited rows selection with given column")
print(df.loc['a':'d',["Name"]])
print("\nDrop rows from the dataframe based on certain condition applied on a column")
result=df[df['Marks']!=85]
print(result)
print("\nCreate a list from rows in Pandas dataframe")
print(df.values.tolist())