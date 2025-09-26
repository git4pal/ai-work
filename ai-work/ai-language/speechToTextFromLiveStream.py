import azure.cognitiveservices.speech as speechsdk

endpoint="https://pal-ai-services.cognitiveservices.azure.com/"
key="3zyZbuU4BYknyawkNVMGBWG35dFn8YZER7DHTwE8Di7jj3Ycoen9JQQJ99BIACYeBjFXJ3w3AAAEACOGcYr4"

config = speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)
config.speech_recognition_language="en-US"
audioInput = speechsdk.AudioConfig(use_default_microphone=True)
txtGenerator = speechsdk.SpeechRecognizer(speech_config=config, audio_config=audioInput)
result= txtGenerator.recognize_once_async().get()
print(f"Here is the text: {result.text}")
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Success")
else:
    print("Error")