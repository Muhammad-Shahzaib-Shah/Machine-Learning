"""Vectorization means doing operations on entire arrays at once instead of using loops, by relying on optimized low-level (C) code."""
import numpy as np 

array = np.array([100 , 200 ,300 ,400 ,500,1000])
arr_mul = array /10
print(arr_mul)
print(arr_mul.astype(int))