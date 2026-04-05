import pandas as pd

data = {
    "Student": ["Arun", "Priya", "Karthik", "Sneha", "Vikram", "Rahul"],
    "Subject": ["Math", "Sci", "Math", "Eng", "Sci", "Math"],
    "Marks": [85, 90, 78, 88, 92, 80]
}

df = pd.DataFrame(data)

df_sorted = df.sort_values(by="Marks", ascending=False)

print("--- Students Sorted by Highest Marks ---")
print(df_sorted)
