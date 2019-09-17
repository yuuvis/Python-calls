import requests

key = ""
#relative path to your content file
contentFilePath = '/path/to/your/content.pdf'
#relative path to your metadata file
metaDataFilePath = '/path/to/your/metadata.json'

headerDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

multipart_form_data = {
    'data' :('data.json', open(metaDataFilePath, 'rb'), 'application/json'),
    'cid_63apple' : ('content.pdf', open(contentFilePath, 'rb'), 'application/pdf')
}

response = session.post(str(baseUrl+'/dms/objects'), files=multipart_form_data, headers=headerDict)
print(response.json())
