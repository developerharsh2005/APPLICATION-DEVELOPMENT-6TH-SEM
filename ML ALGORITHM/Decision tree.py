import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, roc_auc_score


df = pd.read_csv(r"C:\Users\KIIT0001\Desktop\APPLICATION DEVELOPMENT LABORATORY\APPLICATION-DEVELOPMENT-6TH-SEM\ML ALGORITHM\heart.csv")

print("First 5 Rows of Dataset:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())


X = df.drop("target", axis=1)
y = df["target"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

y_pred = dt_model.predict(X_test)


cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

TN, FP, FN, TP = cm.ravel()


accuracy = accuracy_score(y_test, y_pred)
sensitivity = TP / (TP + FN)
specificity = TN / (TN + FP)

print("\nPerformance Metrics:")
print("Accuracy:", round(accuracy, 4))
print("Sensitivity (Recall):", round(sensitivity, 4))
print("Specificity:", round(specificity, 4))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


y_prob = dt_model.predict_proba(X_test)[:, 1]

auc_score = roc_auc_score(y_test, y_prob)
print("AUC Score:", round(auc_score, 4))


fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure()
plt.plot(fpr, tpr, label="Decision Tree (AUC = %0.2f)" % auc_score)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Decision Tree")
plt.legend()
plt.show()