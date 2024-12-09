import pandas as pd
import matplotlib.pyplot as plt

# load data onto pandas dataframe
df = pd.read_excel('RBRTEd.xls', sheet_name = 'Data 1', skiprows = 2)
df = df.rename(columns = {'Sourcekey': 'Date','Europe Brent Spot Price FOB (Dollars per Barrel)': 'Price'})

# convert all values to numerical
df['Date'] = pd.to_datetime(df['Date'])
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# print to check
print(df)
print(df.columns)