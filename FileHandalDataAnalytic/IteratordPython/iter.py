# # check any programe haveing iterator and not iterators
# t = [2,3,4,5]
# print(dir(t))
# g = {1,2,3,4,5}
# print(dir(g))
# f = (1,2,3,4,5)
# print(dir(f))
# ///////////////////////
#L = [2,3,4,5,6]
# L is not iterator
#print(dir(iter(L)))  #jisme for loop calega vah iterator hoga
# /////understanding the for loop work
# num1 = [1,2,3,4,5,6]
# for i in num1:
#     print(num1)

# num = [2,3,4,5,4,3,2]
# iterator = iter(num)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# //////////////////////////////
# create ne apna for loop
# def mera_loop(iterable):
#     iterable = iter(iterable)
#     while True:
#         try:
#             print(next(iterable))
#         except StopIteration:
#             break
# a = [1,2,3,4,5]
# b = {'q','w','e','p'}
# c = {0,9,8,7,6,5}
# d = (2,4,7,8,9)
# mera_loop(b)

