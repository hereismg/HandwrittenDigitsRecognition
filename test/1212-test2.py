import numpy as npy

m1 = npy.array([
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]
])

m2 = npy.array([4, 4, 4])

m3 = npy.array([3, 3, 3])

m4 = m1 * m2.reshape((3, 1))

print(m4)
