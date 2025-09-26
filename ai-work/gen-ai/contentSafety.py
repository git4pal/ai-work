# pip install azure-ai-contentsafety


from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential # pip install azure-core
from azure.ai.contentsafety.models import AnalyzeTextOptions, TextCategory

endpoint = "https://pal-content-safety.cognitiveservices.azure.com/"
key="AfjwIHHbbeVCATVNYcemVJVdSLQb6VVi3PjG0oN0ls7swRzlM4IDJQQJ99BIACYeBjFXJ3w3AAAHACOGmgUt"
client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

text_to_analyze = input("Enter some text :")
options = AnalyzeTextOptions(
    text=text_to_analyze,
    categories=[TextCategory.HATE, TextCategory.VIOLENCE, TextCategory.SELF_HARM, TextCategory.SEXUAL],
    halt_on_blocklist_hit=True
)
analysis_result = client.analyze_text(options)
print (analysis_result.categories_analysis)
# for index, categoryAnalysis in enumerate(analysis_result.categories_analysis):
#     print(f"{categoryAnalysis.category} : {categoryAnalysis.severity}")

hate_result = next(item for item in analysis_result.categories_analysis if item.category == TextCategory.HATE)
self_harm_result = next(item for item in analysis_result.categories_analysis if item.category == TextCategory.SELF_HARM)
sexual_result = next(item for item in analysis_result.categories_analysis if item.category == TextCategory.SEXUAL)
violence_result = next(item for item in analysis_result.categories_analysis if item.category == TextCategory.VIOLENCE)

if hate_result:
    print(f"Hate severity: {hate_result.severity}")
if self_harm_result:
    print(f"SelfHarm severity: {self_harm_result.severity}")
if sexual_result:
    print(f"Sexual severity: {sexual_result.severity}")
if violence_result:
    print(f"Violence severity: {violence_result.severity}")
