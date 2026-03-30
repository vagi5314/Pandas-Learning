import pandas as pd
customer_data = {
    "CustomerID": [101, 102, 103, 104, 105],
    "Name": ["Arun", "Priya", "Karthik", "Sneha", "Vikram"],
    "Age": [23, 27, 22, 25, 30],
    "City": ["Coimbatore", "Chennai", "Bangalore", "Hyderabad", "Mumbai"],
    "PurchaseAmount": [2500, 3200, 1500, 2800, 4000]
}
df = pd.DataFrame(customer_data)
print(df)
print(df.head(3))
print(df.tail(2))
print(df.iloc[0:4])
print(df.index)
print(df.values)
#
print(df[0:2], ["Name", "Age"])
print(df.loc[0:2], ["Name", "Age"])