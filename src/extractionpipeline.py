import requests
import pandas as pd
import os
import json
from dotenv import load_dotenv


load_dotenv()

# Initialisation
token = os.getenv("TOKEN_ACCESS")
databaseID = os.getenv("DATABASE_ID")
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

# Response a Database (this function is not directly relevant to the pagination issue, but kept for completeness)
def responseDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}"
    res = requests.request("GET", readUrl, headers=headers)
    print(res.status_code)

def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    all_results = []
    has_more = True
    next_cursor = None

    while has_more:
        payload = {}
        if next_cursor:
            payload['start_cursor'] = next_cursor

        res = requests.request("POST", readUrl, headers=headers, json=payload)
        res.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        data = res.json()

        all_results.extend(data['results'])
        has_more = data.get('has_more')
        next_cursor = data.get('next_cursor')
        print(f"Fetched {len(data['results'])} rows. Total so far: {len(all_results)}. Has more: {has_more}")

    # Optionally, save the full data to a file
    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump({"results": all_results}, f, ensure_ascii=False, indent=2) # Added indent for readability

    return all_results

data = readDatabase(databaseID, headers)
print(f"Successfully retrieved {len(data)} rows from the Notion database.")