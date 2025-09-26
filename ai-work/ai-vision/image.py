import json
import os
from openai import AzureOpenAI

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