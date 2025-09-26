# pip install azure-ai-vision-imageanalysis
import json
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures


apiKey= "Ew2wBiUwjbu7giZERDhZhEbqD3YyE92L3aWJp5TM2DvTJlPrJK74JQQJ99BIACYeBjFXJ3w3AAAFACOGYgZw"
endPoint="https://pal-computer-vision.cognitiveservices.azure.com/"
client = ImageAnalysisClient(endpoint=endPoint, credential=AzureKeyCredential(apiKey))

with open("images/myImage.JPG", "rb") as image_file:
    image_details=image_file.read()

response = client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.TAGS, VisualFeatures.CAPTION, VisualFeatures.OBJECTS]
)
print (json.dumps(response.as_dict(), indent=2) )
print ("\n***** Here are the captions ***** ")
print(response.caption.text)

print ("\n***** Here are the Tags *****")
for eachTag in response.tags.list:
    print(f"{eachTag.name}, confidence score: {eachTag.confidence:.2f}")

print ("\n***** Here are the Objects *****")
for eachObject in response.objects.list:
    for eachTag in eachObject.tags:
        print(eachTag)
        # print(f"{eachTag.name}, confidence score: {eachTag.confidence:.2f}")
