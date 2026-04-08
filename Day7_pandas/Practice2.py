import pandas as pd
data={"Fruit":["Apple","Orange","Apple","Banana","Orange","Banana"],"Qty":[10,5,15,8,12,7],"Price":[1.2,0.8,1.5,0.5,0.9,0.6]}
df=pd.DataFrame(data)
df["Total"]=df["Qty"]*df["Price"]
print(df)
print(df.groupby("Fruit")["Qty"].sum())
print(df[df["Price"]>0.7])
