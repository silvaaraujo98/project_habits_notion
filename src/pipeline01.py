import requests
import pandas as pd
import os
import json
from dotenv import load_dotenv


load_dotenv()

# Initialisation
token = os.getenv("TOKEN_ACCESS")
databaseID =os.getenv("DATABASE_ID")
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}
# Response a Database
def responseDatabase(databaseID,headers):
    readUrl=f"https://api.notion.com/v1/databases/{databaseID}"
    res=requests.request("GET",readUrl,headers=headers)
    print(res.status_code)

def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data['results']


data = readDatabase(databaseID,headers)