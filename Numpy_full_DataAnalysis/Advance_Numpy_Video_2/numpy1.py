import numpy as np
import time
# numpy array vs python list
# speed list
# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]
# c = []

# start = time.time()

# for i in range(len(a)):
#     c.append(a[i] + b[i])

# print("Time:", time.time() - start)

# //////////////////////////  Numpy method

a = np.arange(10000000)
b = np.arange(10000000,20000000)
start = time.time()
c = a + b

print("\ntime: ",time.time()-start)
