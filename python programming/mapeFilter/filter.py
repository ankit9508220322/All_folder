def is_grater_then_9(x):
    if x > 9:
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,6,22,33,41,12,9]
new = filter(is_grater_then_9, a)
print(list(new));

    # return x>9
# number = [1,2,33,22,43,12,65];
# new = filter(is_grater_then_9,number)
# print(list(new))
