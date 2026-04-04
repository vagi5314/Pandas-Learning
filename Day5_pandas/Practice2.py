import pandas as pd

data = {
    "Item": ["Mobile", "Laptop", "Tablet", "Camera", "Headphones"],
    "Price": [15000, 45000, 12000, 35000, 2000],
    "Stock": [10, 5, 8, 3, 15]
}

df = pd.DataFrame(data)
print(df.sort_values(by="Price"))
print(df.sort_values(by="Stock", ascending=False))
print(df.head(3))
