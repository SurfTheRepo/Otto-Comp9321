#Activity-4: Merging Two Dataframes

import pandas as pd
import numpy as np

def print_dataframe(dataframe, print_column=True, print_rows=True):
    # print column names
    if print_column:
        print(",".join([column for column in dataframe]))

    # print rows one by one
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))


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

    dfBooks = pd.read_csv('Books.csv')

    dfBooks = clean(dfBooks)
    dfBooks.columns = removeWhiteSpace(dfBooks)
    # dfBooks = [c.replace(' ', '_') for c in dfBooks.columns]
    dfCity = pd.read_csv('City.csv')
    # print(dfCity.info)
    # print(dfBooks.info)

    df = pd.merge(dfBooks, dfCity, how='left', left_on=['Place_of_Publication'], right_on=['City'])

    gb_df = df.groupby(['Country'], as_index=False)

    df = gb_df['Identifier'].count()
    print_dataframe(df)

    df.to_csv("test.csv")