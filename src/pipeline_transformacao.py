import pandas as pd

def Readjson(path):
    df = pd.read_json(path)
    return df


path = './results.json'
df = Readjson(path)