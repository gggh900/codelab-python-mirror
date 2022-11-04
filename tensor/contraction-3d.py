
import numpy as np

ENABLE_CONTRACTION=1
CONFIG_UNIFORM_DIM=0
CONFIG_PRINT_TENSORS=1

CONFIG_DATA_TYPE_INT=0
CONFIG_DATA_TYPE_FP32=1
CONFIG_DATA_TYPE=CONFIG_DATA_TYPE_INT
d=2
if CONFIG_DATA_TYPE==CONFIG_DATA_TYPE_FP32:
    A=np.random.rand(d+0,d+1,d+2)
    B=np.random.rand(d+0,d+1,d+3)
elif CONFIG_DATA_TYPE==CONFIG_DATA_TYPE_INT:
    A=np.random.randint(0, high=100, size=(d+0,d+1,d+2))
    B=np.random.randint(0, high=100, size=(d+0,d+1,d+3))
else:
    print("Data type not specified....")
    exit(1)

if CONFIG_UNIFORM_DIM:
    if CONFIG_DATA_TYPE==CONFIG_DATA_TYPE_FP32:
        A=np.random.rand(d,d,d)
        B=np.random.rand(d,d,d)
    elif CONFIG_DATA_TYPE==CONFIG_DATA_TYPE_INT:
        A=np.random.randint(0, high=100, size=(d,d,d))
        B=np.random.randint(0, high=100, size=(d,d,d))
    else:
        print("Data type not specified....")
        exit(1)

if ENABLE_CONTRACTION:
    Ap=np.transpose(A, (0,2,1))
    Bp=np.transpose(B, (0,2,1))

    #Ap=np.transpose(A, (0,2,1,3))
    #Bp=np.transpose(B, (0,3,1,2))

    if not CONFIG_UNIFORM_DIM:
        App=np.reshape(Ap, ((d+0), (d+1) * (d+2)))
        Bpp=np.reshape(Bp, ((d+0), (d+2) * (d+1)))
    else:
        App=np.reshape(Ap, (d,d*d))
        Bpp=np.reshape(Bp, (d,d*d))


if ENABLE_CONTRACTION:
    print("A, Ap, App: ", A.shape, Ap.shape, App.shape)
    print("B, Bp, Bpp: ", B.shape, Bp.shape, Bpp.shape) 
    if CONFIG_PRINT_TENSORS:
        print("A, Ap, App: \n", A, "\n", Ap, "\n", App)
        print("B, Bp, Bpp: \n", B, "\n", Bp, "\n", Bpp)
else:
    print("A, B: ", A.shape, B.shape)

    if CONFIG_PRINT_TENSORS:
        print("A: \n", A)
        print("B: \n", B)


C=np.matmul(A, B)
print("C.shape: ", C.shape)

if CONFIG_PRINT_TENSORS:
    print("C: \n", C)
if ENABLE_CONTRACTION:
    Cpp=np.matmul(App, Bpp)

    if not CONFIG_UNIFORM_DIM:
        C1=np.reshape(Cpp, (d+0, d+1, d+1))
    else:
        C1=np.reshape(Cpp, (d,d,d))

    print("C1: ", C1.shape)
    if CONFIG_PRINT_TENSORS:
        print("C1: ", C1)

    if np.array_equal(C1, C):
        print("arrays match.")
    else:
        print("!arrays do not match")
        counter = 0
        nonMatch=0

        for i in range(0,d):
            for j in range(0,d):
                for k in range(0,d):
                        if C[i,j,k] != C1[i,j,k]:
                            nonMatch+=1
                            if counter < 10:
                                print("non matching element: [", i,j,k,"]", C[i,j,k], C1[i,j,k])
                            counter+=1
        print("Non-matching elements: ", nonMatch)


