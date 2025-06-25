
"""## Good method"""

import pandas as pd

df = pd.read_csv('weather_data.csv')

df = pd.read_excel('weather_data.xlsx')

df

print(df)

print(type(df))



