import numpy as np
import cmath

from numpy.lib.index_tricks import r_
# Given data 'x' as years and 'y' as time taken
x = [1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972,
     1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
y = [12.20, 11.90, 11.15, 11.90, 11.50, 11.50, 11.00, 11.40, 11.00, 11.07,
     11.08, 11.06, 10.97, 10.54, 10.82, 10.94, 11.12, 10.93, 10.78, 10.75, 10.71]
sum_x = sum(x)
print("Sum of all elements of x is:",sum_x)
sum_y = sum(y)
print("Sum of all elements of y is:",sum_y)

meanx = sum(x)/len(x)
print("Mean of x is:",meanx)
meany = sum(y)/len(y)
print("Mean of y is:",meany)
xi_meanx=[]
for i in range(len(x)):
    xi_meanx.append(x[i]-meanx)
xi_meanx = np.array(xi_meanx)
yi_meany=[]
for i in range(len(y)):
    yi_meany.append(y[i]-meany)
yi_meany = np.array(yi_meany)
sigy_lower = sum(yi_meany**2)
upper = xi_meanx * yi_meany
b1_upper = sum(upper)
lower = xi_meanx**2
b1_lower = sum(lower)
b1 = b1_upper/b1_lower
print("B1 is:",b1)
b0 = meany - (b1*meanx)
year = int(input("Enter the prediction olympic year:"))
y_prediction = b0 + (b1*year)
print("Prediction time for year",year,"is:",y_prediction)
sigx = cmath.sqrt(b1_lower/len(x))
sigy = cmath.sqrt(sigy_lower/len(y))
r_upper = b1_upper/len(x)
r_lower = sigx*sigy
r_sqr = (r_upper/r_lower)**2
print("Coefficient of determinatoin is:",r_sqr)