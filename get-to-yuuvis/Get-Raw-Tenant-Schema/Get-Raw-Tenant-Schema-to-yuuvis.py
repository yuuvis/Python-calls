import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'yuuvis.azure-api.net'

header_name = 'Ocp-Apim-Subscription-Key'
if header_name != 'Content-Type':
    headerDict['Ocp-Apim-Subscription-Key'] = '{subscription key}'



session = requests.Session()

response = session.get(str(baseUrl+'/admin/schema'), headers=headerDict)
print(response.content)

