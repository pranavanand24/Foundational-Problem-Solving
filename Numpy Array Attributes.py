import numpy as np

a = np.array([[1,2,3], [3,4,5]])

a.shape = (3,2)
b = a.reshape(3,2)

c = np.arange(24)

d = c.reshape(2,3,4)

e = np.array([1,2,3,4,5])

print(a)
print(b)
print(c)
print(d)
print(e.flags)