# odd veen
def iseven(num):
    if num %2 == 0:
        return 'even'
    else:
        return 'odd'
    
for i in range(1,11):
   print(iseven(i))
# ////////////////////////
def iseven(num):
    if type(num) ==int:
        if num %2 == 0:
           return 'even'
        else:
          return 'odd'
    else:
       return " ontl number suppore "
        

for i in range(1,11):
   print(iseven(i))
print(iseven('ankit'))

# Type of argument
# default function
def power(a = 1,b=1):
   return a**b
response=power(11,2)
print(response)
# Positional Arguments(take value flow the order )
def squre(a,b):
   return (a*a)+ (b*b)
c = squre(2,4)
print(c)
# keyWors argument
def power(a = 1,b = 1):
   return a**b
c = power(b=2,a=8)
print(c)

    