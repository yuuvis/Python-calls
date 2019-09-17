import requests

key = ""
objectId = ""
versionNr = ""

headerDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.get(str(baseUrl+'/dms/objects/'+objectId+'/versions/'+versionNr+'/contents/file'), headers=headerDict)
print(response.text)
