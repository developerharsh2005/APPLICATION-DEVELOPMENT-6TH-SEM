import pandas as pd

data = []

for i in range(5):
    print(f"Product {i+1}:")
    name = input("Name: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    rating = float(input("Rating: "))

    data.append([name, category, quantity, price, rating])

df = pd.DataFrame(data, columns=["Product", "Category", "Quantity", "Price", "Rating"])

df["Revenue"] = df["Quantity"] * df["Price"]

category_revenue = df.groupby("Category")["Revenue"].sum()
print("\nCategory Revenue:")
for cat, rev in category_revenue.items():
    print(f"{cat}: ₹{int(rev)}")

best_selling = df.loc[df["Quantity"].idxmax()]
print("\nBest Selling Product:")
print(best_selling["Product"])

print("\nRating Distribution:")
print(df["Rating"].value_counts())

print("\nSales Performance Report:")
print(df)
