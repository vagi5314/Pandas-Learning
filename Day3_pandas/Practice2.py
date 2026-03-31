import pandas as pd
student_data = ["Arun", "Priya", "Karthik"]
df = pd.DataFrame(student_data, columns=["Name"])
df.index = [1,2,3]
print(df)
print(df.iloc[1:3])
print(df.loc[1:3])
print(df.loc[1:3, "Name"])