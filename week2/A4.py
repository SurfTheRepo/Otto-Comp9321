import requests
import pandas as pd

def get_json(url):

    resp = requests.get(url=url)
    data = resp.json()
    return data

def json_to_dataframe(json_obj):
    json_data = json_obj['data']
    columns = []
    for c in json_obj['meta']['view']['columns']:
        columns.append(c['name'])

    return pd.DataFrame(data=json_data, columns=columns)



def print_dataframe(dataframe, print_column=True, print_rows=True):
    # print column names
    if print_column:
        print(",".join([column for column in dataframe]))

    # print rows one by one
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))

if __name__ == '__main__':
    url = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json"
    
    print("fetchin json")
    json_obj=get_json(url)

    print("convert the json object to a dataframe")
    df = json_to_dataframe(json_obj)
    print_dataframe(df)