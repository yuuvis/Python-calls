import requests

key = ""
objectId = ""
versionNr = ""

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.get(str(baseUrl+'/dms/objects/'+objectId+'/versions/'+versionNr+'/actions/validate/digest'), headers=headerDict)
print(response)
