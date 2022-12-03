import torch

i=2; j=3; k=4; l=5
A = torch.randn(i,j,k)
B = torch.randn(i,l,k)
BT=torch.transpose(B,1,2)
C = torch.randn(l,j,k)

for i in (A,B,BT, C):
    print("shape: ", i.size())
C1=torch.matmul(A, BT)
print("C1 shape: ", C1.size())
C=torch.transpose(C1, 1,2)
print("C shape: ", C.size())
D=torch.matmul(C1, C)
print("D shape: ", D.size())

