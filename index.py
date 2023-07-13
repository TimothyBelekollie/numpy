# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:35:10 2023

@author: belek
"""

import numpy as np
import pandas as pd

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

#s=one.reshape(5,10);
#print(s)

o=np.linspace(0,7,10)

#print(o)

r=o.resize(2,5)
print(r)

# Generating random numbers

print(np.random.rand(3,2))

print(np.random.randn(3,3))

print(np.random.randint(2,20,10))

myint=np.random.randint(2,10,30)
print(myint)

#broadcasting

myint[myint>7]=10

print(myint)

# how to create a copy of a dataset

myint2=myint

myint3=myint2.copy()

data=pd.read_csv('products.csv');

#print(data.head());

my_copy=data.copy();
print(my_copy.head());















