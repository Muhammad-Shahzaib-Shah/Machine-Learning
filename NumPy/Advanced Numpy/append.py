import numpy as np 
arr = np.array([1,2,3,5,6,7,8,9,10])
print(arr)
new_arr= np.append(arr , 11 )
print(new_arr)

# For 2D
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)
print("")
print("___________________________________")
print("")
new_arr2= np.append(arr2, [[11,12,13,14,15]] , axis=0)
new_arr3= np.append(arr2, [[11],[12]] , axis=1)
print(new_arr2)
print(new_arr3)