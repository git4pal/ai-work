# pip install azure-cognitiveservices-vision-customvision
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

predictionKey = "D2GyUDPCcTzNGBP0zQtOwskEZEBp4w2r6eyejIQED5osVdFAke6yJQQJ99BIACYeBjFXJ3w3AAAIACOGUTWd"
endpoint = "https://palcustomvision-prediction.cognitiveservices.azure.com/"


credentials = ApiKeyCredentials(in_headers={"Prediction-key": predictionKey})
prediction_client = CustomVisionPredictionClient(
    endpoint=endpoint, credentials=credentials)

image_data = open("images/customImage.JPG", mode="rb").read()
response = prediction_client.classify_image(
    project_id="a57d1dbb-5814-479c-9615-62e7a3695df5",
    published_name="pal-custom-model",
    image_data=image_data
)
for prediction in response.predictions:
    print(prediction)

print(f"{response.predictions[0].tag_name}")