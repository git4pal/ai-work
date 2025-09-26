# pip install azure-cognitiveservices-vision-computervision
import json
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from azure.ai.vision.imageanalysis.models import VisualFeatures


apiKey = "Ew2wBiUwjbu7giZERDhZhEbqD3YyE92L3aWJp5TM2DvTJlPrJK74JQQJ99BIACYeBjFXJ3w3AAAFACOGYgZw"
endPoint = "https://pal-computer-vision.cognitiveservices.azure.com/"
client = ComputerVisionClient(
    endpoint=endPoint, credentials=CognitiveServicesCredentials(apiKey))

with open("images/brandImage2.JPG", "rb") as image_file:
    response = client.analyze_image_in_stream(
        image=image_file,
        visual_features=[VisualFeatureTypes.brands]
    )

# print (json.dumps(response.as_dict(), indent=2) )
for brand in response.brands:
    print(f"{brand.name}")

# print(response["captionResult"].text)
