import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Content-Type'
headerDict['Content-Type'] = 'application/json'
header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = '{subscription key}'



session = requests.Session()


#relative path to your new query file
queryFilePath = '/path/to/your/query.json'
response = session.post(str(baseUrl+'/dms/objects/search'), data=open(queryFilePath, 'rb'), headers=headerDict)
print(response.json())

