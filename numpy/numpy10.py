import numpy as np
A = np.array([[17, 24, 1, 8, 15],
              [23, 5, 7, 14, 16],
              [4, 6, 13, 20, 22],
              [10, 12, 19, 21, 3],
              [11, 18, 25, 2, 9]])

row = A.sum(axis=1)
col = A.sum(axis=0)
d1 = np.diag(A).sum()
d2 = np.diag(np.fliplr(A)).sum()

print(row.min(), row.max(), col.min(), col.max(), d1, d2)
