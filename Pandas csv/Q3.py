import pandas as pd

df = pd.read_csv(r"C:\Users\KIIT0001\Documents\sales_data_10.csv")

result = df.groupby("Product")["Sales"].agg(["sum", "mean"])

print(result)
