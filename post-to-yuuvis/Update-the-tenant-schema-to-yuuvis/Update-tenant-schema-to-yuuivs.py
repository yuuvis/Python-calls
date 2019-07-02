import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'yuuvis.azure-api.net'

header_name = 'Content-Type'
if header_name != 'Content-Type':
    headerDict['Content-Type'] = 'multipart/form-data'
header_name = 'Ocp-Apim-Subscription-Key'
if header_name != 'Content-Type':
    headerDict['Ocp-Apim-Subscription-Key'] = '{subscription key}'



session = requests.Session()


#relative path to your schema files
schemaFilePath = '/path/to/your/schema.xml'

multipart_form_data = {
    'file' : ('schema.xml', open(schemaFilePath, 'rb'), 'application/xml')
}

response = session.post(str(baseUrl+'/admin/schema'), files=multipart_form_data, headers=headerDict)
print(response.content)

