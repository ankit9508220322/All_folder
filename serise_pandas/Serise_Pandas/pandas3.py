import pandas as pd

# ////value _count->movies
# data = pd.read_csv('Book3.csv')
# print(data)
# print(data.city.value_counts())
# c = data.stTE.sort_values()
# print(c)
# //////////// index_sort
data = pd.read_csv('Book3.csv')
print('original value\n',data)
A=data.city.sort_index()
print("sort index value \n",A)
# /////////////////////////////////
# sort accending value
data = pd.read_csv('Book3.csv')
B = data.sort_values('city')
print("Sorted by city:\n", B)

# ////////////////////////////////////////
