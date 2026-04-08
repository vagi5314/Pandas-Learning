import pandas as pd
data={"Name":["Alice","Bob","Charlie","Alice","Bob","Charlie"],"Score":[85,70,95,90,65,80]}
df=pd.DataFrame(data)
df["Bonus"]=df["Score"]+5
print(df)
print(df.groupby("Name")["Score"].mean())
print(df[df["Score"]>80])