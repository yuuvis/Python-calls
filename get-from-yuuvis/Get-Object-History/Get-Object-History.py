import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = '{subscription key}'




session = requests.Session()

response = session.get(str(baseUrl+'/dms/objects/{objectId}/history'), headers=headerDict)
print(response)

