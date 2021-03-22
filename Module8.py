import pandas as pd

data = pd.read_csv("FRvideos.csv")
data2 = pd.read_csv("DEvideos.csv")

new = pd.concat([data, data2])

print(new)