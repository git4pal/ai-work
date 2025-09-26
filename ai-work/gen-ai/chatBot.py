# pip install openai

import json
import os
from openai import AzureOpenAI

name = input("What is your name :")
print(f"Hello {name}")
# question = print ("Please give me your question. - ")

endpoint = "https://palar-mfl9bxve-eastus2.cognitiveservices.azure.com/"
model_name = "gpt-5-chat"
deployment = "gpt-5-chat"

subscription_key = "5HvGd0oRFQN5NhxZWvexyY7T5mXUYDSYsRX87MbBFOkzgGF2iGmcJQQJ99BIACHYHv6XJ3w3AAAAACOGDfrP"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_tokens=200,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)
print ("***** RAW Response *****")
print (json.dumps(response.model_dump(), indent=2) )
#print ("***** Response Content *****")
#print(response.choices[0].message.content)
