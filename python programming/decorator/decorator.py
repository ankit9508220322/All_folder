import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}ran in {end-start} time")
        return result
    return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)
#     return n
# example_function(2)
# print("jai ram ji ki")

# def decorater(func):
#     def wrapper():
#         print("thid is before function to executed");
#         func()
#         print("this is after executed function");
#     return wrapper

# @decorater
# def say_hello():
#     print("jai ram ji ki jai ho");
# say_hello()


# =====================================
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for _ in range(n):
                func(a)
        return wrapper
    return decorator
@repeat(13)
def greet(name):
    print(f"Hello, {name}!")

greet("world")