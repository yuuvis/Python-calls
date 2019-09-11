import requests

key = ""
objectId = ""

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

#relative path to your new metadata file
newMetadataFilePath = '/path/to/your/new/metadata.json'

response = session.post(str(baseUrl+'/dms/objects/'+objectId), data=open(newMetadataFilePath, 'rb'), headers=headerDict)
print(response.text)
