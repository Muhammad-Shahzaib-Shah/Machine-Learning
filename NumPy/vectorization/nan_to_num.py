import numpy as np 

arr= np.array([10,20,np.nan, 30, np.nan, 40])
print(np.isnan(arr))

new_arr = np.nan_to_num(arr , nan = 90)
print(new_arr)