# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:38:25 2023

@author: belek
"""

import numpy as np

#1
array1=np.arange(15,41);
print(array1)

#2
array2=np.arange(10,25);
print(array2);
# The two arrays do not have the same length
#3
even_array1=np.arange(10,21,2)
print(even_array1);

even_array2=np.arange(34,43,2)

print(even_array2);

arr1=np.array([1,2,3,4]);
arr2=np.array([2,3,4,5]);

addall=np.stack((arr1,arr2), axis=0);
print(addall);

matrix=np.arange(0,36).reshape(6,6);
print(matrix);
print(matrix[2][1])

secondmatrix=np.random.normal(size=(5,2));
print(secondmatrix);
print(secondmatrix[1][1])


# finding the mininum
minimum=np.min(secondmatrix);
print(minimum);

#finding the maximum
maximum=np.max(secondmatrix);
print("th max is ",maximum);


#Finding the standard deviation

standardDeviation=np.std(secondmatrix);

print("This is the standard deviation",standardDeviation);

# Finding the Variance

v=np.var(secondmatrix);
print("Variance:",v);



#finding the Mean

m=np.mean(secondmatrix);
print("Mean:",m);



