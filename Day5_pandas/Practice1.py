import pandas as pd

data = {
    "City": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad"],
    "Temp": [32, 45, 28, 35, 38],
    "Rain": [100, 20, 150, 80, 50]
}

df = pd.DataFrame(data)
print(df)
print(df[df["Temp"] > 30])
print(df[df["Rain"] > 50])
