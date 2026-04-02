import pandas as pd
practice_data = {
    "EmpID": [301, 302, 303, 304, 305, 305],
    "Name": ["Ravi", "Meena", "Arjun ", "kavya", None, "Kavya"],
    "Age": [25, None, 30, 22, 28, 28],
    "Department": ["IT", "HR ", "finance", "Marketing", "IT", "IT"],
    "Salary": [50000, 60000, None, 45000, 70000, 70000],
    "Experience": [2, 5, 3, None, -1, 3],
    "City": ["Chennai", "Coimbatore ", "Bangalore", "", "Hyderabad", "Hyderabad"],
    "JoinDate": ["2022-05-10", "12/08/2021", "July 1 2020", None, "2023/03/15", "2023/03/15"]
}
df = pd.DataFrame(practice_data)
print(df)
#data cleaning
print(df.dropna(how = "any"))
print(df.dropna(how = "all"))
print(df["Age"].fillna(df["Age"].mean()))
print(df["Salary"].fillna(df["Salary"].mean()))
