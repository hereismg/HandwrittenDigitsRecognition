import numpy as npy

m1 = npy.array([[1, 1, 1],
                [2, 2, 2],
                [3, 3, 3],
                [4, 4, 4]])
m2 = m1 + npy.array([1, 1, 1])
m3 = npy.array([m1, m2])
