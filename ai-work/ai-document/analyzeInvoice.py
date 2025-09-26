# pip install azure-ai-documentintelligence==1.0.0b4
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, AnalyzeResult


endpoint="https://pal-document-intelligence.cognitiveservices.azure.com/"
key="F0SONMQ5kcWm2oNnpNCkMCd1UNPAKfzYQN3t07gQyzU7PgAn1fBwJQQJ99BIACYeBjFXJ3w3AAALACOGsLso"
documentUrl = "https://palstorageaccount.blob.core.windows.net/pal-documents/MyInvoice.pdf"

client = DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))
reponse = client.begin_analyze_document("prebuilt-invoice", AnalyzeDocumentRequest(url_source=documentUrl))
result = reponse.result()

for index, doc in enumerate(result.documents):
    print(f" Customer Name : {doc.fields.get("CustomerName").get("valueString")}")
    print(f" Invoice Number : {doc.fields.get("InvoiceId").get("valueString")}")
    print(f" Invoice Total : {doc.fields.get("InvoiceTotal").get("content")}")

# for attrName, attrValue in vars(result.documents[0].fields.__dict__).items():
#     print(f" {attrName} : {attrValue.get("content")}")
    

