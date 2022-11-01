import numpy as np

x = [1, 2, 3]
y = [4, 5, 6]
z = np.matmul(x, y)
print(x, y, z)
print("-----------")
x = np.array([[1,2,3], [4,5,6]])
y = np.array([[4,5,6], [1,2,3]])
for i in x, y, np.matmul(x,y):
    print(i.shape)
