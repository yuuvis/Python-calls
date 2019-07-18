import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Content-Type'
headerDict['Content-Type'] = 'multipart/form-data'

header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = '{subscription key}'




session = requests.Session()


#relative path to your schema files
schemaFilePath = '/path/to/your/schema.xml'

response = session.post(str(baseUrl+'/admin/schema/validate'), data=open(schemaFilePath, 'rb'), headers=headerDict)
print(response.json())

