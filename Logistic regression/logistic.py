import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(r"C:\Users\KIIT0001\Desktop\APPLICATION DEVELOPMENT LABORATORY\APPLICATION-DEVELOPMENT-6TH-SEM\Logistic regression\logistic_regression_dataset.csv")


print(df.head())

X = df[["Age", "Income"]].values
y = df["Buy"].values

model = LogisticRegression()
model.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[y==0][:,0], X[y==0][:,1])
plt.scatter(X[y==1][:,0], X[y==1][:,1])

plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Logistic Regression Decision Boundary")
plt.show()
