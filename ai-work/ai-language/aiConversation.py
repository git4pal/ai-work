from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

endpoint="https://pal-language.cognitiveservices.azure.com/"
key="Aj0Ng3rD7agsIn6IVNkXfkMLoomsgYk7SV4gNNfkH92TmjsdKafAJQQJ99BIACYeBjFXJ3w3AAAaACOGuJPQ"

client= ConversationAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
utterance="I need to book a room from 1/2/2026 to 1/5/2026"
projectName="luis-training-model"
deploymentName="TrainedDeployment"

response = client.analyze_conversation(
    task={
        
    }
)