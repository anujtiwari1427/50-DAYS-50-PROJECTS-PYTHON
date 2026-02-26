import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {
    "Product": ["Shoes", "Shirt", "Watch", "Shoes", "Watch", "Shirt"],
    "Sales": [5000, 3000, 7000, 4000, 6500, 3500],
    "Month": ["Jan", "Jan", "Jan", "Feb", "Feb", "Feb"]
}

df = pd.DataFrame(data)

# Total sales per product
product_sales = df.groupby("Product")["Sales"].sum()
print(product_sales)

# Visualization
plt.figure()
product_sales.plot(kind="bar")
plt.title("Total Sales per Product")
plt.ylabel("Sales")
plt.show()