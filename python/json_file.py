import json
file = open("myPackage/data/usagov.bitly.txt", mode='r', encoding='utf-8')
lines = file.readlines()
rows = [json.loads(row) for row in lines]
print('rows : ', len(rows))
for row in rows[:10]:
    print(row)
    print(type(row))
file.close()
import pandas as pd
recode_df = pd.DataFrame(rows)
print(recode_df.info())




