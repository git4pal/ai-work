# pip install openai

from openai import AzureOpenAI


endpoint = "https://palar-mfl9bxve-eastus2.cognitiveservices.azure.com/"
model_name = "gpt-5-chat"
deployment = "gpt-5-chat"

subscription_key = "5HvGd0oRFQN5NhxZWvexyY7T5mXUYDSYsRX87MbBFOkzgGF2iGmcJQQJ99BIACHYHv6XJ3w3AAAAACOGDfrP"
api_version = "2025-03-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.responses.create(
    input=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_output_tokens=200,
    temperature=1.0,
    model=deployment,
    stream=True
)

for event in response:
    if event.type == "response.output_text.delta":
        print (event.delta, end="")
    elif event.type == "response.output_text.done":
        print()
    


