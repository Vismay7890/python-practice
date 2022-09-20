# Following is the provided numPy array. Return array of items by taking the third column from all rows
import numpy as np
sampleArray = np.array([[11 ,22, 33], 
                        [44, 55, 66], 
                        [77, 88, 99]])
x = sampleArray[...,2]
print(x)