#https://www.geeksforgeeks.org/numpy-3d-matrix-multiplication/#:~:text=A%203D%20matrix%20is%20nothing,between%20their%20row%2Fcolumn%20vectors.
# [3,3,2] X [3,2,4] = [3,3,4]
# partial:
# [ 6*5+3*9=30+27=57 ... ]
# [ 7*5+4*9=35+36=71  ...]
# [ 5*6+9*9=30+81=111 ...]
import numpy as np
  
np.random.seed(42)
  
A = np.random.randint(0, 10, size=(3, 3, 2))
B = np.random.randint(0, 10, size=(3, 2, 4))
  
print("A:\n{}, shape={}\nB:\n{}, shape={}".format(
  A, A.shape, B, B.shape))

C = np.matmul(A, B)
  
print("Product C:\n{}, shape={}".format(C, C.shape))

