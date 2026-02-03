import numpy as np 
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print("")
print("___________________________________")
print("")
new_arr= np.insert(arr ,2,[11,12,13,14,15], axis=0 )
new_arr= np.insert(arr ,2,[11,12], axis=1 )

print(new_arr)