# pip install azure-ai-vision-imageanalysis
import json
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures


apiKey= "Ew2wBiUwjbu7giZERDhZhEbqD3YyE92L3aWJp5TM2DvTJlPrJK74JQQJ99BIACYeBjFXJ3w3AAAFACOGYgZw"
endPoint="https://pal-computer-vision.cognitiveservices.azure.com/"
client = ImageAnalysisClient(endpoint=endPoint, credential=AzureKeyCredential(apiKey))

with open("images/ocrImage.JPG", "rb") as image_file:
    image_details=image_file.read()

response = client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.READ]
)
#print (json.dumps(response.as_dict(), indent=2) )
for eachLine in response.read.blocks[0].lines:
    print(f"{eachLine.text}")

#print(response["captionResult"].text)