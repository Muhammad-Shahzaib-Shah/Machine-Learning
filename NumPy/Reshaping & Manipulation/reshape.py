# Reshaping returns a view

import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9,10])
reshaped_arr=arr.reshape(5,2)
print(reshaped_arr)
print(arr)