'''from operator import methodcaller
def calculatenumber(a, b):
  total = a + b
  print(total)
calculatenumber(10 , 10)
calculatenumber(100 , 400)


def methodnumber2(p, q):
    returns= p +q
    print(returns)
methodnumber2(50 , 50)'''

'''def average(a, b):
    avj = (a + b) / 2
    print(avj)
    
average(10, 20)'''

# argument function
def add(a ,b): 
      x = a +b
      return x
c = add(20 ,30)
print(c)


def average1(*number):
  sum = 0
  for i in number:
    sum = sum +i
    print(sum/len(number))
average1(2,3,4,5,6,7,8)


def name(**name):
  print("helo",name["name"],name["fnamee"],name["mname"],name["lname"]);
  name(name = "ajit",lname = "bajrangi",fname ="mahte");
  
def greed(name):
  return f"helo {name}"
print(greed("ankit"))

# keyword argument
def student (name , age):
  print(f"name: {name} age: {age}")
  
student(age = 18, name="ankit")