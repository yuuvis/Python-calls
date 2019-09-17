import requests

key = ""
objectId = ""
versionNr = ""

headerDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.delete(str(baseUrl+'/dms/objects/'+objectId+'/versions/'+versionNr), headers=headerDict)
print(response)
