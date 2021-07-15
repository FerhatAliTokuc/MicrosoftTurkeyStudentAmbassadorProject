import json
import os
from pprint import pprint
import requests

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = 'PLEASE ENTER YOUR KEY'
endpoint = 'https://api.bing.microsoft.com/v7.0/news/search'

# Query term(s) to search for.
query = "Microsoft Learn Student Ambassadors"

# Construct a request
mkt = 'en-US'
params = { 'q': query, 'mkt': mkt }
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    print("\nHeaders:\n")
    print(response.headers)

    print("\nJSON Response:\n")
    pprint(response.json())
except Exception as ex:
    raise ex