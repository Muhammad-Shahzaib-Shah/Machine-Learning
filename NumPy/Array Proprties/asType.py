#Convert data type

import numpy as np 
arr = np.array([1.45,24.4,5,54.9])
print(arr.dtype)
int_arr = arr.astype(int)
print(int_arr.dtype)
print(int_arr)