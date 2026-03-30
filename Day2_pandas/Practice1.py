import pandas as pd
fruit_protein = {
    "Apple": 0.3,
    "Banana": 1.1,
    "Orange": 0.9,
    "Mango": 0.8,
    "Pineapple": 0.5,
    "Strawberry": 0.7,
    "Watermelon": 0.6,
    "Papaya": 0.5,
    "Guava": 2.6,
    "Avocado": 2.0
}
fps = pd.Series(fruit_protein)
print(fps)
print(fps.index)
print(fps['Papaya'])
print(fps.iloc[0:4])
print(fps.loc['Apple':'Mango'])


#conditional selection 
print(fps>0.5)
print(fps[fps>0.5])

#logicalA operators
print(fps[(fps>=0.5) & (fps<=2.0)])
print(fps[(fps>=0.5) | (fps<=2.0)])
print(fps[~(fps>=0.5)])

#modifying
fps["Apple"] = 0.7
print(fps)