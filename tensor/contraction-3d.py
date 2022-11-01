import numpy as np
d=10
A=np.random.rand(d+0,d+1,d+2)
B=np.random.rand(d+0,d+2,d+1)

'''
Ap=np.transpose(A, (0,2,1,3))
Bp=np.transpose(B, (0,3,1,2))
App=np.reshape(Ap, ((d+0) * (d+1), (d+2) * (d+3)))
Bpp=np.reshape(Bp, ((d+3) * (d+2), (d+1) * (d+0)))

print("A, Ap, App: ", A.shape, Ap.shape, App.shape)
print("B, Bp, Bpp: ", B.shape, Bp.shape, Bpp.shape)
'''

print("A: ", A.shape)
print("B: ", B.shape)
C=np.matmul(A, B)
print("C: ", C.shape)
#Cpp=np.matmul(App, Bpp)
#print("Cpp: ", Cpp.shape)
