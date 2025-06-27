import pandas as pd
import numpy as np

""" REGEX PATTERN """
df=pd.DataFrame(['$40.000*','$40000 condition attached'],
                columns=['one']
                )
print(df)

df['one']=df['one'].str.replace(r'\D+','',regex=True).astype('int')
print(df)

print("\nRemove all special characters (keep only alphanumerics)")
df['one'] = df['one'].str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
print(df)

print("\nExtract only numbers (keep decimal)")
df['one'] = df['one'].str.extract(r'(\d+\.\d+|\d+)')
print(df)

print("\nKeep only alphabets (remove numbers and symbols)")
df['one'] = df['one'].str.replace(r'[^a-zA-Z ]', '', regex=True)
print(df)

print("\nExtract only words (no numbers/symbols)")
df['one'] = df['one'].str.findall(r'[a-zA-Z]+').str.join(' ')
print(df)

print("\nExtract first number only")
df['number'] = df['one'].str.extract(r'(\d+)')
print(df)

print("\nExtract everything after a number")
df['after_number'] = df['one'].str.extract(r'\d+(.*)')
print(df)

print("\nKeep only special characters")
df['specials'] = df['one'].str.findall(r'[^a-zA-Z0-9\s]').str.join('')
print(df)

print("\nExtract currency amount with symbol")
df['money'] = df['one'].str.extract(r'(\$\d+(?:\.\d+)?)')
print(df)

""" DATETIME FUNCTION """

df = pd.DataFrame({
    'date_str': ['2025-06-01', '2025-06-15', '2025-06-26']})
date_column = pd.to_datetime(df['date_str'])
print("\nOriginal Dates:\n", date_column)

year = date_column.dt.year
print("\nYear:\n", year)

month = date_column.dt.month
print("\nMonth:\n", month)

day = date_column.dt.day
print("\nDay:\n", day)

day_name = date_column.dt.day_name()
print("\nDay Name:\n", day_name)

weekday = date_column.dt.weekday
print("\nWeekday Number (Mon=0):\n", weekday)

is_month_end = date_column.dt.is_month_end
print("\nIs Month End:\n", is_month_end)

is_leap_year = date_column.dt.is_leap_year
print("\nIs Leap Year:\n", is_leap_year)


""" CSV FILE"""

df=pd.read_csv('data.csv')
print(df['First Name'].value_counts())
print(df.to_string())
print(df.head(5))
print(df.tail(5))
print(df.info(5))
print(df.describe())
print(df.shape)
print(df.columns)
print(df['First Name'])

group_data=df.groupby('City')['Index'].count()
print(group_data)
group_data=df.groupby('City')['Index'].mean()
print(group_data)

pd.options.display.max_rows =999
pd.options.display.max_columns =999
df = pd.read_csv('data.csv')
print(df)
x=df["index"].mean()