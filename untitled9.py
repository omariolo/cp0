# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YqUB2mBAyn7rXiVUSe-oyMv1CBYCY6Fr
"""

from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same itmes:")
print(num_list)

import numpy as np
m = np.arange(6).reshape(2,3)
print("Original matrix")
print(m)
result = np.trace(m)
print("Condition number of the said matrix:")
print(result)

import numpy as np
x = np.array([[0,2],[3,5]])
print("Original array:")
print(2)
print("Values bigger than 2 =", x[x>2])
print("Their indices are ", np.nonzero(x>2))

i don't understand the exercice 4

import numpy as np
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(x)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)