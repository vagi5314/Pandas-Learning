import pandas as pd
dirty_employee_data = {
    "EmployeeID": [201, 202, 203, 204, 205, 205],
    "Name": ["Rahul", "Anita ", "suresh", None, "Divya", "Divya"],
    "Age": [28, "32", None, -29, 35, 35],
    "Department": ["HR", "finance", "IT ", "Marketing", "", "Marketing"],
    "Salary": [40000, "55000", None, -45000, 70000, 70000],
    "JoiningDate": ["2021-06-15", "09/10/2020", "Jan 5 2022", None, "2019/03/18", "2019/03/18"]
}
df = pd.DataFrame(dirty_employee_data)
print(df)
print(df.dropna(how="all"))
print(df.dropna(how="any"))
print(df.dropna(subset=["Name"]))
print(df.dropna(subset=["Name"], how="all"))