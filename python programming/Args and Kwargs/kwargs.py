# kwargs is a dictionary with all the key value pairs with were passed to make
def marks(**kwargs):
    for item in kwargs.keys():
        print(f"the marks of {item} is {kwargs[item]}")
        # print(kwargs[item]);
marks(ankit = 99, amit=44, ajit=43)