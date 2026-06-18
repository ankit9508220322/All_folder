import pandas as pd
import numpy as np
movi =pd.read_csv("imdb_movi.csv",index_col='Series_Title')
data = movi.groupby('Genre').sum()['Gross'].sort_values(ascending=True).head(2)
# print(data)
print(movi.head(2))





















ipl = pd.read_csv("ipl20081.csv")
match = ipl.groupby("city")
# print(match.sum())