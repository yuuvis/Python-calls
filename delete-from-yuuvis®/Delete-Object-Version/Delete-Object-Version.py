import requests

key = ""
objectId = ""
versionNr = ""

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.delete(str(baseUrl+'/dms/objects/'+objectId+'/versions/'+versionNr), headers=headerDict)
print(response)
