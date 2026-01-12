import pandas as pd

s = pd.Series([[1, 2], [3, 4], [5, 6]])
new_s = s.explode()
print(new_s)
