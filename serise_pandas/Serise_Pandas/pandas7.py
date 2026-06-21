import pandas as pd
import numpy as np
# serise with python functionalities (csv file only name sort not value)
# ///(len/dir/sorted/max/min)
data = pd.read_csv('Book3.csv')
print(data)
print(len(data))
# print(dir(data))
# print(sorted(data))
# data2 = pd.read_csv('aaa.csv')
# print(sorted(data2))
# print(min(data2))
# print(max(data2))
# //////////////////////////////
print('type conversion \n')
data2 = pd.read_csv('aaa.csv')
A = list(data2)
print(A)
# //////////////////////////

student={
    'ankit':24,
    'bikash':66,
    'ajit':58,
    'mohit':40,
    'mohit1':40
}
marks = pd.Series(student)
print(list(marks))
print(min(marks))
print(max(marks))
print(sorted(marks))
print(len(marks))

# /// looping method
student={
    'ankit':24,
    'bikash':66,
    'ajit':58,
    'mohit':40,
    'mohit1':40
}
marks = pd.Series(student)
for i in marks:
    print("only show value\n",i)
print('index value thismethod\n')
for i in marks.index:
    print(i)
# //////////////////////////
student={
    'ankit':24,
    'bikash':66,
    'ajit':58,
    'mohit':40,
    'mohit1':40
}
marks = pd.Series(student)
# /Arithmetic operators
print('100 me se kitne kam hai \n',100-marks)
# //////////////////////////////////
# find the kiska mark 50 or 50 se jada hai
score = pd.read_csv('student.csv')
print(score)
A=score.name.value_counts()
print(A)


# ///////////////////
import matplotlib.pyplot as plt
score = pd.read_csv('batsman_runs.csv')
score.plot()   # ✅ function call
plt.show()  

# /////////////////all show name and graph
score = pd.read_csv('batsman_runs.csv')
score.set_index('batter').head(40).plot(kind='bar')
plt.show()
# //create pie chart
score = pd.read_csv('batsman_runs.csv')
score.set_index('batter').head(40).plot(kind='pie')
plt.show()

# ////////////////////////////////
score = pd.read_csv('student.csv')
score.set_index('name').plot()
A=plt.show()
print(A)

# ////////////////////////////////
score = pd.read_csv('student.csv')
# remove extra spaces
score.columns = score.columns.str.strip()
print(score.columns)  # check names
score.set_index('name').plot(kind='bar')
plt.show()
