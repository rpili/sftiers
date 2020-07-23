import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

df = pd.read_csv("data.csv")
df.head()

tier_dict = {
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

df.map(tier_dict)
