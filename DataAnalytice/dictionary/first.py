# dictionary in python is a collection of key value and pair  ans store the single value and element
# dictionary you can change any number muitable
# indexing not have menning
# key can't be mutable item
# 1D dictinary
num = {
    'name':"ankit",
    'village':"andour",
    'age':33,
    'salary':2000
}
print('one d dictionery\n',num)

#2D dictionary
student={
    'name':"vikash",
    'collage':"kochas",
    'sem':2,
    'subject':{
        'dsa':22,
        'cbot':33,
        'coa':31
    }
}
print('tow D \n',student)
# ///////////////////////////////////
num1 ={'name':"nakit",'age':33,'sub':"dsa"}
A=num1['name']
print(A)
B = num1.get('age')
# add new name
num1['gender']="male"
print(num1)
# /////////////////////////////////////////////////////
# removeing the value(clear , pop, popitem , remove)
num2 ={'name':"ankit",'age':33,'sub':"dsa"}
B = num2.pop('sub')
# popitem delet the last item
C = num2.popitem()
print('the value c\n',C)
# ////////////////////////

# editing  the value 
num2 ={'name':"ankit",'age':33,'sub':"dsa"}
print(num2)
num2['name']="ajit kumar chauney"
print(num2)
# ///////////////////////////////////////////
# dictionary membership
# membership
# iteration
student={
    'name':"vikash",
    'collage':"kochas",
    'sem':2,
    'subject':{
        'dsa':22,
        'cbot':33,
        'coa':31
    }
}
# key print only
for i in student:
    print(i)
    # key and value print 
for i in student:
    print(i,student[i])
# ////////////////////////////////////
num2 = {'name':'abc','age':'22'}
for i in num2:
    print(num2[i])
# //////////////////////////////////////////////
# function discenoray
student={
    'name':"vikash",
    'collage':"kochas",
    'sem':2,
    'subject':{
        'dsa':22,
        'cbot':33,
        'coa':31
    }
}
b=sorted(student)
print(b)
print(len(student))
print(min(student))
print(max(student))
print(student.items())
print(student.keys())
print(student.values())