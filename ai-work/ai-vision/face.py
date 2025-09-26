# pip install azure-ai-vision-face
import json
from azure.ai.vision.face import FaceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face.models import *


apiKey = "8LcQmwEG4XT7lRnL5w3mWqfkXMwpH1RbH9kQ1E9SdpBm8OzGxFVYJQQJ99BIACYeBjFXJ3w3AAAKACOGFs6Y"
endPoint = "https://pal-face-service.cognitiveservices.azure.com/"
client = FaceClient(endpoint=endPoint, credential=AzureKeyCredential(apiKey))

features = [
    FaceAttributeTypeDetection01.HEAD_POSE,
    FaceAttributeTypeDetection01.OCCLUSION,
    FaceAttributeTypeDetection01.ACCESSORIES
]

with open("images/myImage.JPG", mode="rb") as image_file:
    response = client.detect(
        image_content=image_file.read(),
        detection_model=FaceDetectionModel.DETECTION01,
        recognition_model=FaceRecognitionModel.RECOGNITION01,
        return_face_id=False,
        return_face_attributes=features
    )


print(json.dumps(response[0].as_dict(), indent=2))
