import numpy as np
import pandas as pd
filename = "load.csv"
cols = None
data = []
with open(filename) as f:
	for line in f.readlines():
		vals  = line.replace("\n", "").split(",")
		if cols is None:
			cols = vals

		else:
			data.append([float(x) for x in vals])

d0 = pd.DataFrame(data, columns=cols)
print(d0.dtypes)
d0.head()

d1 = np.loadtxt(filename, skiprows=1, delimiter=",")
print(d1.dtype)
print(d1[:5, :])

d2 = np.genfromtxt(filename, delimiter=",", dtype=None)
print(d2.dtype)
print(d2[:5])

d3 = pd.read_csv(filename)
print(d3.dtypes)
d3.head()
