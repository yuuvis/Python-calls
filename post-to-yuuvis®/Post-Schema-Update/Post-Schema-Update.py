import requests

key = ""
#relative path to your schema files
schemaFilePath = '/path/to/your/schema.xml'

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Content-Type'] = 'application/xml'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

headerDict['Content-Type'] = 'application/xml'

response = session.post(str(baseUrl+'/admin/schema'), data=open(schemaFilePath, 'rb'), headers=headerDict)
print(response.text)
