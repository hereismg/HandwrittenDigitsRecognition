import numpy as np
import pandas as pd

m1 = np.array([
    [1, 2, 3],
    [3, 3, 4],
    [4, 4, 5]
])

m2 = np.array([
    [1, 2, 4]
])

m3 = np.array([
    1, 2, 4
])

m31 = m3.reshape((1, -1))
m32 = m3.reshape((-1, 1))

res1 = m1 @ m3.reshape((-1, 1))
res2 = m1 @ m3
print(res1)
print(res2)