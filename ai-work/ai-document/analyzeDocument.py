# pip install azure-ai-documentintelligence==1.0.0b4

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, AnalyzeResult

endpoint="https://pal-document-intelligence.cognitiveservices.azure.com/"
key="F0SONMQ5kcWm2oNnpNCkMCd1UNPAKfzYQN3t07gQyzU7PgAn1fBwJQQJ99BIACYeBjFXJ3w3AAALACOGsLso"
documentUrl = "https://palstorageaccount.blob.core.windows.net/pal-documents/Arindam Pal Senior Architect 2025.pdf"

client = DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))
reponse = client.begin_analyze_document("prebuilt-read", AnalyzeDocumentRequest(url_source=documentUrl))
result: AnalyzeResult = reponse.result() # typecast example

for index, para in enumerate(result.paragraphs):
    print(f"Paragraph {index}: {para.content}")

handwritenDocumentUrl = "https://palstorageaccount.blob.core.windows.net/pal-documents/handWritten.jpg"
handwritenReponse = client.begin_analyze_document("prebuilt-read", AnalyzeDocumentRequest(url_source=handwritenDocumentUrl))
handwritenResult: AnalyzeResult = handwritenReponse.result() # typecast example

print(f"Is Handwritten {handwritenResult.styles[0].is_handwritten}")
for para in handwritenResult.pages:
    for index, eachLine in enumerate(para.lines):
        print(f"{index}: {eachLine.content}")

