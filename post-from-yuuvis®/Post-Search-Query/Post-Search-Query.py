import requests
import json

key = ""
#relative path to your new query file
queryFilePath = '/path/to/your/query.json'

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Content-Type'
headerDict['Content-Type'] = 'application/json'
header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.post(str(baseUrl+'/dms/objects/search'), data=open(queryFilePath, 'rb'), headers=headerDict)
print(response.json())
