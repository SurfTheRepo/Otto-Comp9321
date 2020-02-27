#!/usr/bin/python3

import pandas as pd
import numpy as np

df = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv')

print(df.columns)

for index, row in df.iterrows():
    print(",".join([str(row[column]) for column in df]))

df.to_csv('Save.csv')