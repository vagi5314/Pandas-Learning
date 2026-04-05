import pandas as pd

# --- DAY 6: PRACTICE 1 (SORTING) ---
# Goal: Sort our student list to see who got the highest marks first.

data = {
    "Student": ["Arun", "Priya", "Karthik", "Sneha", "Vikram", "Rahul"],
    "Subject": ["Math", "Sci", "Math", "Eng", "Sci", "Math"],
    "Marks": [85, 90, 78, 88, 92, 80]
}

df = pd.DataFrame(data)

# SORTING: We use sort_values()
# 'ascending=False' puts the highest number on top!
df_sorted = df.sort_values(by="Marks", ascending=False)

print("--- Students Sorted by Highest Marks ---")
print(df_sorted)
