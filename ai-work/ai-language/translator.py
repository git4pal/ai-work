from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

endpoint="https://api.cognitive.microsofttranslator.com/"
key="C48dDwyLSB0NrLQup5fnF78iqSed1kF9l0uz4DbZ4pF3ZoWFTguuJQQJ99BIACYeBjFXJ3w3AAAbACOGhpc8"
region="eastus"

credential=TranslatorCredential(key, region)
client = TextTranslationClient(credential=credential, endpoint=endpoint)

sourceLanguage="en"
targetLanguage=["bn"]
inputText = input("Enter you text :")

documents=[
    InputTextItem(text=inputText)
]
response = client.translate(content=documents, to=targetLanguage, from_parameter=sourceLanguage)[0]
print(f"Translated Text : {response.translations}")