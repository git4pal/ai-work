from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://pal-language.cognitiveservices.azure.com/"
key="Aj0Ng3rD7agsIn6IVNkXfkMLoomsgYk7SV4gNNfkH92TmjsdKafAJQQJ99BIACYeBjFXJ3w3AAAaACOGuJPQ"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))


documents = [
    'apni kemon aachen, ami bhalo aachi'
]

# ********** LANGUAGE DETECTION ********** #
print ("\n********** LANGUAGE DETECTION **********")
response= client.detect_language(documents)
for eachLang in response:
    print(f"{eachLang.primary_language.name}, confidence score: {eachLang.primary_language.confidence_score:.2f}")

# ********** SENTIMENT ANALYSIS ********** #
print ("\n********** SENTIMENT ANALYSIS **********")
sentimentDocument=[
    "We ordered a pizza and it must have been delivered to the wrong address because we did not receive it. We ordered on the app which has our address included so I don't know how this could happen???",
    "I ordered a 1/2 and 1/2 pizza to go. Toppings were distributed fairly well. The pizza tasted fine, "
]
sentimentResponse = client.analyze_sentiment(sentimentDocument)
for eachSentiment in sentimentResponse:
    for eachSentense in eachSentiment.sentences:
        print(f"{eachSentense.text}: Sentence Sentiment: {eachSentense.sentiment}; Overall: {eachSentiment.sentiment}")

# ********** EXTRACT KEY PHRASE ********** #
print ("\n********** EXTRACT KEY PHRASE **********")
keyPhraseDocument=[
    "I live in Jamison PA. I like to go to school everyday. I study in CB East high school. I like to get some biriyani in lunch."
]
keyPhraseResponse = client.extract_key_phrases(keyPhraseDocument)[0]
for keyPhrase in keyPhraseResponse.key_phrases:
    print(keyPhrase)


# ********** NAMED ENTITY ********** #
print ("\n********** NAMED ENTITY **********")
namedEntityDocument=[
    "George Washington is the first president of United States of America"
]
namedEntityResponse = client.recognize_entities(namedEntityDocument)[0]
for namedEntity in namedEntityResponse.entities:
    print(f"{namedEntity.text} ( {namedEntity.category} )")

