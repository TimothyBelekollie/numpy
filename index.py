# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:35:10 2023

@author: belek
"""

import numpy as np

m=[1,2,3,4]
v=np.array(m)
print("this is array",v)

#creating a multidimensional Array

mult=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(mult)

#arrange

print(np.arange(0,11))

#zeros, Ones and Eye functions 

zero=np.zeros(100);
print(zero);

one=np.ones((3,3));

print(one);

#eye

eye=np.eye(10);
print(eye);

# Reshape function

s=one.reshape(5,10);
print(s)












