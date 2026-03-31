import pandas as pd
studen_data = {
    "Name": ["Vrook", "Mann", "Kirk"],
    "Age": [20, 21, 22],
    "City": ["Chennai", "Bangalore", "Mumbai"]
}
df = pd.DataFrame(studen_data)
print(df)
df["Age"] = df["Age"] + 2 #Broadcasting
print(df)
df.rename(columns = {"City" : "Place"}, inplace = True) #Renaming columns
print(df)
df.drop(1, axis = 0, inplace = True) #Dropping rows
print(df)
print(df["Age"].value_counts())
df["Age Add"] = [18,56]
print(df)
