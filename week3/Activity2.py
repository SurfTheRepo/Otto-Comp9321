import pandas as pd
import numpy as np


def print_dataframe(dataframe, print_column=True, print_rows=True):
    if print_column:  
        print(", ".join([column for column in dataframe]))

    if print_rows:
        for row in dataframe.iterrows():
            print(", ".join([str(row[column]) for column in dataframe]))


if __name__ == "__main__":

    df = pd.read_csv('Books.csv')
    
    # print(df['Place of Publication'])

    # print('changing')
    df['Place of Publication'] = df['Place of Publication'].apply(
        lambda x : 'London' if 'London' in x else x.replace('-', ' ')
    )

    print(df['Place of Publication'])
    print("****************************************")

    print(df['Date of Publication'])
    new_date = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    
    new = pd.to_numeric(new_date)
    print(df['Date of Publication'])

    new_date = new_date.fillna(0)
    df['Date of Publication'] = new_date
    print(df['Date of Publication'])