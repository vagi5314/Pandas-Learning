import pandas as pd
product_data = {
    "Product": ["Apple", "Milk", "Bread", "Mango", "Butter"],
    "Price": [120, 50, 40, 80, 200],
    "Stock": [15, 20, 10, 5, 8]
}

df = pd.DataFrame(product_data).set_index("Product")
print(df)
print(df[["Price", "Stock"]])
print(df.loc["Mango", "Price"])
print(df.iloc[3:5])
print(df.loc[["Apple","Bread"],["Price","Stock"]])
print(df[0:3])
print(df.loc[["Bread","Butter"]])
print(df.loc[["Apple"],["Price", "Stock"]])
df.drop("Price", axis=1, inplace=True)
print(df)
df.drop("Apple", axis=0, inplace=True)
print(df)
df["Stock"] = df["Stock"] + 2
print(df)


