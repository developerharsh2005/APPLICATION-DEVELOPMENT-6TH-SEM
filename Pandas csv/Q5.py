import pandas as pd

df = pd.read_csv(r"C:\Users\KIIT0001\Documents\attendance_10.csv")

shortage = df[df["Attendance"] < 75]

print("Students with attendance < 75%:")
print(shortage)

print("\nTotal number of students with attendance shortage:")
print(len(shortage))
