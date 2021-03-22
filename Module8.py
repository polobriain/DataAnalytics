import pandas as pd

data = pd.read_csv("stuff")
data2 = pd.read_csv("stuff2")

new = pd.concat([data, data2])
