import requests

key = ""
#relative path to your schema files
schemaFilePath = '/path/to/your/schema.xml'

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Content-Type'] = 'application/xml'

header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.post(str(baseUrl+'/admin/schema/validate'), data=open(schemaFilePath, 'rb'), headers=headerDict)
print(response.json())
