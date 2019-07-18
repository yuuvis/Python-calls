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


#relative path to your new metadata file
newMetadataFilePath = '/path/to/your/new/metadata.json'

response = session.post(str(baseUrl+'/dms/objects/{objectId}'), data=open(newMetadataFilePath, 'rb'), headers=headerDict)
print(response.json())

