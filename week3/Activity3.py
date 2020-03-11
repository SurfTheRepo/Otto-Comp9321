#Filtering Rows

import pandas as pd
import numpy as np


def print_dataframe(dataframe, print_column=True, print_rows=True):
    if print_column:  
        print(", ".join([column for column in dataframe]))

    if print_rows:
        for index, row in dataframe.iterrows():
            print(", ".join([str(row[column]) for column in dataframe]))


def clean(df):
    df['Place of Publication'] = df['Place of Publication'].apply(
        lambda x : 'London' if 'London' in x else x.replace('-', ' ')
    )


    new_date = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    new_date = pd.to_numeric(new_date)
    new_date = new_date.fillna(0)
    df['Date of Publication'] = new_date
    
    return df


def removeWhiteSpace(df):
    return [c.replace(' ', '_') for c in df.columns]


if __name__ == "__main__":

    df = pd.read_csv('Books.csv')
    df = clean(df)

    df.columns = removeWhiteSpace(df)

    df = df.query('Date_of_Publication > 1866 and Place_of_Publication == "London"')
    
    print_dataframe(df)

