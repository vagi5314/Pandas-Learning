import pandas as pd

# --- DAY 6: PRACTICE 2 (FILTERING WITH MULTIPLE CONDITIONS) ---
# Goal: Find students who are in 'Math' and have scores above 80.

data = {
    "Student": ["Arun", "Priya", "Karthik", "Sneha", "Vikram", "Rahul"],
    "Subject": ["Math", "Sci", "Math", "Eng", "Sci", "Math"],
    "Marks": [85, 90, 78, 88, 92, 80]
}

df = pd.DataFrame(data)

# FILTERING: We use '&' for AN-D and '|' for OR.
# Remember to wrap each condition in (brackets)!
math_high_score = df[(df["Subject"] == "Math") & (df["Marks"] > 80)]

print("--- Students in Math with Marks > 80 ---")
print(math_high_score)
