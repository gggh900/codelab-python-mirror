import numpy as np
ENABLE_CONTRACTION=1
CONFIG_UNIFORM_DIM=1
d=2
A=np.random.rand(d+0,d+1,d+2,d+3)
B=np.random.rand(d+0,d+1,d+3,d+2)

if CONFIG_UNIFORM_DIM:
    A=np.random.rand(d,d,d,d)
    B=np.random.rand(d,d,d,d)

if ENABLE_CONTRACTION:
    Ap=np.transpose(A, (0,2,1,3))
    Bp=np.transpose(B, (0,3,1,2))

    if not CONFIG_UNIFORM_DIM:
        App=np.reshape(Ap, ((d+0) * (d+1), (d+2) * (d+3)))
        Bpp=np.reshape(Bp, ((d+3) * (d+2), (d+1) * (d+0)))
    else:
        App=np.reshape(Ap, (d*d,d*d))
        Bpp=np.reshape(Bp, (d*d,d*d))

if ENABLE_CONTRACTION:
    print("A, Ap, App: ", A.shape, Ap.shape, App.shape)
    print("B, Bp, Bpp: ", B.shape, Bp.shape, Bpp.shape)
else:
    print("A, B: ", A.shape, B.shape)

C=np.matmul(A, B)
print("C: ", C.shape)

if ENABLE_CONTRACTION:
    Cpp=np.matmul(App, Bpp)

    if not CONFIG_UNIFORM_DIM:
        C1=np.reshape(Cpp, (d+0, d+1, d+0, d+1))
    else:
        C1=np.reshape(Cpp, (d,d,d,d))

    print("C1: ", C1.shape)

    if np.array_equal(C1, C):
        print("arrays match.")
    else:
        print("!arrays do not match")
        counter = 0
        nonMatch=0

        for i in range(0,d):
            for j in range(0,d):
                for k in range(0,d):
                    for l in range(0,d):
                        if C[i,j,k,l] != C1[i,j,k,l]:
                            nonMatch+=1
                            if counter < 10:
                                print("non matching element: [", i,j,k,l, "]", C[i,j,k,l], C1[i,j,k,l])
                            counter+=1
        print("Non-matching elements: ", nonMatch)

