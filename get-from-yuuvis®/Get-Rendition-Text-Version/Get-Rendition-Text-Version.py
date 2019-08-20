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

response = session.get(str(baseUrl+'/dms/objects/'+objectId+'/versions/'+versionNr+'/contents/renditions/text'), headers=headerDict)
print(response.text)
