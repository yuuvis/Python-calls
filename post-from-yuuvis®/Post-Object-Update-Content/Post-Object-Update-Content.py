import requests

key = ""
objectId = ""

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Content-Disposition'
headerDict['Content-Disposition'] = ''

header_name = 'Content-Type'
headerDict['Content-Type'] = 'application/octet-stream'

header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

#relative path to your new content file
newContentFilePath = '/path/to/your/new/content.pdf'

response = session.post(str(baseUrl+'/dms/objects/'+objectId+'/contents/file'), data=open(newContentFilePath, 'rb'), headers=headerDict)
print(response.text)
