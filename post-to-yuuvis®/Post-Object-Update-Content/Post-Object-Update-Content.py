import requests

key = ""
objectId = ""

headerDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

#relative path to your new content file
newContentFilePath = '/path/to/your/new/content.pdf'

response = session.post(str(baseUrl+'/dms/objects/'+objectId+'/contents/file'), data=open(newContentFilePath, 'rb'), headers=headerDict)
print(response.text)
