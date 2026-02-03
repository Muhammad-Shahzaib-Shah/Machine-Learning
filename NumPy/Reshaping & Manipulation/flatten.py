"""
Ravel return view
Flatten returns copy
"""
import numpy as np 
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.ravel())
print(arr.flatten())