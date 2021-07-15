from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import json
import os
from pprint import pprint
import requests
# use this code if you're using SDK version is 5.0.0
# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = 'Please enter your key here'
endpoint = 'https://api.bing.microsoft.com/v7.0/news/search'
# Query term(s) to search for.
query = "Microsoft Learn Student Ambassadors"
# Construct a request
mkt = 'en-US'
params = { 'q': query, 'mkt': mkt }
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
# Call the API
def authenticate_client():
    ta_credential = AzureKeyCredential("2771bac383264a6b87553f97fab0a6e7")
    text_analytics_client = TextAnalyticsClient(
        endpoint="https://textanalysfat.cognitiveservices.azure.com/",
       credential = ta_credential)
    return text_analytics_client
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    print("\nHeaders:\n")
    print(response.headers)
    print("\nJSON Response:\n")
    result = response.json()["value"]
    client = authenticate_client()
    for report in result:
        currentdescription=report["description"]
        documents = [currentdescription]
        '''
        print(type(documents))
        break
        '''
        response = client.analyze_sentiment(documents=documents)[0]
        print("Document Sentiment: {}".format(response.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            response.confidence_scores.positive,
            response.confidence_scores.neutral,
            response.confidence_scores.negative,
        ))
        for idx, sentence in enumerate(response.sentences):
            print("Sentence: {}".format(sentence.text))
            print("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
            print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative,
            ))
except Exception as ex:
    raise ex