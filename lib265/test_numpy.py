import numpy as np

a = np.random.rand(6,6)
print(a,a.shape)

b = np.kron(a,np.ones((2,2)))

print(b,b.shape)