import requests
import pandas as pd
import os
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

responseDatabase(databaseID,headers)
