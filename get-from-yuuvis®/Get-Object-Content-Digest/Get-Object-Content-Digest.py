import requests

key = ""
objectId = ""

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.get(str(baseUrl+'/dms/objects/'+objectId+'/actions/validate/digest'), headers=headerDict)
print(response)
