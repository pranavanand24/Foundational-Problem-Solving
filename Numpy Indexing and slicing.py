import numpy as np

a = np.arange(10)
b = slice(2,7,2)

d = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
 
print(a[b])
print(a[2:])
print(a[2:5])
print(d[1:])