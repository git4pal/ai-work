# import sys
# import os
# module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'common'))
# print (module_path)
# # Add the directory to sys.path
# sys.path.insert(0, module_path)

from audioPlayer import play_audio
import azure.cognitiveservices.speech as speechsdk


endpoint="https://pal-ai-services.cognitiveservices.azure.com/"
key="3zyZbuU4BYknyawkNVMGBWG35dFn8YZER7DHTwE8Di7jj3Ycoen9JQQJ99BIACYeBjFXJ3w3AAAEACOGcYr4"

config = speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)
config.speech_synthesis_voice_name="en-US-CoraMultilingualNeural"
#inputText="My Name is Arindam Pal. I live in Jamison, PA. I like to eat biriyani."
inputText = input("Enter you text :")

output_file="audio/speech01.wav"
audioOutput = speechsdk.audio.AudioConfig(filename=output_file)
speechGenerator = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=audioOutput)
result = speechGenerator.speak_text_async(inputText).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Success")
    play_audio(output_file)
else:
    print("Error")