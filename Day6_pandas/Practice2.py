import pandas as pd

data = {
    "Student": ["Arun", "Priya", "Karthik", "Sneha", "Vikram", "Rahul"],
    "Subject": ["Math", "Sci", "Math", "Eng", "Sci", "Math"],
    "Marks": [85, 90, 78, 88, 92, 80]
}

df = pd.DataFrame(data)

math_high_score = df[(df["Subject"] == "Math") & (df["Marks"] > 80)]

print("--- Students in Math with Marks > 80 ---")
print(math_high_score)
