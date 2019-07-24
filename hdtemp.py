import numpy as np
import pandas as pd

lst = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
ar = np.array(lst)
print(lst)
print(ar)
print(ar.itemsize)
print(ar.ndim)
print(ar.T)
print(np.reshape(ar,(6, 2)))
print(ar.reshape(2, 6))