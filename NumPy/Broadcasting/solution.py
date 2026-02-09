"""What is broadcasting?

Broadcasting is a NumPy feature that lets you perform element-wise operations on arrays of different shapes by automatically expanding the smaller array, without copying data."""
import numpy as np 

prices = np.array([100 , 200 ,300 ,400 ,500,1000])
disnt = 10
fn_price = prices - (prices* disnt/100)
print(fn_price)