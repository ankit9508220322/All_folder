'''a = [1,2,3,4,5,6,7,8,9,"ankit"]
print(a)

print(type(a))'''

marks = [22,33,54,76,12,52,61]
# [start ,stop , step]
print((marks[-2]))
# reverse all number
print(marks[::-1])
print(marks[len(marks)-3])
print(marks[5- 3])
print(marks[2])

# find any number in list
marksa= [22,33,54,76,12,52,61]
print(marksa[:3])
if 21 in marksa:
    print("yes")
else:
    print("not this  number in list")

# find any name in list
'''list = ["ankir","vikash","shivam","ajit"]
if "ram "in list:
    print("yes")
else:
    print("noo")'''
    
total = [22,33,44,55,666,77,88,99]
# add the number extra 
total.append(200)
# total.pop() 
total.remove(33)
total.sort()
total.reverse()
total.count(22)
total.copy()
# total.clear()
print(total)
print(total[0:len(total):3])


'''marksA = [2,3,4,5,6,7,8]
marksB = [7,6,5,4,3,2,1]
# murze two data ude the extend command
marksA.extend(marksB)
print(marksA)

a = 2
table = []
for i in range(1, 11):
    table.append((5*i))
print(table);

tablea = [8*i for i in range(1, 20)]
print(tablea)'''
    
# list comprehension print any long number

'''lst = [i+1 for i in range(10)]
print(lst)'''

# print only even number
'''lsta = [i for i in range(100) if i%2 == 0]
print(lsta)'''
'''
number =[x**2 for x in range(1,8)]
print(number)'''

# apply function of each element of loop
fruts = ["apple","ankit","vikash","papaya"]
fruts = "jai ram ji ki"
print(fruts)
print(fruts.upper())

# 
fruts = ["apple","ankit","vikash","papaya"]
for i in fruts:
    print(i)


lsta = ([i for i in range(20)if i%2==0])
print(lsta)

# print the table
table_of = {i: 4*i for i in range(1 , 11)}
print(table_of)

tupal = (2,3,4)
a, b, c = tupal
print(a ,b , c)
2345
# tupal sum number
sum = (2,33,12,44,21,22)
print(sum.count((33)))
# find index
sum.index(33)
print(sum)

# set new chapter start
set = {2,3,4,5,6}
print(set, type(set))

set1 = {22,33,44,55,66}
print(set1)
set1.add(21)
set1.add(11)
print(set1)

a = {2,3,4,5,6}
b = {2,3,7,8,0}
c = a.union(b)
ca = b.intersection(a)
print(ca)
print(c)

# dictionaries and dictionary method

marks = {"ankit": 22, "ajit": 45, "prakash": 33}
print(marks["ajit"])
print(marks)

print(marks.keys())
print(marks.values())
print(marks, type(marks))