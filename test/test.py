import numpy as npy

m1 = npy.array([1, 2, 3])

m2 = npy.tile(m1.reshape((1, -1)), 5).T
print(m2)