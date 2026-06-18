# arg
# allow to pass a variable number of non_keyword argument
# def multply(*args):
#     product = 1
#     for i in args:
#         product = product *i
#     return product
# print(multply(2,3))
# //////////////////////////////////
# kwargs (keywors value)
def display(*kwargs):
    for (key ,value) in  kwargs.items():
        print(key,'->' ,value)
display(india='india',ankit='bikash')