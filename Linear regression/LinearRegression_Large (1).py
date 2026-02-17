import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

file_path = r"C:\Users\KIIT0001\Desktop\APPLICATION DEVELOPMENT LABORATORY\APPLICATION-DEVELOPMENT-6TH-SEM\Linear regression\house_price_dataset_large.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:", df.shape)
print(df.head())

X = df[['Size (sq ft)']].values
y = df['Price ($)'].values

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

r2 = r2_score(y, y_pred)

print("\n===== Linear Regression (Full Dataset) =====")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R2 Score:", r2)

plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($)")
plt.title("Linear Regression - Large Dataset")
plt.show()
