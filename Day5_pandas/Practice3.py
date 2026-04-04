import pandas as pd

data = {
    "Student": ["A", "B", "C", "D", "E", "F"],
    "Subject": ["Math", "Sci", "Math", "Eng", "Sci", "Math"],
    "Marks": [85, 90, 78, 88, 92, 80]
}

df = pd.DataFrame(data)
print(df["Subject"].value_counts())
print(df["Marks"].describe())
print(df["Marks"].mean())
