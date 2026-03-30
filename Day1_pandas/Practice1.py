import pandas as pd
series = pd.Series([10,56,79,64,45,18])
print(series)
print(series.values)
print(series.index)
series.name = "List"
print(series)
print(series[0:4])
print(series.iloc[0:2])
series.index = ["a","b","c","d","e","f"]
print(series)
print(series.iloc[0:2])
print(series.loc["a":"d"])