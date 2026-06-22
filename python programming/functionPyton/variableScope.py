def sum(a , b):
    c = a + b
    return c
print(sum(2,2))
# //////////////////////////////////////
x=10
def my_fun():
    # local variable
    x = 5
    print(x);
    
my_fun()
# golobal variable this type
print(x) 

# /////////////////////////////////////////
# start new parten
x = 100  # Global variable
def my_func():
    x = 55  # Local variable
    print(x)  # Output: 5

my_func()
print(x)  # Output: 100 (global x remains unchanged)

# //////////////////////////////////
x = 10  # Global variable
def modify_global():
    global x
    x = 55  # Modifies the global x
    
modify_global()
print(x)
# ///////////////////////////////////////

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)


