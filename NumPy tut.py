import numpy as np
import time

size = 1000000000
l1 = range(size)
l2 = range(size)


la1 = np.arange(size)
la2 = np.arange(size)

st = time.time()
l3 = [(x * y) for x, y in zip(l1, l2)]
print("Python list time : ", (time.time() - st)*1000)
st = time.time()
la3 = la1 * la2
print("numPy list time: ", (time.time() - st)*1000)
