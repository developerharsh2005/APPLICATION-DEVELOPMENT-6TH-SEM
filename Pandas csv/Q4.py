import pandas as pd

df = pd.read_csv(r"C:\Users\KIIT0001\Documents\missing_marks_10.csv")

print(df.isnull())

mean_marks = df["Marks"].mean()

df["Marks"] = df["Marks"].fillna(mean_marks)

print(df)
