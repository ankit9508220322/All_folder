import pandas as pd
import sys
# data = pd.read_csv('movies_data.csv')
# A = sys.getsizeof(data)
# print(A)
# between
# data2 = pd.read_csv('ipl-matches_data.csv')
# B = data2[data2.between(91,51)]
# print(B)
# data2 = pd.read_csv('ipl-matches_data.csv')
# B =data2.drop_duplicates()
# print(B)
# //////////////drop dublicate
data2 = pd.read_csv('ipl-matches_data.csv')
# B =data2.drop_duplicates()
# print(B)
# ///////////////// find duplicate
# c = data2.duplicated().sum()
# print(c)
# # //////// isnull
# d = data2.isnull()
# print(d)
# //// count
e = data2.count()
print(e)
# //////dropna
f = data2.dropna()
print(f)
# ///////////// isin

