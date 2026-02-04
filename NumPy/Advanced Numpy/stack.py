"""
vstack row wise
hstack column wise
"""
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10,11,12]])
print(np.vstack((A,B)))
print(np.hstack((A,B)))