# Create a 4X2 integer array and Prints its attributes
import numpy as np
x = np.empty([4,2],dtype = np.uint16)
print(x)
print("Shape is:",x.shape)
print("Dimensions:",x.ndim)
print("Length of each element in array is :" , x.itemsize)
