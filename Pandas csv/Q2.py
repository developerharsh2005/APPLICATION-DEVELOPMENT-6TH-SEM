import pandas as pd

df = pd.read_csv(r"C:\Users\KIIT0001\Documents\employee_salary_10.csv")

df["New_Salary"] = df.apply(
    lambda x: x["Salary"] * 1.10 if x["Experience"] >= 5 else x["Salary"] * 1.05,
    axis=1
)

print(df)
