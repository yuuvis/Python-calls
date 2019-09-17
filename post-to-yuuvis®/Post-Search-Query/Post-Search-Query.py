import requests
import json

key = ""
#relative path to your new query file
queryFilePath = '/path/to/your/query.json'

headerDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Content-Type'] = 'application/json'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.post(str(baseUrl+'/dms/objects/search'), data=open(queryFilePath, 'rb'), headers=headerDict)
print(response.json())
