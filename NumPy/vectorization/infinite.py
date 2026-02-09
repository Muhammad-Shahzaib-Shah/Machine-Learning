import numpy as np 

arr= np.array([10,20,np.inf, 30, -np.inf, 40])
print(np.isinf(arr))
cleaned_arr = np.nan_to_num(arr , posinf=2000 , neginf=-1000)

print(cleaned_arr)