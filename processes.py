import pandas as pd

with open("iris.data") as f:
    data= f.read()
    data= data.split("\n")

newData = []
for line in data:
    newData.append(line.split(","))
df= pd.DataFrame(newData, columns=["D1","D2","D3","D4","Type"])
df.to_csv("process.csv", index=False)