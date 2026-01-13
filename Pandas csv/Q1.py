import pandas as pd

df = pd.read_csv(r"C:\Users\KIIT0001\Documents\students_marks_10.csv")

df["Total Marks"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average Marks"] = df[["Maths", "Science", "English"]].mean(axis=1)

df["Result"] = df["Average Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print(df)
