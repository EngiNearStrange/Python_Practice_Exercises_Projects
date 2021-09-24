import numpy as np
a = np.linspace(30, 110, num=59)
y = []
b = 0
while b<59:
    y.append(b)
    b+=1
print(y)
import matplotlib.pyplot as plt
plt.plot(a,y)