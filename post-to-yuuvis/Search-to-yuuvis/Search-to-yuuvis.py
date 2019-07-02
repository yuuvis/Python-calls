import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'yuuvis.azure-api.net'

headerDict['Content-Type'] = 'application/json'
headerDict['Ocp-Apim-Subscription-Key'] = '{subscription key}'



session = requests.Session()


#relative path to your new query file
queryFilePath = '/path/to/your/query.json'
response = session.post(str(baseUrl+'/dms/objects/search'), data=open(queryFilePath), headers=headerDict)
print(response.content)

