import json
file = open("myPackage_Database/data/labels.json", mode='r', encodings="utf-8")
lines = json.load(file)
print(type(lines))
print(len(lines))
print(type(lines[0]))
import pandas as pd
df = pd.DataFrame(lines)
print(df.info())
print(df.head())