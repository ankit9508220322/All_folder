# fruit = ["apple","banana","orange"]
# print(fruit[0])
# fruit[1]= "cherry"
# print(len(fruit))

# number = [i for i in range(1 ,11)]
# print(number)
# print(number[0:3])
# print(number[-3:])


# assending = [8,5,6,7,4,3,2]
# assending.sort()
# print(assending)
# assending.remove(7)
# print(assending)

# name = ["apple","ram","ankit","bajrangi"]
# name.insert(1 , "mahakal")
# print(name)
# cordinets = (10 , 20)
# print(cordinets[0])
# print(cordinets[1])

# # cordinets[0] = 77
# print(cordinets)
# corlist = list(cordinets)
# corlist[0] = 5
# cordinets = tuple(corlist)
# print(cordinets)

# que1= {1,2,3,4}
# que2 = {4,3,2,4}
# unions =que1.union(que2)
# print(unions)
# intersection = que1.intersection(que2)
# print(intersection)
# diffrent = que1.difference(que2)
# print(diffrent);


contect = {
    "ankit":8484848484884,
    "vikash":9087654526,
    "ajit": 8765432134556
}
print(contect.keys())
print(contect.values())

a = contect.keys()
b = contect.values()
print(a,b)

contectA = {
    "ankit-KUMAR":8484848484884,
    "vikash-KUMAR":9087654526,
    "ajit-PANDIT": 8765432134556
}

for key , value in contect.items():
    print(key ,value)