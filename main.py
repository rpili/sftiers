import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

df = pd.read_csv("data.csv", header=None)
df.rename(columns={0:"character"}, inplace=True)
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
print(df.head()) 


tier_dict = {
    "S+":14,
    "S":13,
    "S-":12,
    "A+":11,
    "A":10,
    "A-":9,
    "B+":8,
    "B":7,
    "B-":6,
    "C+":5,
    "C":4,
    "C-":3,
    "D+":2,
    "D":1
    }

#for column in df.columns:
#    df[column].map(tier_dict)

#df[1].map(tier_dict)
#print(df.iloc[5,1], type(df.iloc[5,1]))

df = df.replace(tier_dict)
df.set_index('character', inplace=True)
df = df.transpose()

print(df)
