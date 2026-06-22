# args will be a tuple of all the value passed tu sum
def sum(*args):
    total = 0
    for item in args:
        total += item
    return total
print(sum(20,10,20,80))

def my_function(*args):
    print(type(args))
    for arg in args:
        print(arg)
        
my_function(1,2,3, "ankit")